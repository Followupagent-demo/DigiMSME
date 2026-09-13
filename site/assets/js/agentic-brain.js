/*
 * Agentic Use Cases page: rotates the "brain terminal" through a handful
 * of industry scenarios, dissolving and reassembling the chat text with
 * ParticleText (the same engine Home's cinematic scroll uses) between
 * each so it visibly morphs instead of just cutting. Purely time-driven
 * (rAF + setInterval), no GSAP dependency — this widget isn't
 * scroll-scrubbed, it just needs to keep animating on its own.
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
  var replyEl = document.getElementById("brain-reply");

  var idx = 0;
  var running = true;
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) { running = entries[0].isIntersecting; });
    io.observe(wrap);
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

  function applyScenario(s) {
    iconEl.textContent = s.icon;
    industryEl.textContent = s.industry;
    customerEl.textContent = s.customer;
    replyEl.textContent = s.reply;
    renderSteps(s.thinking);
  }

  function swap() {
    idx = (idx + 1) % scenarios.length;
    var next = scenarios[idx];

    if (reduceMotion || !window.ParticleText) {
      applyScenario(next);
      return;
    }

    var custPt = new window.ParticleText(customerEl, { stride: 2 });
    var replyPt = new window.ParticleText(replyEl, { stride: 2 });
    stepsEl.classList.add("is-fading");

    animate(380, function (t) { custPt.setProgress(t); replyPt.setProgress(t); }, function () {
      applyScenario(next);
      stepsEl.classList.remove("is-fading");

      var custPt2 = new window.ParticleText(customerEl, { stride: 2 });
      var replyPt2 = new window.ParticleText(replyEl, { stride: 2 });
      custPt2.setProgress(1);
      replyPt2.setProgress(1);
      animate(420, function (t) { custPt2.setProgress(1 - t); replyPt2.setProgress(1 - t); });
    });
  }

  setInterval(function () { if (running) swap(); }, 3500);
})();
