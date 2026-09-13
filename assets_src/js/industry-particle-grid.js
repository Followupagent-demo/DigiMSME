/*
 * Agentic Use Cases page: the 15-industry grid is fully readable at rest
 * (a visitor shouldn't have to hover every tile just to find their own
 * industry) — hovering triggers a quick scatter-and-reassemble pulse as a
 * decorative flourish on top of a label that's already legible. Reuses
 * ParticleText exactly as-is, just driven by pointer events instead of
 * scroll position.
 */
(function () {
  var tiles = document.querySelectorAll(".ind-particle-tile");
  if (!tiles.length || !window.ParticleText) return;
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduceMotion) return; // labels are already real, readable DOM text

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

  Array.prototype.forEach.call(tiles, function (tile) {
    var label = tile.querySelector(".ind-particle-label");
    if (!label) return;
    var pt = new window.ParticleText(label, { stride: 2 });
    var pulsing = false;

    function pulse() {
      if (pulsing) return;
      pulsing = true;
      animate(260, function (t) { pt.setProgress(t); }, function () {
        animate(380, function (t) { pt.setProgress(1 - t); }, function () { pulsing = false; });
      });
    }

    tile.addEventListener("mouseenter", pulse);
    tile.addEventListener("focus", pulse);
    tile.addEventListener("touchstart", pulse, { passive: true });
  });
})();
