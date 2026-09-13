/*
 * Industries page: balloons carrying each industry's name+icon drift down
 * from the top of a contained field. Click one and it freezes, inflates
 * to fill the screen, bursts, then takes you to that industry's page —
 * the real static grid below still exists and works with zero JS, this
 * is purely an added, progressively-enhanced way in.
 */
(function () {
  var field = document.getElementById("balloon-field");
  if (!field) return;
  var balloons = Array.prototype.slice.call(field.querySelectorAll(".balloon"));
  if (!balloons.length) return;

  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  field.classList.add("is-active");
  field.removeAttribute("aria-hidden");

  if (reduceMotion) {
    // No falling, no inflate-and-burst — just a plain clickable grid of
    // balloons that behave like ordinary links.
    balloons.forEach(function (b) {
      b.addEventListener("click", function () { window.location.href = b.dataset.href; });
    });
    return;
  }

  var fieldW = field.clientWidth;
  balloons.forEach(function (b) {
    var left = Math.random() * Math.max(0, fieldW - 108);
    var duration = 12 + Math.random() * 9;
    var delay = -(Math.random() * duration);
    b.style.left = left + "px";
    b.style.animationDuration = duration + "s";
    b.style.animationDelay = delay + "s";
  });

  var busy = false;

  balloons.forEach(function (b) {
    b.addEventListener("click", function () {
      if (busy) return;
      busy = true;

      var rect = b.getBoundingClientRect();
      b.style.left = rect.left + "px";
      b.style.top = rect.top + "px";
      b.style.width = rect.width + "px";
      b.style.height = rect.height + "px";
      b.style.animation = "none";
      b.style.margin = "0";

      // Force a reflow so the frozen position above is committed before
      // the inflate transition below starts animating from it.
      void b.offsetHeight;

      b.classList.add("is-inflating");
      b.style.left = "0px";
      b.style.top = "0px";
      b.style.width = "100vw";
      b.style.height = "100vh";
      b.style.borderRadius = "0";

      setTimeout(function () {
        b.classList.add("is-bursting");
        setTimeout(function () { window.location.href = b.dataset.href; }, 240);
      }, 600);
    });
  });
})();
