// Home's search-results scenes cycle through several industries so no
// single visitor sees only a field that isn't theirs. Both the "broken"
// and "fixed" scenes share one index, so scrolling between them always
// shows the same industry mid-story.
(function () {
  var slides = document.querySelectorAll(".rotation-slide");
  if (!slides.length) return;
  var max = 0;
  slides.forEach(function (s) { max = Math.max(max, parseInt(s.dataset.rot, 10)); });
  var current = 0;

  setInterval(function () {
    current = (current + 1) % (max + 1);
    slides.forEach(function (s) {
      s.hidden = parseInt(s.dataset.rot, 10) !== current;
    });
  }, 2200);
})();
