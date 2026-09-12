// Industry pages: switches the visible before/after preview panel to match
// whichever use-case chip is tapped (primary use case or one of its mapped
// secondary automation modules).
(function () {
  document.querySelectorAll(".use-case-chip-row").forEach(function (row) {
    var container = row.closest("section").querySelector(".use-case-panels");
    if (!container) return;
    row.addEventListener("click", function (e) {
      var chip = e.target.closest(".use-case-chip");
      if (!chip) return;
      row.querySelectorAll(".use-case-chip").forEach(function (c) { c.classList.remove("is-active"); });
      chip.classList.add("is-active");
      container.querySelectorAll(".use-case-panel").forEach(function (panel) {
        panel.hidden = panel.dataset.usecase !== chip.dataset.usecase;
      });
    });
  });
})();
