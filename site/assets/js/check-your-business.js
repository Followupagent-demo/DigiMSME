// "Check Your Business" wizard: industry -> scale -> tools -> (dept if
// Large) -> pain points -> a composite automation flow assembled live
// in the browser from real module workflow files, rendered with the
// same components used everywhere else (process-runner.js /
// workflow-canvas.js), ending in a WhatsApp CTA prefilled with the
// visitor's own answers.
(function () {
  var dataEl = document.getElementById("cyb-data");
  var wizard = document.getElementById("cyb-wizard");
  if (!dataEl || !wizard) return;

  var CYB;
  try { CYB = JSON.parse(dataEl.textContent); } catch (e) { return; }

  var state = { industry: null, scale: null, tools: [], dept: null, pains: [] };
  var stepIndex = 0;

  function currentSteps() {
    var all = ["industry", "scale", "tools", "department", "pains"];
    return state.scale === "large" ? all : all.filter(function (s) { return s !== "department"; });
  }

  function goToStep(i) {
    var steps = currentSteps();
    if (i >= steps.length) { showResult(); return; }
    if (i < 0) i = 0;
    stepIndex = i;
    var name = steps[i];
    document.querySelectorAll(".cyb-step").forEach(function (el) {
      el.hidden = el.getAttribute("data-step") !== name;
    });
    var bar = document.getElementById("cyb-progress-bar");
    if (bar) bar.style.width = Math.round(((i + 1) / steps.length) * 100) + "%";
  }

  function advance() { goToStep(stepIndex + 1); }

  function wireSingleSelect(stepName, stateKey) {
    var root = document.querySelector('.cyb-step[data-step="' + stepName + '"]');
    if (!root) return;
    root.querySelectorAll(".cyb-chip").forEach(function (chip) {
      chip.addEventListener("click", function () {
        root.querySelectorAll(".cyb-chip").forEach(function (c) { c.classList.remove("is-active"); });
        chip.classList.add("is-active");
        state[stateKey] = chip.getAttribute("data-value");
        setTimeout(advance, 180);
      });
    });
  }

  function wireMultiSelect(stepName, stateKey, onChange) {
    var root = document.querySelector('.cyb-step[data-step="' + stepName + '"]');
    if (!root) return;
    root.querySelectorAll(".cyb-chip").forEach(function (chip) {
      chip.addEventListener("click", function () {
        chip.classList.toggle("is-active");
        var val = chip.getAttribute("data-value");
        var idx = state[stateKey].indexOf(val);
        if (idx === -1) state[stateKey].push(val); else state[stateKey].splice(idx, 1);
        if (onChange) onChange();
      });
    });
  }

  wireSingleSelect("industry", "industry");
  wireSingleSelect("scale", "scale");
  wireSingleSelect("department", "dept");
  wireMultiSelect("tools", "tools");
  wireMultiSelect("pains", "pains", function () {
    var btn = document.getElementById("cyb-generate-btn");
    if (btn) btn.disabled = state.pains.length === 0;
  });

  var toolsNext = document.getElementById("cyb-tools-next");
  if (toolsNext) toolsNext.addEventListener("click", advance);

  var startBtn = document.getElementById("cyb-start-btn");
  if (startBtn) {
    startBtn.addEventListener("click", function () {
      document.getElementById("cyb-intro").hidden = true;
      wizard.hidden = false;
      goToStep(0);
      wizard.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }

  var genBtn = document.getElementById("cyb-generate-btn");
  if (genBtn) {
    genBtn.disabled = true;
    genBtn.addEventListener("click", function () { showResult(); });
  }

  // ---------------- workflow parsing (mirrors build.py's _wf_load / _wf_primary_path) ----------------
  var N8N_NODE_STYLE = {
    "n8n-nodes-base.webhook": ["⚡", "n8n-node-trigger"],
    "n8n-nodes-base.scheduleTrigger": ["🕒", "n8n-node-trigger"],
    "n8n-nodes-base.wait": ["⏱", "n8n-node-wait"],
    "n8n-nodes-base.httpRequest": ["🌐", "n8n-node-action"],
    "n8n-nodes-base.if": ["🔀", "n8n-node-condition"],
    "n8n-nodes-base.noOp": ["✅", "n8n-node-done"],
  };

  function nodeIcon(n) {
    var pair = N8N_NODE_STYLE[n.type] || ["⚙️", "n8n-node-action"];
    var icon = pair[0], cls = pair[1];
    var name = n.name;
    if (name.indexOf("Lost") === 0 || name.indexOf("❌") === 0 || name.indexOf("Competitor Wins") !== -1) { icon = "❌"; cls = "n8n-node-danger"; }
    else if (name.indexOf("Staff") === 0 || name.indexOf("Manual") === 0) { icon = "🧍"; cls = "n8n-node-manual"; }
    else if (name.indexOf("AI:") === 0 || name.indexOf("AI ") === 0) { icon = "🧠"; cls = "n8n-node-ai"; }
    else if (name.indexOf("WhatsApp") !== -1) { icon = "💬"; }
    else if (name.indexOf("Email") !== -1) { icon = "✉️"; }
    else if (name.indexOf("Alert") !== -1) { icon = "🔔"; }
    else if (name.indexOf("Check") !== -1 || name.indexOf("Sentiment") !== -1) { icon = "🔍"; }
    return [icon, cls];
  }

  function primaryPath(wf) {
    var nodesByName = {};
    wf.nodes.forEach(function (n) { nodesByName[n.name] = n; });
    var connections = wf.connections || {};
    var incoming = {};
    Object.keys(connections).forEach(function (src) {
      (connections[src].main || []).forEach(function (branch) {
        branch.forEach(function (c) { incoming[c.node] = true; });
      });
    });
    var startCandidates = wf.nodes.filter(function (n) { return !incoming[n.name]; });
    var pool = startCandidates.length ? startCandidates : wf.nodes;
    var start = pool.reduce(function (a, b) { return a.position[0] <= b.position[0] ? a : b; });
    var path = [], seen = {}, cur = start.name;
    while (cur && !seen[cur]) {
      seen[cur] = true;
      var n = nodesByName[cur];
      if (!n) break;
      path.push(n);
      var branches = (connections[cur] || {}).main || [];
      cur = (branches[0] && branches[0][0]) ? branches[0][0].node : null;
    }
    return path;
  }

  function fetchModule(modId) {
    var meta = CYB.modules[modId];
    var filename = meta ? meta.file : modId + ".json";
    return fetch("/assets/n8n-workflows/" + filename)
      .then(function (r) { return r.json(); })
      .then(function (wf) { return { id: modId, wf: wf }; });
  }

  // ---------------- composite assembly + rendering ----------------
  var NODE_W = 210, NODE_H = 64, PAD = 60, GAP = 140, SCALE = 0.85;

  function buildComposite(mods) {
    var runningX = 0;
    var allNodes = [], allEdges = [], mobileSteps = [];
    mods.forEach(function (mod, mi) {
      var path = primaryPath(mod.wf);
      if (!path.length) return;
      var xs = path.map(function (n) { return n.position[0]; });
      var ys = path.map(function (n) { return n.position[1]; });
      var minX = Math.min.apply(null, xs), minY = Math.min.apply(null, ys);
      var moduleNodes = path.map(function (n) {
        var iconCls = nodeIcon(n);
        return {
          key: mi + "::" + n.name,
          label: n.name,
          icon: iconCls[0],
          cls: iconCls[1],
          x: runningX + Math.round((n.position[0] - minX) * SCALE),
          y: 60 + Math.round((n.position[1] - minY) * SCALE),
        };
      });
      var prevLastNode = allNodes.length ? allNodes[allNodes.length - 1] : null;
      for (var i = 0; i < moduleNodes.length; i++) {
        allNodes.push(moduleNodes[i]);
        mobileSteps.push(moduleNodes[i]);
        if (i > 0) allEdges.push({ from: moduleNodes[i - 1].key, to: moduleNodes[i].key });
      }
      if (mi > 0 && prevLastNode) allEdges.push({ from: prevLastNode.key, to: moduleNodes[0].key });
      var maxX = Math.max.apply(null, moduleNodes.map(function (n) { return n.x; }));
      runningX = maxX + NODE_W + GAP;
    });
    var height = allNodes.length ? Math.max.apply(null, allNodes.map(function (n) { return n.y; })) + NODE_H + PAD : 300;
    return { nodes: allNodes, edges: allEdges, mobileSteps: mobileSteps, width: runningX + PAD, height: height };
  }

  function wrapTwoLines(text, width) {
    width = width || 17;
    var words = text.split(" "), line1 = "", i = 0;
    while (i < words.length && (line1 + " " + words[i]).trim().length <= width) {
      line1 = (line1 + " " + words[i]).trim();
      i++;
    }
    var line2 = words.slice(i).join(" ");
    if (line2.length > width) line2 = line2.slice(0, width - 1) + "…";
    return [line1, line2];
  }

  function escHtml(s) {
    var div = document.createElement("div");
    div.textContent = String(s);
    return div.innerHTML;
  }

  function buildCanvasHTML(composite) {
    var boxes = composite.nodes.map(function (n) {
      var lines = wrapTwoLines(n.label, 17);
      var labelHtml = '<tspan x="' + (n.x + 48) + '" dy="0">' + escHtml(lines[0]) + "</tspan>";
      if (lines[1]) labelHtml += '<tspan x="' + (n.x + 48) + '" dy="16">' + escHtml(lines[1]) + "</tspan>";
      return '<g class="n8n-node ' + n.cls + '" data-name="' + escHtml(n.key) + '" transform="translate(' + n.x + "," + n.y + ')">' +
        '<rect width="' + NODE_W + '" height="' + NODE_H + '" rx="12"></rect>' +
        '<text x="16" y="27" class="n8n-node-icon">' + n.icon + "</text>" +
        '<text x="48" y="27" class="n8n-node-label">' + labelHtml + "</text></g>";
    }).join("");

    var byKey = {};
    composite.nodes.forEach(function (n) { byKey[n.key] = n; });
    var paths = composite.edges.map(function (e) {
      var s = byKey[e.from], d = byKey[e.to];
      if (!s || !d) return "";
      var sx = s.x + NODE_W, sy = s.y + NODE_H / 2;
      var dx = d.x, dy = d.y + NODE_H / 2;
      var mx = (sx + dx) / 2;
      var p = "M" + sx + "," + sy + " C" + mx + "," + sy + " " + mx + "," + dy + " " + dx + "," + dy;
      return '<path class="n8n-edge" d="' + p + '"></path>' +
        '<circle class="n8n-edge-pulse" r="4" data-from="' + escHtml(e.from) + '" data-to="' + escHtml(e.to) + '">' +
        '<animateMotion dur="3s" repeatCount="indefinite" path="' + p + '"></animateMotion></circle>';
    }).join("");

    var vb = "0 0 " + composite.width + " " + composite.height;
    var nodeRects = {};
    composite.nodes.forEach(function (n) { nodeRects[n.key] = { x: n.x, y: n.y, w: NODE_W, h: NODE_H }; });
    var walk = composite.nodes.map(function (n) { return n.key; });
    var canvasData = JSON.stringify({ viewBox: vb, nodes: nodeRects, walk: walk }).replace(/</g, "\\u003c");

    return '<div class="workflow-canvas">' +
      '<div class="workflow-canvas-toolbar">' +
      '<button type="button" class="workflow-canvas-start">▶ Tap to see how this runs</button>' +
      '<button type="button" class="workflow-canvas-replay" hidden>↻ Replay</button>' +
      '<div class="workflow-canvas-status" aria-live="polite"></div></div>' +
      '<div class="workflow-canvas-frame"><svg class="workflow-canvas-svg" viewBox="' + vb + '" preserveAspectRatio="xMidYMid meet">' +
      paths + boxes + "</svg></div>" +
      '<div class="workflow-canvas-live-caption"></div>' +
      '<script type="application/json" class="workflow-canvas-data">' + canvasData + "</" + "script>" +
      "</div>";
  }

  function buildRunnerHTML(composite) {
    var steps = composite.mobileSteps.map(function (n) {
      var stepCls = n.cls.replace("n8n-node-", "process-step-");
      return '<div class="process-step ' + stepCls + '">' +
        '<span class="process-step-dot"><span class="process-step-icon">' + n.icon + "</span></span>" +
        '<span class="process-step-body"><span class="process-step-label">' + escHtml(n.label) + "</span></span></div>";
    }).join("");
    return '<div class="process-runner">' +
      '<button type="button" class="process-runner-start">▶ Tap to see how this runs</button>' +
      '<div class="process-runner-status" aria-live="polite"></div>' +
      '<div class="process-steps">' + steps + "</div>" +
      '<button type="button" class="process-runner-replay" hidden>↻ Replay</button></div>';
  }

  function buildWorkflowDualHTML(composite, caption) {
    var cap = caption ? '<p class="process-runner-caption workflow-dual-caption">' + escHtml(caption) + "</p>" : "";
    return '<div class="workflow-dual">' +
      '<div class="workflow-mobile-view">' + buildRunnerHTML(composite) + "</div>" +
      '<div class="workflow-desktop-view">' + buildCanvasHTML(composite) + "</div>" + cap + "</div>";
  }

  function showResult() {
    wizard.hidden = true;
    var result = document.getElementById("cyb-result");
    result.hidden = false;
    result.scrollIntoView({ behavior: "smooth", block: "start" });

    var painObjs = state.pains.map(function (id) { return CYB.pains[id]; }).filter(Boolean);
    var modIds = [];
    painObjs.forEach(function (p) {
      p.modules.forEach(function (m) { if (modIds.indexOf(m) === -1) modIds.push(m); });
    });
    if (!modIds.length) return;

    var industryMeta = CYB.industries[state.industry];
    var industryName = industryMeta ? industryMeta.name : "your business";
    var scaleMeta = CYB.scale[state.scale];
    var scaleLabel = scaleMeta ? scaleMeta.label : state.scale;
    var deptLabel = state.dept ? CYB.depts[state.dept] : null;

    var summaryEl = document.getElementById("cyb-result-summary");
    if (summaryEl) {
      summaryEl.textContent = "Built around " + industryName + ", a " + scaleLabel + "-scale operation" +
        (deptLabel ? " (" + deptLabel + ")" : "") + " — based on what you told us is actually costing you money.";
    }

    Promise.all(modIds.map(fetchModule)).then(function (mods) {
      var composite = buildComposite(mods);
      var modNames = modIds.map(function (id) { return (CYB.modules[id] || {}).name || id; });
      var flowEl = document.getElementById("cyb-result-flow");
      flowEl.innerHTML = buildWorkflowDualHTML(composite, "Your automation — " + modNames.join(", "));
      flowEl.querySelectorAll(".process-runner").forEach(function (el) {
        if (window.AsliKaamProcessRunner) window.AsliKaamProcessRunner.init(el);
      });
      flowEl.querySelectorAll(".workflow-canvas").forEach(function (el) {
        if (window.AsliKaamWorkflowCanvas) window.AsliKaamWorkflowCanvas.init(el);
      });

      var painLabels = painObjs.map(function (p) { return p.label; }).join("; ");
      var msgLines = [
        "Hi! I checked my business on AsliKaam.",
        "Industry: " + industryName,
        "Size: " + scaleLabel + (deptLabel ? " (" + deptLabel + ")" : ""),
        "Currently using: " + (state.tools.length ? state.tools.join(", ") : "Nothing / fully manual"),
        "Biggest pain points: " + painLabels,
        "Please send me a free consultation on automating this.",
      ];
      var btn = document.getElementById("cyb-whatsapp-btn");
      if (btn) btn.href = "https://wa.me/" + CYB.whatsapp + "?text=" + encodeURIComponent(msgLines.join("\n"));
    });
  }
})();
