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
 * As each scene changes, its copy (eyebrow/title/body) dissolves out
 * word-by-word while the next scene's copy assembles in — word
 * splitting only happens here, so a page with no JS or a blocked CDN
 * never sees anything but plain, fully-visible text.
 */
(function () {
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var isNarrow = window.innerWidth < 640;

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

  // Wraps every word of a scene's copy in its own <span class="wd">,
  // preserving whitespace as plain text nodes — run once per scene,
  // only when GSAP is actually driving the transition.
  function splitIntoWords(scene) {
    if (scene.dataset.split) return;
    scene.dataset.split = "1";
    var targets = scene.querySelectorAll(".scene-copy .eyebrow, .scene-copy h2, .scene-copy p");
    targets.forEach(function (el) {
      var text = el.textContent;
      var frag = document.createDocumentFragment();
      text.split(/(\s+)/).forEach(function (chunk) {
        if (/^\s+$/.test(chunk)) {
          frag.appendChild(document.createTextNode(chunk));
        } else if (chunk.length) {
          var span = document.createElement("span");
          span.className = "wd";
          span.textContent = chunk;
          frag.appendChild(span);
        }
      });
      el.innerHTML = "";
      el.appendChild(frag);
    });
  }

  function getWords(scene) {
    return Array.prototype.slice.call(scene.querySelectorAll(".scene-copy .wd"));
  }

  function enhanceWithGsap() {
    var wraps = document.querySelectorAll(".cinematic-wrap");
    wraps.forEach(function (wrap) {
      var pinEl = wrap.querySelector(".cinematic-pin");
      var scenes = Array.prototype.slice.call(pinEl.querySelectorAll(".scene"));
      if (scenes.length < 2) return; // nothing to scrub between

      var dots = Array.prototype.slice.call(wrap.querySelectorAll(".scene-dots .dot"));
      wrap.classList.add("js-pin-active");
      scenes.forEach(splitIntoWords);
      scenes.forEach(function (s) { s.classList.remove("is-visible"); });

      var currentIdx = -1;

      function showScene(scene, instant) {
        scene.classList.add("is-active");
        var words = getWords(scene);
        if (reduceMotion || instant) {
          gsap.set(words, { opacity: 1, y: 0, filter: "none" });
          return;
        }
        gsap.fromTo(words,
          { opacity: 0, y: isNarrow ? 10 : 18, filter: isNarrow ? "none" : "blur(6px)" },
          { opacity: 1, y: 0, filter: "none", duration: 0.5, stagger: 0.012, ease: "power2.out", overwrite: true });
      }

      function hideScene(scene) {
        var words = getWords(scene);
        if (!reduceMotion) {
          gsap.to(words, {
            opacity: 0, y: isNarrow ? -8 : -14, filter: isNarrow ? "none" : "blur(5px)",
            duration: 0.35, stagger: 0.008, ease: "power1.in", overwrite: true,
          });
        }
        scene.classList.remove("is-active");
      }

      showScene(scenes[0], true);
      currentIdx = 0;
      if (dots[0]) dots[0].classList.add("is-active");

      ScrollTrigger.create({
        trigger: wrap,
        start: "top top",
        end: "+=" + scenes.length * 100 + "%",
        pin: pinEl,
        scrub: true,
        onUpdate: function (self) {
          var idx = Math.min(scenes.length - 1, Math.floor(self.progress * scenes.length));
          if (idx !== currentIdx) {
            hideScene(scenes[currentIdx]);
            showScene(scenes[idx], false);
            currentIdx = idx;
          }
          dots.forEach(function (d, i) { d.classList.toggle("is-active", i === idx); });
        },
      });
    });
    ScrollTrigger.refresh();
  }

  document.addEventListener("DOMContentLoaded", initBaseline);
  document.addEventListener("gsap:ready", enhanceWithGsap);
})();
