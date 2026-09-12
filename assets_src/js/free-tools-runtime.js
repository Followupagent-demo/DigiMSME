// Generic wiring for every Free Tools calculator page: reads all
// .tool-field inputs, calls the page's own computeResult(values)
// (defined inline per tool, since formulas differ), and live-updates
// the result panel on every keystroke.
(function () {
  var form = document.getElementById("tool-form");
  var result = document.getElementById("tool-result-body");
  if (!form || !result || typeof window.computeResult !== "function") return;

  function run() {
    var values = {};
    form.querySelectorAll("input[data-id]").forEach(function (el) {
      values[el.dataset.id] = parseFloat(el.value) || 0;
    });
    try {
      result.innerHTML = window.computeResult(values);
    } catch (e) {
      result.innerHTML = '<div class="tr-note">Enter valid numbers to see the result.</div>';
    }
  }

  form.addEventListener("input", run);
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    run();
  });
  run();
})();
