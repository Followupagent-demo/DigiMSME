// Desktop-only companion to process-runner.js: plays the full n8n-style
// graph in .workflow-canvas by animating the SVG viewBox to zoom into
// each node in turn (a virtual camera), pulsing the edge just crossed,
// then pulling back out to show the whole run lit up. No-op if absent.
(function () {
  function parseVB(s) { return s.split(" ").map(Number); }
  function lerpVB(a, b, t) {
    var pa = parseVB(a), pb = parseVB(b), out = [];
    for (var i = 0; i < 4; i++) out.push(pa[i] + (pb[i] - pa[i]) * t);
    return out.join(" ");
  }
  function ease(t) { return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t; }

  function initCanvas(root) {
    var svg = root.querySelector(".workflow-canvas-svg");
    var dataEl = root.querySelector(".workflow-canvas-data");
    var startBtn = root.querySelector(".workflow-canvas-start");
    var replayBtn = root.querySelector(".workflow-canvas-replay");
    var statusEl = root.querySelector(".workflow-canvas-status");
    var captionEl = root.querySelector(".workflow-canvas-live-caption");
    if (!svg || !dataEl) return;

    var data;
    try { data = JSON.parse(dataEl.textContent); } catch (e) { return; }
    var full = data.viewBox;
    var nodes = data.nodes || {};
    var walk = data.walk || [];
    if (!walk.length) return;

    var nodeEls = Array.prototype.slice.call(root.querySelectorAll(".n8n-node"));
    var edgeEls = Array.prototype.slice.call(root.querySelectorAll(".n8n-edge-pulse"));
    function findNode(name) { return nodeEls.filter(function (g) { return g.dataset.name === name; })[0]; }
    function findEdge(from, to) {
      return edgeEls.filter(function (c) { return c.dataset.from === from && c.dataset.to === to; })[0];
    }

    var PAD = 90;
    function nodeViewBox(name) {
      var r = nodes[name];
      if (!r) return full;
      var cx = r.x + r.w / 2, cy = r.y + r.h / 2;
      var w = r.w + PAD * 2.4, h = r.h + PAD * 9;
      return [cx - w / 2, cy - h / 2, w, h].join(" ");
    }

    var raf = null;
    function animateTo(targetVB, duration, cb) {
      var startVB = svg.getAttribute("viewBox") || full;
      var t0 = performance.now();
      if (raf) cancelAnimationFrame(raf);
      function frame(now) {
        var t = Math.min(1, (now - t0) / duration);
        svg.setAttribute("viewBox", lerpVB(startVB, targetVB, ease(t)));
        if (t < 1) { raf = requestAnimationFrame(frame); }
        else { raf = null; if (cb) cb(); }
      }
      raf = requestAnimationFrame(frame);
    }

    function clearActive() {
      nodeEls.forEach(function (g) { g.classList.remove("is-active"); });
      edgeEls.forEach(function (c) { c.classList.remove("is-live"); });
    }

    var playing = false;
    function step(i) {
      if (i >= walk.length) {
        animateTo(full, 900, function () {
          playing = false;
          root.classList.remove("is-playing");
          root.classList.add("is-done");
          if (replayBtn) replayBtn.hidden = false;
          if (statusEl) statusEl.textContent = "✓ That's the full flow, start to finish.";
          if (captionEl) captionEl.textContent = "The complete automation — " + walk.length + " steps, one continuous run.";
        });
        return;
      }
      var name = walk[i];
      var g = findNode(name);
      if (g) g.classList.add("is-active");
      if (i > 0) {
        var edge = findEdge(walk[i - 1], name);
        if (edge) {
          edge.classList.add("is-live");
          var motion = edge.querySelector("animateMotion");
          if (motion && motion.beginElement) { try { motion.beginElement(); } catch (e) {} }
        }
      }
      if (statusEl) statusEl.textContent = "● Step " + (i + 1) + " of " + walk.length;
      if (captionEl) captionEl.textContent = name;
      animateTo(nodeViewBox(name), 700, function () {
        setTimeout(function () { step(i + 1); }, 500);
      });
    }

    function play() {
      if (playing) return;
      playing = true;
      clearActive();
      if (startBtn) startBtn.hidden = true;
      if (replayBtn) replayBtn.hidden = true;
      root.classList.remove("is-done");
      root.classList.add("is-playing");
      svg.setAttribute("viewBox", full);
      step(0);
    }

    if (startBtn) startBtn.addEventListener("click", play);
    if (replayBtn) replayBtn.addEventListener("click", play);
  }

  document.querySelectorAll(".workflow-canvas").forEach(initCanvas);
})();
