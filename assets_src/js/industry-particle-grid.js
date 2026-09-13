/*
 * Agentic Use Cases page: the 15-industry grid sits as scattered ambient
 * particles at rest and "snaps into focus" — assembles into its crisp
 * icon + name — on hover, focus, or touch. Visualizes one adaptive engine
 * reshaping itself per industry, not 15 separate fixed bots. Reuses
 * ParticleText exactly as-is, just driven by pointer events instead of
 * scroll position.
 */
(function () {
  var tiles = document.querySelectorAll(".ind-particle-tile");
  if (!tiles.length || !window.ParticleText) return;
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduceMotion) return; // labels are already real, readable DOM text

  function animate(duration, onUpdate) {
    var start = performance.now();
    function frame(now) {
      var t = Math.min(1, (now - start) / duration);
      onUpdate(t);
      if (t < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  // ParticleText's own alpha curve fades to fully invisible at t=1 (it
  // was built for "dissolve away to nothing"), so a resting scatter needs
  // a value short of 1 to actually stay visible as a loose, glowing cloud
  // rather than disappearing entirely.
  var REST_SCATTER = 0.62;

  Array.prototype.forEach.call(tiles, function (tile) {
    var label = tile.querySelector(".ind-particle-label");
    if (!label) return;
    var pt = new window.ParticleText(label, { stride: 2 });
    pt.setProgress(REST_SCATTER);
    var current = REST_SCATTER;

    function go(target) {
      var from = current;
      animate(450, function (t) {
        current = from + (target - from) * t;
        pt.setProgress(current);
      });
    }

    tile.addEventListener("mouseenter", function () { go(0); });
    tile.addEventListener("mouseleave", function () { go(REST_SCATTER); });
    tile.addEventListener("focus", function () { go(0); });
    tile.addEventListener("blur", function () { go(REST_SCATTER); });
    tile.addEventListener("touchstart", function () { go(0); }, { passive: true });
  });
})();
