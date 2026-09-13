/*
 * Canvas-based particle text effect.
 *
 * Given a target element, renders its text onto an offscreen canvas,
 * samples the drawn pixels at a stride, and turns each sampled pixel into
 * a lightweight particle with a home position (where it sits when the
 * text is fully readable) and a scatter target (where it drifts to when
 * fully dispersed). setProgress(t) — 0 = assembled/readable, 1 = fully
 * blown apart — interpolates every particle between those two points and
 * repaints a visible canvas placed exactly over the element, so the
 * effect is a pure function of t: driving t with scroll position makes it
 * reverse cleanly when the user scrolls back up.
 *
 * The source element's real text stays in the DOM so screen readers, SEO,
 * and the no-JS fallback are unaffected — this only ever runs after GSAP
 * has loaded and this script is only invoked from cinematic.js's
 * gsap:ready path. Crucially, the canvas is only shown WHILE t is
 * actually mid-transition: the instant a scene is fully assembled (t
 * back down near 0) the canvas is hidden and the real, normally
 * anti-aliased text is shown instead — a "held, readable" scene must
 * never sit there rendered as a sparse dot-grid.
 */
(function () {
  function easeOutCubic(x) { return 1 - Math.pow(1 - x, 3); }

  function ParticleText(el, opts) {
    opts = opts || {};
    this.el = el;
    this.stride = opts.stride || 3;
    this.drift = opts.drift || "down"; // "down" (gravity fall) or "up" (smoke rising)
    this.built = false;
    this._build();
  }

  ParticleText.prototype._build = function () {
    var el = this.el;
    var rect = el.getBoundingClientRect();
    if (!rect.width || !rect.height) return;

    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var cs = getComputedStyle(el);
    var color = cs.color;
    var fontSizePx = parseFloat(cs.fontSize) || 16;
    var lineHeight = parseFloat(cs.lineHeight);
    if (!lineHeight || isNaN(lineHeight)) lineHeight = fontSizePx * 1.25;

    var sample = document.createElement("canvas");
    sample.width = Math.ceil(rect.width * dpr);
    sample.height = Math.ceil(rect.height * dpr);
    var sctx = sample.getContext("2d");
    sctx.scale(dpr, dpr);
    sctx.font = cs.fontStyle + " " + cs.fontWeight + " " + cs.fontSize + " " + cs.fontFamily;
    sctx.fillStyle = color;
    sctx.textBaseline = "alphabetic";

    // Manually word-wrap to the element's own width — doesn't need to be
    // pixel-identical to the browser's own line breaks, since the real
    // DOM text is painted transparent and only this canvas is ever seen.
    var text = el.textContent.trim();
    var words = text.split(/\s+/);
    var lines = [];
    var current = "";
    words.forEach(function (w) {
      var test = current ? current + " " + w : w;
      if (current && sctx.measureText(test).width > rect.width) {
        lines.push(current);
        current = w;
      } else {
        current = test;
      }
    });
    if (current) lines.push(current);

    var baseline = fontSizePx * 0.85;
    lines.forEach(function (line, i) {
      sctx.fillText(line, 0, baseline + i * lineHeight);
    });

    var imgW = sample.width, imgH = sample.height;
    var data;
    try {
      data = sctx.getImageData(0, 0, imgW, imgH).data;
    } catch (e) {
      return;
    }

    var stride = Math.max(1, Math.round(Math.max(1, this.stride - 1) * dpr));
    var driftY = this.drift === "up" ? -1 : 1; // "smoke" targets drift upward instead of falling
    var particles = [];
    for (var y = 0; y < imgH; y += stride) {
      for (var x = 0; x < imgW; x += stride) {
        if (data[(y * imgW + x) * 4 + 3] > 80) {
          var angle = Math.random() * Math.PI * 2;
          var dist = 30 + Math.random() * 90;
          particles.push({
            hx: x / dpr, hy: y / dpr,
            tx: x / dpr + Math.cos(angle) * dist,
            ty: y / dpr + Math.sin(angle) * dist + driftY * (40 + Math.random() * 40),
            size: Math.max(1, (stride / dpr) * 0.9),
            jitter: Math.random(),
          });
        }
      }
    }
    if (!particles.length) return;

    var canvas = document.createElement("canvas");
    canvas.className = "ptxt-canvas";
    canvas.width = imgW;
    canvas.height = imgH;
    canvas.style.width = rect.width + "px";
    canvas.style.height = rect.height + "px";
    canvas.style.display = "none";

    el.parentNode.insertBefore(canvas, el.nextSibling);

    this.particles = particles;
    this.rectW = rect.width;
    this.rectH = rect.height;
    this.color = color;
    this.canvas = canvas;
    this.ctx = canvas.getContext("2d");
    this.ctx.scale(dpr, dpr);
    this.built = true;
    this.showingReal = true;
    this.setProgress(0);
  };

  // Below this, treat the scene as "at rest" — show the real, normally
  // rendered (fully anti-aliased) text and hide the particle canvas
  // entirely, rather than a dot-grid rendition of a static state.
  var REST_THRESHOLD = 0.04;

  ParticleText.prototype.setProgress = function (t) {
    if (!this.built) return;
    t = Math.max(0, Math.min(1, t));

    if (t < REST_THRESHOLD) {
      if (!this.showingReal) {
        this.canvas.style.display = "none";
        this.el.style.color = "";
        this.showingReal = true;
      }
      return;
    }

    if (this.showingReal) {
      this.canvas.style.display = "block";
      this.el.style.color = "transparent";
      this.showingReal = false;
    }

    var ctx = this.ctx;
    ctx.clearRect(0, 0, this.rectW, this.rectH);
    var baseAlpha = 1 - t;
    ctx.fillStyle = this.color;
    var particles = this.particles;
    for (var i = 0; i < particles.length; i++) {
      var p = particles[i];
      var localT = Math.min(1, t * (0.7 + p.jitter * 0.6));
      var eased = easeOutCubic(localT);
      var x = p.hx + (p.tx - p.hx) * eased;
      var y = p.hy + (p.ty - p.hy) * eased;
      ctx.globalAlpha = Math.max(0, baseAlpha * (1 - localT * 0.3));
      ctx.fillRect(x, y, p.size, p.size);
    }
    ctx.globalAlpha = 1;
  };

  window.ParticleText = ParticleText;
})();
