// Tap-to-play walkthrough for .process-runner widgets (real n8n workflow,
// rendered as a vertical step list). No-op on pages without one.
(function () {
  function initRunner(root) {
    var startBtn = root.querySelector(".process-runner-start");
    var replayBtn = root.querySelector(".process-runner-replay");
    var statusEl = root.querySelector(".process-runner-status");
    var steps = Array.prototype.slice.call(root.querySelectorAll(".process-step"));
    if (!steps.length) return;
    var playing = false;

    function play() {
      if (playing) return;
      playing = true;
      steps.forEach(function (s) { s.classList.remove("is-active"); });
      root.classList.remove("is-done");
      root.classList.add("is-playing");
      if (startBtn) startBtn.hidden = true;
      if (replayBtn) replayBtn.hidden = true;
      if (statusEl) statusEl.textContent = "● Running the automation…";

      var n = steps.length;
      var stepDelay = Math.max(300, Math.min(600, Math.round(3200 / n)));
      steps.forEach(function (step, i) {
        setTimeout(function () {
          step.classList.add("is-active");
          if (i === n - 1) {
            setTimeout(function () {
              playing = false;
              root.classList.remove("is-playing");
              root.classList.add("is-done");
              if (replayBtn) replayBtn.hidden = false;
              if (statusEl) statusEl.textContent = "✓ That's the full flow, start to finish.";
            }, 450);
          }
        }, i * stepDelay);
      });
    }

    if (startBtn) startBtn.addEventListener("click", play);
    if (replayBtn) replayBtn.addEventListener("click", play);
  }

  document.querySelectorAll(".process-runner").forEach(initRunner);
  // Exposed so pages that build a .process-runner after load (e.g. the
  // Check Your Business wizard's dynamically-assembled flow) can wire it
  // up without duplicating this logic.
  window.AsliKaamProcessRunner = { init: initRunner };
})();
