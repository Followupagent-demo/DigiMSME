/*
 * Cinematic scroll engine — data-agnostic, works on any .cinematic-wrap
 * containing a .cinematic-pin with one or more .scene children.
 *
 * Baseline (always on, zero dependencies): scenes fade/slide into view
 * via IntersectionObserver as the page scrolls normally.
 *
 * Enhancement (only after gsap:ready fires): pins the section and
 * scrubs between scenes on scroll. Uses GSAP's own ScrollTrigger pin —
 * never combined with CSS position:sticky, to avoid double-pinning.
 */
(function () {
  function initBaseline() {
    var scenes = document.querySelectorAll(".scene");
    if (!("IntersectionObserver" in window) || !scenes.length) {
      scenes.forEach(function (s) { s.classList.add("is-visible"); });
      return;
    }
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) entry.target.classList.add("is-visible");
        });
      },
      { threshold: 0.2 }
    );
    scenes.forEach(function (s) { io.observe(s); });
  }

  function enhanceWithGsap() {
    var wraps = document.querySelectorAll(".cinematic-wrap");
    wraps.forEach(function (wrap) {
      var pinEl = wrap.querySelector(".cinematic-pin");
      var scenes = Array.prototype.slice.call(pinEl.querySelectorAll(".scene"));
      if (scenes.length < 2) return; // nothing to scrub between

      var dots = Array.prototype.slice.call(wrap.querySelectorAll(".scene-dots .dot"));
      wrap.classList.add("js-pin-active");
      scenes.forEach(function (s) { s.classList.remove("is-visible"); });
      scenes[0].classList.add("is-active");
      if (dots[0]) dots[0].classList.add("is-active");

      ScrollTrigger.create({
        trigger: wrap,
        start: "top top",
        end: "+=" + scenes.length * 100 + "%",
        pin: pinEl,
        scrub: true,
        onUpdate: function (self) {
          var idx = Math.min(scenes.length - 1, Math.floor(self.progress * scenes.length));
          scenes.forEach(function (s, i) { s.classList.toggle("is-active", i === idx); });
          dots.forEach(function (d, i) { d.classList.toggle("is-active", i === idx); });
        },
      });
    });
    ScrollTrigger.refresh();
  }

  document.addEventListener("DOMContentLoaded", initBaseline);
  document.addEventListener("gsap:ready", enhanceWithGsap);
})();
