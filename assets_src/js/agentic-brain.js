/*
 * Agentic Use Cases page: rotates the "brain terminal" through all 15
 * industries. Each transition uses ShatterVisual on the WHOLE chat panel
 * (not just its text) — the earlier ParticleText approach only dissolved
 * the glyphs, leaving the bubble's own solid background sitting there
 * looking like a broken empty box. ShatterVisual hides the real element
 * entirely and draws tinted tiles in its place, so the panel genuinely
 * breaks apart and falls, then the next industry's conversation drops
 * back in with a bounce ("blocks falling, bouncing into place").
 * Tapping/clicking the terminal jumps to the next industry immediately.
 * Purely time-driven (rAF + setInterval), no GSAP dependency.
 */
(function () {
  var wrap = document.getElementById("brain-terminal");
  var dataEl = document.getElementById("brain-scenarios-data");
  if (!wrap || !dataEl) return;

  var scenarios;
  try { scenarios = JSON.parse(dataEl.textContent); } catch (e) { return; }
  if (!scenarios || scenarios.length < 2) return;

  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var iconEl = document.getElementById("brain-icon");
  var industryEl = document.getElementById("brain-industry");
  var customerEl = document.getElementById("brain-customer");
  var stepsEl = document.getElementById("brain-steps");
  var resolutionEl = document.getElementById("brain-resolution");

  var idx = 0;
  var running = true;
  var timer = null;
  var busy = false;

  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) { running = entries[0].isIntersecting; });
    io.observe(wrap);
  }

  function escapeHtml(s) {
    return s.replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function bubblesHtml(lines) {
    return lines.map(function (pair) {
      return '<div class="chat-bubble ' + pair[0] + '">' + escapeHtml(pair[1]) + "</div>";
    }).join("");
  }

  function renderSteps(steps) {
    stepsEl.innerHTML = "";
    steps.forEach(function (step, i) {
      var li = document.createElement("li");
      li.className = "brain-step";
      li.textContent = step;
      li.style.animationDelay = (i * 0.18) + "s";
      stepsEl.appendChild(li);
    });
  }

  function applyScenario(s) {
    iconEl.textContent = s.icon;
    industryEl.textContent = s.industry;
    customerEl.innerHTML = bubblesHtml(s.customer);
    resolutionEl.innerHTML = bubblesHtml(s.resolution);
    renderSteps(s.thinking);
  }

  // ShatterVisual inserts a fresh canvas next to the element on every
  // construction — since this widget rebuilds panels indefinitely (not
  // once per page load, like Home's), the old canvas has to be removed
  // each time or they'd pile up in the DOM forever.
  function rebuildShatter(el) {
    var old = el.nextSibling;
    if (old && old.classList && old.classList.contains("shatter-canvas")) old.remove();
    return new window.ShatterVisual(el, { color: el.getAttribute("data-shatter") });
  }

  function animate(duration, onUpdate, onDone) {
    var start = performance.now();
    function frame(now) {
      var t = Math.min(1, (now - start) / duration);
      onUpdate(t);
      if (t < 1) requestAnimationFrame(frame);
      else if (onDone) onDone();
    }
    requestAnimationFrame(frame);
  }

  // Classic "ball dropping and settling" curve — bounded to [0, 1], so it
  // drives dispersion (1 = scattered, 0 = assembled) straight into
  // ShatterVisual.setProgress without any risk of an out-of-range value.
  function easeOutBounce(x) {
    var n1 = 7.5625, d1 = 2.75;
    if (x < 1 / d1) return n1 * x * x;
    if (x < 2 / d1) { x -= 1.5 / d1; return n1 * x * x + 0.75; }
    if (x < 2.5 / d1) { x -= 2.25 / d1; return n1 * x * x + 0.9375; }
    x -= 2.625 / d1;
    return n1 * x * x + 0.984375;
  }

  function swap() {
    if (busy) return;
    busy = true;
    idx = (idx + 1) % scenarios.length;
    var next = scenarios[idx];

    if (reduceMotion || !window.ShatterVisual) {
      applyScenario(next);
      busy = false;
      return;
    }

    var custShatter = rebuildShatter(customerEl);
    var resShatter = rebuildShatter(resolutionEl);
    stepsEl.classList.add("is-fading");

    // Exit: shatter and fall away.
    animate(320, function (t) {
      custShatter.setProgress(t);
      resShatter.setProgress(t);
    }, function () {
      applyScenario(next);
      stepsEl.classList.remove("is-fading");

      var custShatter2 = rebuildShatter(customerEl);
      var resShatter2 = rebuildShatter(resolutionEl);
      custShatter2.setProgress(1);
      resShatter2.setProgress(1);

      // Entrance: bounce into place.
      animate(600, function (t) {
        var dispersion = 1 - easeOutBounce(t);
        custShatter2.setProgress(dispersion);
        resShatter2.setProgress(dispersion);
      }, function () { busy = false; });
    });
  }

  function manualAdvance() {
    swap();
    clearInterval(timer);
    timer = setInterval(function () { if (running) swap(); }, 3500);
  }

  wrap.addEventListener("click", manualAdvance);
  wrap.addEventListener("keydown", function (e) {
    if (e.key === "Enter" || e.key === " ") { e.preventDefault(); manualAdvance(); }
  });

  timer = setInterval(function () { if (running) swap(); }, 3500);
})();
