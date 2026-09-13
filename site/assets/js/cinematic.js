/*
 * Cinematic scroll engine — data-agnostic, works on any .cinematic-wrap
 * containing a .cinematic-pin with one or more .scene children.
 *
 * Baseline (always on, zero dependencies): scenes fade/slide into view
 * via IntersectionObserver as the page scrolls normally.
 *
 * Enhancement (only after gsap:ready fires): pins the section and, as the
 * user scrolls, drives a continuous per-scene "dispersion" value (0 =
 * fully assembled/readable, 1 = fully dissolved) purely as a function of
 * scroll position. Each scene's heading is rendered as canvas particles
 * (particle-text.js) that scatter/reassemble with that value; the body
 * copy on "red" (loss) scenes falls into place phrase by phrase, turning
 * red as it lands. Because it's a pure function of scroll position, not a
 * one-shot animation, scrolling back up reverses it exactly.
 *
 * Uses GSAP's own ScrollTrigger pin — never combined with CSS
 * position:sticky, to avoid double-pinning. Canvas/particle work only
 * happens here, after GSAP has actually loaded — a page with no JS or a
 * blocked CDN never sees anything but plain, fully-visible text.
 */
(function () {
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var isNarrow = window.innerWidth < 640;
  var MUTED_RGB = [154, 164, 175]; // --muted
  var DANGER_RGB = [255, 107, 107]; // --danger

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

  function lerpColor(a, b, t) {
    return "rgb(" + Math.round(a[0] + (b[0] - a[0]) * t) + "," +
      Math.round(a[1] + (b[1] - a[1]) * t) + "," +
      Math.round(a[2] + (b[2] - a[2]) * t) + ")";
  }

  // Splits a paragraph into sentence-ish phrase spans, kept for scenes
  // whose "loss" copy should fall into place line by line instead of
  // fading in as one block.
  function splitIntoPhrases(el) {
    if (el.dataset.phraseSplit) return Array.prototype.slice.call(el.querySelectorAll(".ph"));
    el.dataset.phraseSplit = "1";
    var text = el.textContent;
    var parts = text.match(/[^.!?]+[.!?]*\s*/g) || [text];
    var frag = document.createDocumentFragment();
    var spans = [];
    parts.forEach(function (part) {
      if (!part.trim()) { frag.appendChild(document.createTextNode(part)); return; }
      var span = document.createElement("span");
      span.className = "ph";
      span.textContent = part;
      spans.push(span);
      frag.appendChild(span);
    });
    el.innerHTML = "";
    el.appendChild(frag);
    return spans;
  }

  function setPhraseProgress(spans, assembleT) {
    var n = spans.length;
    spans.forEach(function (span, i) {
      var start = (i / n) * 0.5;
      var span_range = 1 - start || 1;
      var local = Math.max(0, Math.min(1, (assembleT - start) / span_range));
      var eased = 1 - Math.pow(1 - local, 3);
      gsap.set(span, { y: (1 - eased) * -26, opacity: eased, color: lerpColor(MUTED_RGB, DANGER_RGB, eased) });
    });
  }

  function enhanceWithGsap() {
    var wraps = document.querySelectorAll(".cinematic-wrap");
    wraps.forEach(function (wrap) {
      var pinEl = wrap.querySelector(".cinematic-pin");
      var scenes = Array.prototype.slice.call(pinEl.querySelectorAll(".scene"));
      var n = scenes.length;
      if (n < 2) return; // nothing to scrub between

      var dots = Array.prototype.slice.call(wrap.querySelectorAll(".scene-dots .dot"));
      wrap.classList.add("js-pin-active");
      scenes.forEach(function (s) { s.classList.remove("is-visible"); });

      var stride = isNarrow ? 5 : 3;
      var state = scenes.map(function (scene) {
        var h2 = scene.querySelector(".scene-copy h2");
        var eyebrow = scene.querySelector(".scene-copy .eyebrow");
        var pEl = scene.querySelector(".scene-copy p");
        var isRed = scene.getAttribute("data-accent") === "red";
        var isGreen = scene.getAttribute("data-accent") === "green";
        // A scene using the shatter-fall effect (data-visual-fx="shatter")
        // opts out of the default green X-ray clip-path reveal — the two
        // effects on the same panel would fight each other.
        var visualEl = (isGreen && scene.getAttribute("data-visual-fx") !== "shatter") ? scene.querySelector(".scene-visual") : null;
        var ptxt = (!reduceMotion && h2 && window.ParticleText) ? new window.ParticleText(h2, { stride: stride }) : null;
        var phrases = (!reduceMotion && isRed && pEl) ? splitIntoPhrases(pEl) : null;

        // Any element inside this scene opting in via data-dissolve gets
        // the same canvas particle treatment as the heading — e.g. an
        // unanswered chat bubble "evaporating" (data-dissolve-drift="up")
        // or a skipped listing's name scattering away like the heading
        // does. Reuses the same engine, just applied more places.
        var extraDissolve = [];
        if (!reduceMotion && window.ParticleText) {
          Array.prototype.forEach.call(scene.querySelectorAll("[data-dissolve]"), function (el) {
            extraDissolve.push(new window.ParticleText(el, { stride: stride, drift: el.getAttribute("data-dissolve-drift") || "down" }));
          });
        }

        var currencyParticles = [];
        if (!reduceMotion && window.CurrencyParticles) {
          Array.prototype.forEach.call(scene.querySelectorAll("[data-currency-particles]"), function (el) {
            currencyParticles.push(new window.CurrencyParticles(el));
          });
        }

        var shatter = [];
        if (!reduceMotion && window.ShatterVisual) {
          Array.prototype.forEach.call(scene.querySelectorAll("[data-shatter]"), function (el) {
            shatter.push(new window.ShatterVisual(el, { color: el.getAttribute("data-shatter") }));
          });
        }

        return { scene: scene, h2: h2, ptxt: ptxt, eyebrow: eyebrow, pEl: pEl, phrases: phrases, extraDissolve: extraDissolve, currencyParticles: currencyParticles, shatter: shatter, visualEl: visualEl };
      });

      var HALF_WIDTH = 0.2; // fraction of one scene's slot spent transitioning across each boundary

      function band(progressFrac, boundary) {
        return Math.max(0, Math.min(1, (progressFrac - (boundary - HALF_WIDTH)) / (2 * HALF_WIDTH)));
      }

      function apply(progressFrac) {
        var activeIdx = Math.max(0, Math.min(n - 1, Math.round(progressFrac)));
        state.forEach(function (st, i) {
          var dispersion = 0;
          if (i > 0) dispersion = Math.max(dispersion, 1 - band(progressFrac, i));
          if (i < n - 1) dispersion = Math.max(dispersion, band(progressFrac, i + 1));

          if (reduceMotion) {
            gsap.set(st.scene, { opacity: i === activeIdx ? 1 : 0 });
            return;
          }

          gsap.set(st.scene, { opacity: 1 - dispersion });
          st.scene.style.pointerEvents = dispersion < 0.4 ? "auto" : "none";

          if (st.ptxt) st.ptxt.setProgress(dispersion);
          else if (st.h2) gsap.set(st.h2, { opacity: 1 - dispersion });

          if (st.eyebrow) gsap.set(st.eyebrow, { opacity: 1 - dispersion });

          if (st.phrases) setPhraseProgress(st.phrases, 1 - dispersion);
          else if (st.pEl) gsap.set(st.pEl, { opacity: 1 - dispersion });

          st.extraDissolve.forEach(function (pt) { pt.setProgress(dispersion); });
          st.currencyParticles.forEach(function (cp) { cp.setProgress(dispersion); });
          st.shatter.forEach(function (sv) { sv.setProgress(dispersion); });

          if (st.visualEl) st.visualEl.style.setProperty("--reveal", 1 - dispersion);
        });
        dots.forEach(function (d, i) { d.classList.toggle("is-active", i === activeIdx); });
      }

      apply(0);

      ScrollTrigger.create({
        trigger: wrap,
        start: "top top",
        end: "+=" + n * 100 + "%",
        pin: pinEl,
        scrub: true,
        onUpdate: function (self) { apply(self.progress * n); },
      });
    });
    ScrollTrigger.refresh();
  }

  document.addEventListener("DOMContentLoaded", initBaseline);
  document.addEventListener("gsap:ready", enhanceWithGsap);
})();
