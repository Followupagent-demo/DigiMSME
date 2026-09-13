/*
 * Shared "pick one, everything else falls away" navigation transition —
 * used on Home's industry picker grid and the Agentic Use Cases particle
 * industry grid. On click: every OTHER card in the group dissolves into
 * fine falling pixel dust (reusing ShatterVisual), a burst of particles
 * radiates outward from the clicked card to fill the screen, then the
 * page navigates to that card's real href. No-op under
 * prefers-reduced-motion or without ShatterVisual — the link just
 * navigates normally.
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

  function burstFromElement(el, color, onDone) {
    var rect = el.getBoundingClientRect();
    var cx = rect.left + rect.width / 2, cy = rect.top + rect.height / 2;
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

    var maxDist = Math.hypot(vw, vh) * 0.75;
    var particles = [];
    for (var i = 0; i < 260; i++) {
      particles.push({
        angle: Math.random() * Math.PI * 2,
        dist: maxDist * (0.4 + Math.random() * 0.7),
        size: 3 + Math.random() * 4,
        jitter: Math.random(),
      });
    }

    animate(480, function (t) {
      ctx.clearRect(0, 0, vw, vh);
      ctx.fillStyle = color;
      particles.forEach(function (p) {
        var localT = Math.min(1, t * (0.8 + p.jitter * 0.5));
        var eased = 1 - Math.pow(1 - localT, 2);
        var x = cx + Math.cos(p.angle) * p.dist * eased;
        var y = cy + Math.sin(p.angle) * p.dist * eased;
        ctx.globalAlpha = Math.max(0, 1 - localT * 0.65);
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
    var fallColor = opts.fallColor || "#8a95a3";
    var burstColor = opts.burstColor || "#25d366";
    var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    Array.prototype.forEach.call(document.querySelectorAll(containerSelector), function (container) {
      var items = Array.prototype.slice.call(container.querySelectorAll(itemSelector));
      if (!items.length || reduceMotion || !window.ShatterVisual) return;

      items.forEach(function (item) {
        item.addEventListener("click", function (e) {
          if (item.dataset.busting) { e.preventDefault(); return; }
          var href = item.getAttribute("href");
          if (!href) return;
          e.preventDefault();
          item.dataset.busting = "1";

          items.forEach(function (other) {
            if (other === item) return;
            var sv = new window.ShatterVisual(other, { color: fallColor, cell: 5 });
            animate(420, function (t) { sv.setProgress(t); });
          });

          burstFromElement(item, burstColor, function () {
            window.location.href = href;
          });
        });
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    wire(".picker-grid", ".picker-chip", { fallColor: "#8a95a3", burstColor: "#25d366" });
    wire(".ind-particle-grid", ".ind-particle-tile", { fallColor: "#5a6472", burstColor: "#25d366" });
  });
})();
