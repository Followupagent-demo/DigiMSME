// Home: a personalized "how much are you losing" calculator — same
// math shape as the site's Free Tools calculators, with a lightweight
// ambient particle-drip visual behind the number. Pure vanilla JS +
// canvas, no GSAP dependency, so it works everywhere including the
// no-JS/CDN-blocked fallback (the drip is just a bonus if canvas/rAF
// are available; the number itself needs nothing but plain inputs).
(function () {
  var form = document.getElementById("leak-calc-form");
  var amountEl = document.getElementById("leak-amount");
  var canvas = document.getElementById("leak-drip-canvas");
  var resultBox = document.getElementById("leak-calc-result");
  if (!form || !amountEl || !resultBox) return;

  var leadsEl = document.getElementById("lc-leads");
  var valueEl = document.getElementById("lc-value");
  var lostEl = document.getElementById("lc-lost");

  var currentValue = 0;
  var displayValue = 0;

  function compute() {
    var leads = parseFloat(leadsEl.value) || 0;
    var value = parseFloat(valueEl.value) || 0;
    var lostPct = parseFloat(lostEl.value) || 0;
    currentValue = leads * value * (lostPct / 100);
  }

  form.addEventListener("input", compute);
  compute();
  displayValue = currentValue;
  amountEl.textContent = "₹" + Math.round(displayValue).toLocaleString("en-IN");

  if (!canvas || !canvas.getContext) return; // number still works without the visual

  var ctx = canvas.getContext("2d");
  var dpr = Math.min(window.devicePixelRatio || 1, 2);

  function resize() {
    var rect = resultBox.getBoundingClientRect();
    canvas.width = Math.ceil(rect.width * dpr);
    canvas.height = Math.ceil(rect.height * dpr);
    canvas.style.width = rect.width + "px";
    canvas.style.height = rect.height + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  resize();
  window.addEventListener("resize", resize);

  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduceMotion) return; // static number only, no drip animation

  var running = true;
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) { running = entries[0].isIntersecting; });
    io.observe(resultBox);
  }

  var drops = [];
  var lastSpawn = 0;

  function tick(ts) {
    requestAnimationFrame(tick);
    if (!running) return;
    var rect = resultBox.getBoundingClientRect();

    if (ts - lastSpawn > 550 && drops.length < 10) {
      drops.push({ x: Math.random() * rect.width, y: -10, vy: 1 + Math.random() * 1.4, size: 12 + Math.random() * 6 });
      lastSpawn = ts;
    }

    ctx.clearRect(0, 0, rect.width, rect.height);
    ctx.fillStyle = "#25d366";
    ctx.textAlign = "center";
    drops = drops.filter(function (d) {
      d.y += d.vy;
      ctx.globalAlpha = Math.max(0, 1 - d.y / rect.height);
      ctx.font = "bold " + d.size + "px sans-serif";
      ctx.fillText("₹", d.x, d.y);
      return d.y < rect.height + 20;
    });
    ctx.globalAlpha = 1;

    displayValue += (currentValue - displayValue) * 0.08;
    if (Math.abs(currentValue - displayValue) < 1) displayValue = currentValue;
    amountEl.textContent = "₹" + Math.round(displayValue).toLocaleString("en-IN");
  }
  requestAnimationFrame(tick);
})();
