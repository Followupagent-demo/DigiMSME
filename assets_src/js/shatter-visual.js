/*
 * "Shatter & fall" effect for whole visual panels — not text, a full
 * screen-mock box (e.g. the search-results phone screen). Instead of a
 * plain crossfade, the panel visibly breaks into small tinted tiles that
 * fall away past the bottom of the box (used on a "red"/ignored scene) or
 * rise up into place (the same math, running in reverse as the next scene
 * becomes focused — used on the paired "green"/tapped scene).
 *
 * Same continuous, scroll-position-driven model as ParticleText:
 * setProgress(0) = real content shown, canvas hidden; setProgress(1) =
 * fully shattered, real content hidden. A pure function of t, so scrolling
 * back up reverses it exactly — no one-shot animation.
 */
(function () {
  function easeOutCubic(x) { return 1 - Math.pow(1 - x, 3); }

  function ShatterVisual(el, opts) {
    opts = opts || {};
    this.el = el;
    this.color = opts.color || "#ff6b6b";
    this.cell = opts.cell || 26;
    this.built = false;
    this._build();
  }

  ShatterVisual.prototype._build = function () {
    var el = this.el;
    var rect = el.getBoundingClientRect();
    if (!rect.width || !rect.height) return;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);

    var canvas = document.createElement("canvas");
    canvas.className = "shatter-canvas";
    canvas.width = Math.ceil(rect.width * dpr);
    canvas.height = Math.ceil(rect.height * dpr);
    canvas.style.width = rect.width + "px";
    canvas.style.height = rect.height + "px";
    canvas.style.display = "none";
    el.parentNode.insertBefore(canvas, el.nextSibling);

    var cell = this.cell;
    var cols = Math.max(1, Math.round(rect.width / cell));
    var rows = Math.max(1, Math.round(rect.height / cell));
    var cw = rect.width / cols, ch = rect.height / rows;
    var particles = [];
    for (var gy = 0; gy < rows; gy++) {
      for (var gx = 0; gx < cols; gx++) {
        var hx = gx * cw, hy = gy * ch;
        particles.push({
          hx: hx, hy: hy, w: Math.max(1, cw - 2), h: Math.max(1, ch - 2),
          tx: hx + (Math.random() - 0.5) * cw * 4,
          ty: rect.height + ch * 2 + Math.random() * rect.height * 0.6,
          rot: (Math.random() - 0.5) * 1.4,
          jitter: Math.random(),
        });
      }
    }
    if (!particles.length) return;

    this.particles = particles;
    this.rectW = rect.width;
    this.rectH = rect.height;
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.ctx.scale(dpr, dpr);
    this.built = true;
    this.showingReal = true;
    this.setProgress(0);
  };

  // Below this, the panel is "at rest": show the real box, hide the shard
  // canvas entirely — never leave a held scene sitting there as tinted
  // tiles.
  var REST_THRESHOLD = 0.04;

  ShatterVisual.prototype.setProgress = function (t) {
    if (!this.built) return;
    t = Math.max(0, Math.min(1, t));

    if (t < REST_THRESHOLD) {
      if (!this.showingReal) {
        this.canvas.style.display = "none";
        this.el.style.opacity = "";
        this.showingReal = true;
      }
      return;
    }

    if (this.showingReal) {
      this.canvas.style.display = "block";
      this.el.style.opacity = "0";
      this.showingReal = false;
    }

    var ctx = this.ctx;
    ctx.clearRect(0, 0, this.rectW, this.rectH);
    var particles = this.particles;
    for (var i = 0; i < particles.length; i++) {
      var p = particles[i];
      var localT = Math.min(1, t * (0.7 + p.jitter * 0.6));
      var eased = easeOutCubic(localT);
      var x = p.hx + (p.tx - p.hx) * eased;
      var y = p.hy + (p.ty - p.hy) * eased;
      ctx.save();
      ctx.translate(x + p.w / 2, y + p.h / 2);
      ctx.rotate(p.rot * eased);
      ctx.globalAlpha = Math.max(0, Math.min(1, eased * 1.4)) * (1 - eased * 0.25);
      ctx.fillStyle = this.color;
      ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
      ctx.restore();
    }
    ctx.globalAlpha = 1;
  };

  window.ShatterVisual = ShatterVisual;
})();
