/*
 * Shared "pick one, everything falls away" navigation transition — used
 * on Home's industry picker grid and the Agentic Use Cases particle
 * industry grid. On click: every card in the group (the clicked one
 * included) falls intact, like real gravity, to the bottom of the
 * screen and piles up there — then a burst of fine green pixels
 * destroys the pile, and the page navigates to the clicked card's real
 * href. No-op under prefers-reduced-motion — the link just navigates
 * normally.
 */
(function () {
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

  var FALL_DURATION = 550;
  var MAX_STAGGER = 180;

  function dropAll(items) {
    var vh = window.innerHeight;
    // Read every rect before freezing any element — freezing the first
    // item would remove it from flow and shift the rects of the ones
    // still measured after it.
    var rects = items.map(function (el) { return el.getBoundingClientRect(); });
    items.forEach(function (el, i) {
      var rect = rects[i];
      el.style.position = "fixed";
      el.style.left = rect.left + "px";
      el.style.top = rect.top + "px";
      el.style.width = rect.width + "px";
      el.style.height = rect.height + "px";
      el.style.margin = "0";
      el.style.zIndex = "150";
      el.style.transition = "none";
    });
    // Force layout so the frozen start position above is committed
    // before the transition target below starts animating from it.
    void items[0].offsetHeight;

    items.forEach(function (el) {
      var delay = Math.random() * MAX_STAGGER;
      el.style.transitionProperty = "top";
      el.style.transitionDuration = FALL_DURATION + "ms";
      el.style.transitionDelay = delay + "ms";
      el.style.transitionTimingFunction = "cubic-bezier(.55,0,1,.45)"; // accelerating, like gravity
      el.style.top = (vh + 60) + "px";
    });
  }

  function burstAtBottom(color, onDone) {
    var vw = window.innerWidth, vh = window.innerHeight;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);

    var canvas = document.createElement("canvas");
    canvas.style.position = "fixed";
    canvas.style.left = "0"; canvas.style.top = "0";
    canvas.style.width = vw + "px"; canvas.style.height = vh + "px";
    canvas.style.zIndex = "999"; canvas.style.pointerEvents = "none";
    canvas.width = Math.ceil(vw * dpr);
    canvas.height = Math.ceil(vh * dpr);
    document.body.appendChild(canvas);
    var ctx = canvas.getContext("2d");
    ctx.scale(dpr, dpr);

    var particles = [];
    for (var i = 0; i < 320; i++) {
      particles.push({
        x0: Math.random() * vw,
        y0: vh - Math.random() * 50,
        vx: (Math.random() - 0.5) * vw * 0.9,
        vy: -(vh * 0.5 + Math.random() * vh * 0.9),
        size: 2 + Math.random() * 3,
        jitter: Math.random(),
      });
    }

    animate(520, function (t) {
      ctx.clearRect(0, 0, vw, vh);
      ctx.fillStyle = color;
      particles.forEach(function (p) {
        var localT = Math.min(1, t * (0.8 + p.jitter * 0.5));
        var eased = 1 - Math.pow(1 - localT, 2);
        var x = p.x0 + p.vx * eased;
        var y = p.y0 + p.vy * eased;
        ctx.globalAlpha = Math.max(0, 1 - localT * 0.7);
        ctx.fillRect(x, y, p.size, p.size);
      });
      ctx.globalAlpha = 1;
    }, function () {
      canvas.remove();
      onDone();
    });
  }

  function wire(containerSelector, itemSelector, opts) {
    opts = opts || {};
    var burstColor = opts.burstColor || "#25d366";
    var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    Array.prototype.forEach.call(document.querySelectorAll(containerSelector), function (container) {
      var items = Array.prototype.slice.call(container.querySelectorAll(itemSelector));
      if (!items.length || reduceMotion) return;

      items.forEach(function (item) {
        item.addEventListener("click", function (e) {
          if (container.dataset.busting) { e.preventDefault(); return; }
          var href = item.getAttribute("href");
          if (!href) return;
          e.preventDefault();
          container.dataset.busting = "1";

          dropAll(items);
          setTimeout(function () {
            items.forEach(function (el) { el.style.visibility = "hidden"; });
            burstAtBottom(burstColor, function () {
              window.location.href = href;
            });
          }, FALL_DURATION + MAX_STAGGER + 40);
        });
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    wire(".picker-grid", ".picker-chip", { burstColor: "#25d366" });
    wire(".ind-particle-grid", ".ind-particle-tile", { burstColor: "#25d366" });
  });
})();
