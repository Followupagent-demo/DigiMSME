// Home: an interactive sandbox where a typed message dissolves into
// particles if it doesn't get a reply within 3 seconds — the exact
// mechanism the "Enquiry" loss-point scene tells a story about, except
// the visitor's own words. Uses ParticleText directly with a plain
// requestAnimationFrame tween, not GSAP, so it works even if the GSAP
// CDN is blocked — this is a bonus interactive, not core content, and
// there's no reason to make it depend on a library it doesn't need.
(function () {
  var form = document.getElementById("sandbox-form");
  var input = document.getElementById("sandbox-input");
  var mock = document.getElementById("sandbox-chat-mock");
  var statusEl = document.getElementById("sandbox-status");
  if (!form || !input || !mock || !statusEl) return;

  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var pending = null;

  function clearPending() {
    if (!pending) return;
    clearTimeout(pending.timeoutId);
    clearInterval(pending.intervalId);
    pending = null;
  }

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

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var text = input.value.trim();
    if (!text) return;
    clearPending();
    var oldReply = mock.querySelector(".sandbox-reply-btn");
    if (oldReply) oldReply.remove();

    var bubble = document.createElement("div");
    bubble.className = "chat-bubble in";
    bubble.textContent = text;
    mock.appendChild(bubble);
    input.value = "";
    mock.scrollTop = mock.scrollHeight;

    var replyBtn = document.createElement("button");
    replyBtn.type = "button";
    replyBtn.className = "btn btn-ghost sandbox-reply-btn";
    replyBtn.textContent = "Reply now";
    mock.appendChild(replyBtn);

    var secondsLeft = 3;
    statusEl.textContent = "Seen · no reply · " + secondsLeft + "s";

    var ptxt = (!reduceMotion && window.ParticleText) ? new window.ParticleText(bubble, { stride: 2 }) : null;

    function explode() {
      clearPending();
      replyBtn.remove();
      statusEl.textContent = "Gone — they've already asked someone else.";
      if (ptxt) {
        animate(700, function (t) { ptxt.setProgress(t); }, function () { bubble.remove(); });
      } else {
        bubble.remove();
      }
    }

    function reply() {
      clearPending();
      replyBtn.remove();
      statusEl.textContent = "Online";
      var out = document.createElement("div");
      out.className = "chat-bubble out";
      out.textContent = "Thanks for your message! How can I help?";
      mock.appendChild(out);
      mock.scrollTop = mock.scrollHeight;
    }

    replyBtn.addEventListener("click", reply);

    var intervalId = setInterval(function () {
      secondsLeft -= 1;
      if (secondsLeft > 0) statusEl.textContent = "Seen · no reply · " + secondsLeft + "s";
    }, 1000);
    var timeoutId = setTimeout(explode, 3000);
    pending = { timeoutId: timeoutId, intervalId: intervalId };
  });
})();
