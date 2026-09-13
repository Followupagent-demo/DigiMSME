/*
 * Agentic Use Cases page: lets the visitor set the AI's own discount
 * ceiling, then simulates a customer pushing past it — proving the agent
 * respects a limit the business owner set rather than deciding alone.
 * Plain vanilla JS, no GSAP/ParticleText dependency needed.
 */
(function () {
  var range = document.getElementById("guardrail-range");
  var valueOut = document.getElementById("guardrail-value-out");
  var testBtn = document.getElementById("guardrail-test-btn");
  var chatEl = document.getElementById("guardrail-chat");
  var thinkingEl = document.getElementById("guardrail-thinking");
  var stepsEl = document.getElementById("guardrail-steps");
  if (!range || !testBtn || !chatEl || !thinkingEl || !stepsEl) return;

  range.addEventListener("input", function () { valueOut.textContent = range.value; });

  function addBubble(cls, text) {
    var b = document.createElement("div");
    b.className = "chat-bubble " + cls;
    b.textContent = text;
    chatEl.appendChild(b);
  }

  function renderStepsStaggered(steps, onDone) {
    stepsEl.innerHTML = "";
    thinkingEl.style.display = "block";
    steps.forEach(function (step, i) {
      setTimeout(function () {
        var li = document.createElement("li");
        li.className = "brain-step";
        li.textContent = step;
        stepsEl.appendChild(li);
        if (i === steps.length - 1) setTimeout(onDone, 550);
      }, i * 500);
    });
  }

  testBtn.addEventListener("click", function () {
    chatEl.innerHTML = "";
    thinkingEl.style.display = "none";
    testBtn.disabled = true;

    var cap = parseInt(range.value, 10);
    var ask = Math.min(50, cap + 10 + Math.round(Math.random() * 10));
    addBubble("in", "Can you do " + ask + "% off if I book today?");

    renderStepsStaggered(
      ["Reading your guardrail: max " + cap + "% without approval…", "Customer asked for " + ask + "% — over the limit"],
      function () {
        addBubble("out", "I can offer you " + cap + "% right now, or flag this to the owner to see if a higher one-time waiver is possible — which would you prefer?");
        testBtn.disabled = false;
      }
    );
  });
})();
