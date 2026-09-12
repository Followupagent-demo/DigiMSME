// Custom Pack configurator: tap an industry to see what's recommended,
// tick anything else, and it all becomes a live summary + a prefilled
// WhatsApp enquiry. No pricing is invented — selections just become a
// clear message a real person quotes on WhatsApp.
(function () {
  var form = document.getElementById("configurator-form");
  if (!form) return;

  var industryRow = document.getElementById("config-industry");
  var recommendedNote = document.getElementById("config-recommended");
  var summaryList = document.getElementById("config-summary-list");
  var waButton = document.getElementById("config-wa-cta");
  var cfg = window.ASLIKAAM_CONFIG || {};
  var wa = cfg.whatsappNumber || "911234567890";

  var selectedSlug = "";
  var selectedName = "";

  var industryModulesData = {};
  var dataEl = document.getElementById("industry-modules-data");
  if (dataEl) {
    try { industryModulesData = JSON.parse(dataEl.textContent); } catch (e) { industryModulesData = {}; }
  }

  function applyIndustryRecommendation() {
    var moduleIds = industryModulesData[selectedSlug] || [];
    var moduleCheckboxes = form.querySelectorAll("input[data-module-id]");

    if (!selectedSlug) {
      recommendedNote.textContent = "";
    } else {
      moduleCheckboxes.forEach(function (el) {
        el.checked = moduleIds.indexOf(el.dataset.moduleId) !== -1;
      });
      var names = Array.prototype.slice.call(moduleCheckboxes)
        .filter(function (el) { return el.checked; })
        .map(function (el) { return el.dataset.label; });
      recommendedNote.textContent = names.length
        ? "Recommended for " + selectedName + ": " + names.join(", ")
        : "";
    }
    render();
  }

  function render() {
    var checked = Array.prototype.slice
      .call(form.querySelectorAll("input[type=checkbox]:checked"))
      .map(function (el) { return el.dataset.label; });

    summaryList.innerHTML = "";
    if (!checked.length && !selectedName) {
      var li = document.createElement("li");
      li.className = "empty";
      li.textContent = "Select what you need — we'll build the quote message as you go.";
      summaryList.appendChild(li);
    } else {
      if (selectedName) {
        var indLi = document.createElement("li");
        indLi.textContent = "🏷 " + selectedName;
        summaryList.appendChild(indLi);
      }
      checked.forEach(function (label) {
        var li = document.createElement("li");
        li.textContent = "✓ " + label;
        summaryList.appendChild(li);
      });
    }

    var lines = [];
    if (selectedName) lines.push("Industry: " + selectedName);
    if (checked.length) lines.push("I'd like a quote for:\n- " + checked.join("\n- "));
    var msg = lines.length
      ? "Hi! " + lines.join("\n\n")
      : "Hi! I'd like to build a Custom Pack — can we talk through what I need?";
    waButton.href = "https://wa.me/" + wa + "?text=" + encodeURIComponent(msg);
  }

  if (industryRow) {
    industryRow.addEventListener("click", function (e) {
      var chip = e.target.closest(".use-case-chip");
      if (!chip) return;
      var alreadyActive = chip.classList.contains("is-active");
      industryRow.querySelectorAll(".use-case-chip").forEach(function (c) { c.classList.remove("is-active"); });
      if (alreadyActive) {
        selectedSlug = "";
        selectedName = "";
      } else {
        chip.classList.add("is-active");
        selectedSlug = chip.dataset.slug;
        selectedName = chip.dataset.name;
      }
      applyIndustryRecommendation();
    });
  }

  form.addEventListener("change", function (e) {
    if (!e.target.closest("#config-industry")) render();
  });
  render();
})();
