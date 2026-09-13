/*
 * A small, separate particle system (not text-based) for the Payment
 * loss-point scene: a handful of "₹" glyphs scattered around a container,
 * floating in place while the scene is being read, then spiral-vacuumed
 * into the center and consumed as the scene disperses. Driven by the same
 * continuous dispersion value as everything else in cinematic.js, so it's
 * a pure function of scroll position and reverses cleanly.
 */
(function () {
  function CurrencyParticles(container, opts) {
    opts = opts || {};
    this.container = container;
    this.count = opts.count || 12;
    this.built = false;
    this._build();
  }

  CurrencyParticles.prototype._build = function () {
    var rect = this.container.getBoundingClientRect();
    if (!rect.width || !rect.height) return;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);

    var canvas = document.createElement("canvas");
    canvas.className = "cur-particles-canvas";
    canvas.width = Math.ceil(rect.width * dpr);
    canvas.height = Math.ceil(rect.height * dpr);
    canvas.style.width = rect.width + "px";
    canvas.style.height = rect.height + "px";
    this.container.appendChild(canvas);

    this.ctx = canvas.getContext("2d");
    this.ctx.scale(dpr, dpr);
    this.rectW = rect.width;
    this.rectH = rect.height;
    this.targetX = rect.width / 2;
    this.targetY = rect.height / 2;

    var particles = [];
    var minSide = Math.min(rect.width, rect.height);
    for (var i = 0; i < this.count; i++) {
      var angle0 = Math.random() * Math.PI * 2;
      var dist0 = minSide * (0.4 + Math.random() * 0.35);
      particles.push({
        angle0: angle0,
        dist0: dist0,
        size: 14 + Math.random() * 12,
        spin: (Math.random() < 0.5 ? -1 : 1) * (0.6 + Math.random() * 0.8),
      });
    }
    this.particles = particles;
    this.canvas = canvas;
    this.built = true;
    this.setProgress(0);
  };

  CurrencyParticles.prototype.setProgress = function (t) {
    if (!this.built) return;
    t = Math.max(0, Math.min(1, t));
    var ctx = this.ctx;
    ctx.clearRect(0, 0, this.rectW, this.rectH);
    if (t >= 0.97) return; // fully vacuumed — nothing left to draw

    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillStyle = "#25d366";
    var eased = Math.pow(t, 1.6);
    var particles = this.particles;
    for (var i = 0; i < particles.length; i++) {
      var p = particles[i];
      var angle = p.angle0 + p.spin * eased * Math.PI * 2;
      var dist = p.dist0 * (1 - eased);
      var x = this.targetX + Math.cos(angle) * dist;
      var y = this.targetY + Math.sin(angle) * dist;
      ctx.globalAlpha = 1 - eased;
      ctx.font = "bold " + p.size * (1 - eased * 0.4) + "px sans-serif";
      ctx.fillText("₹", x, y);
    }
    ctx.globalAlpha = 1;
  };

  window.CurrencyParticles = CurrencyParticles;
})();
