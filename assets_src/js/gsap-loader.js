/*
 * Loads GSAP + ScrollTrigger from a CDN with a hard timeout.
 * If either script fails to load, errors, or simply isn't ready in time,
 * we fall back to the plain stacked/non-pinned layout — the page already
 * works with zero JS, this only decides whether to *enhance* it.
 * Never assume CDN success: gsap:ready only fires once both libs are
 * actually confirmed present on window.
 */
(function () {
  var GSAP_URL = "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js";
  var ST_URL = "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js";
  var TIMEOUT_MS = 3000;
  var settled = false;

  function settle(ok) {
    if (settled) return;
    settled = true;
    if (ok && window.gsap && window.ScrollTrigger) {
      document.documentElement.classList.remove("no-gsap");
      document.dispatchEvent(new CustomEvent("gsap:ready"));
    } else {
      document.documentElement.classList.add("no-gsap");
      document.dispatchEvent(new CustomEvent("gsap:unavailable"));
    }
  }

  function loadScript(src, onDone) {
    var s = document.createElement("script");
    s.src = src;
    s.async = true;
    s.onload = function () { onDone(true); };
    s.onerror = function () { onDone(false); };
    document.head.appendChild(s);
  }

  // Assume the fallback until proven otherwise.
  document.documentElement.classList.add("no-gsap");

  var timeoutId = setTimeout(function () { settle(false); }, TIMEOUT_MS);

  loadScript(GSAP_URL, function (gsapOk) {
    if (!gsapOk) { clearTimeout(timeoutId); settle(false); return; }
    loadScript(ST_URL, function (stOk) {
      clearTimeout(timeoutId);
      if (stOk && window.gsap && window.ScrollTrigger) {
        window.gsap.registerPlugin(window.ScrollTrigger);
        settle(true);
      } else {
        settle(false);
      }
    });
  });
})();
