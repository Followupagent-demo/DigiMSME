/*
 * "Free fall" pixel-dust effect for whole visual panels — not text, a
 * full screen-mock box (e.g. the search-results phone screen). Instead of
 * a plain crossfade, the panel dissolves into fine pixel dust that falls
 * straight down past the bottom of the box and vanishes (used on a
 * "red"/ignored scene), or the same math running in reverse as the next
 * scene becomes focused (used on the paired "green"/tapped scene).
 *
 * Deliberately fine-grained and non-rotating — small pixels falling
 * straight down reads as a smooth dissolve; larger tumbling tiles read as
 * a glitch. Same continuous, scroll-position-driven model as
 * ParticleText: setProgress(0) = real content shown, canvas hidden;
 * setProgress(1) = fully dissolved, real content hidden. A pure function
 * of t, so scrolling back up reverses it exactly.
 */
(function () {
  function easeOutCubic(x) { return 1 - Math.pow(1 - x, 3); }

  function ShatterVisual(el, opts) {
    opts = opts || {};
    this.el = el;
    this.color = opts.color || "#ff6b6b";
    this.cell = opts.cell || 5;
    this.built = false;
    this._build();
  }

  ShatterVisual.prototype._build = function () {
    var el = this.el;
    var rect = el.getBoundingClientRect();
    if (!rect.width || !rect.height) return;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);

    var cell = this.cell;
    var cols = Math.max(1, Math.round(rect.width / cell));
    var rows = Math.max(1, Math.round(rect.height / cell));
    var cw = rect.width / cols, ch = rect.height / rows;

    // Pixels fall well past the box's own bottom edge to read as a real
    // freefall, not a wipe — the canvas has to extend down into that drop
    // zone too, or anything past the box's own height is invisibly
    // clipped by the canvas's own bitmap bounds long before the fall (and
    // its alpha fade-in) has actually played out.
    var dropZone = rect.height * 1.6 + ch * 3;
    var canvasH = rect.height + dropZone;

    var canvas = document.createElement("canvas");
    canvas.className = "shatter-canvas";
    canvas.width = Math.ceil(rect.width * dpr);
    canvas.height = Math.ceil(canvasH * dpr);
    canvas.style.width = rect.width + "px";
    canvas.style.height = canvasH + "px";
    canvas.style.display = "none";

    // Sibling of el, not a child (hiding el via opacity must never hide
    // the canvas too) — so its position can't assume el's parent is the
    // positioned ancestor at exactly el's own offset. Anchor with an
    // explicit pixel offset computed from real geometry instead.
    var parent = el.parentNode;
    if (getComputedStyle(parent).position === "static") parent.style.position = "relative";
    var parentRect = parent.getBoundingClientRect();
    canvas.style.left = (rect.left - parentRect.left) + "px";
    canvas.style.top = (rect.top - parentRect.top) + "px";

    parent.insertBefore(canvas, el.nextSibling);

    // Straight-down fall with only a light horizontal drift — enough to
    // feel like dust, not so much it reads as sideways scatter.
    var particles = [];
    for (var gy = 0; gy < rows; gy++) {
      for (var gx = 0; gx < cols; gx++) {
        var hx = gx * cw, hy = gy * ch;
        particles.push({
          hx: hx, hy: hy, w: Math.max(1, cw - 0.5), h: Math.max(1, ch - 0.5),
          tx: hx + (Math.random() - 0.5) * cw * 1.2,
          ty: rect.height + ch + Math.random() * (dropZone - ch),
          jitter: Math.random(),
        });
      }
    }
    if (!particles.length) return;

    this.particles = particles;
    this.rectW = rect.width;
    this.rectH = canvasH;
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.ctx.scale(dpr, dpr);
    this.built = true;
    this.showingReal = true;
    this.setProgress(0);
  };

  // Below this, the panel is "at rest": show the real box, hide the dust
  // canvas entirely — never leave a held scene sitting there as pixels.
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
    ctx.fillStyle = this.color;
    var particles = this.particles;
    for (var i = 0; i < particles.length; i++) {
      var p = particles[i];
      var localT = Math.min(1, t * (0.7 + p.jitter * 0.6));
      var eased = easeOutCubic(localT);
      var x = p.hx + (p.tx - p.hx) * eased;
      var y = p.hy + (p.ty - p.hy) * eased;
      ctx.globalAlpha = Math.max(0, Math.min(1, eased * 1.4)) * (1 - eased * 0.25);
      ctx.fillRect(x, y, p.w, p.h);
    }
    ctx.globalAlpha = 1;
  };

  window.ShatterVisual = ShatterVisual;
})();
