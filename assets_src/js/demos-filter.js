// Demos index: text search + tap-to-filter industry chips, combined with AND logic.
(function () {
  var search = document.getElementById("demos-search");
  var filters = document.getElementById("demos-filters");
  var grid = document.getElementById("demos-grid");
  if (!search || !filters || !grid) return;

  var cards = Array.prototype.slice.call(grid.querySelectorAll(".demo-card"));
  var activeSlug = "";

  function apply() {
    var query = search.value.trim().toLowerCase();
    cards.forEach(function (card) {
      var matchesSearch = !query || card.dataset.search.indexOf(query) !== -1;
      var industries = (card.dataset.industries || "").split(" ");
      var matchesFilter = !activeSlug || industries.indexOf(activeSlug) !== -1;
      card.dataset.hidden = matchesSearch && matchesFilter ? "false" : "true";
    });
  }

  search.addEventListener("input", apply);
  filters.addEventListener("click", function (e) {
    var chip = e.target.closest(".demos-filter-chip");
    if (!chip) return;
    filters.querySelectorAll(".demos-filter-chip").forEach(function (c) { c.classList.remove("is-active"); });
    chip.classList.add("is-active");
    activeSlug = chip.dataset.slug || "";
    apply();
  });
})();
