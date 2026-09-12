// Agentic Use Cases page: tap-to-filter between All / Non-Agentic / Agentic sections.
(function () {
  var filters = document.getElementById("agentic-filters");
  var sections = Array.prototype.slice.call(document.querySelectorAll(".agentic-kind-section"));
  if (!filters || !sections.length) return;

  filters.addEventListener("click", function (e) {
    var chip = e.target.closest(".demos-filter-chip");
    if (!chip) return;
    filters.querySelectorAll(".demos-filter-chip").forEach(function (c) { c.classList.remove("is-active"); });
    chip.classList.add("is-active");
    var kind = chip.dataset.kind;
    sections.forEach(function (section) {
      section.style.display = (kind === "all" || section.dataset.kind === kind) ? "" : "none";
    });
  });
})();
