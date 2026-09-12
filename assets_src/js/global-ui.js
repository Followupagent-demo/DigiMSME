// Injects the persistent WhatsApp float button + mobile Call/WhatsApp bar on every page.
(function () {
  var cfg = window.ASLIKAAM_CONFIG || {};
  var wa = cfg.whatsappNumber || "911234567890";
  var phone = cfg.phoneNumber || "+911234567890";
  var waHref = "https://wa.me/" + wa + "?text=" + encodeURIComponent("Hi! I'd like to know more about AsliKaam.");

  var floatBtn = document.createElement("a");
  floatBtn.className = "wa-float";
  floatBtn.href = waHref;
  floatBtn.target = "_blank";
  floatBtn.rel = "noopener";
  floatBtn.setAttribute("aria-label", "Chat on WhatsApp");
  floatBtn.innerHTML =
    '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.1-1.7-.8-1.9-.9-.3-.1-.4-.1-.6.1-.2.3-.7.9-.8 1-.2.2-.3.2-.5.1-1.5-.7-2.5-1.3-3.5-3-.3-.5.3-.4.7-1.4.1-.2 0-.4 0-.5-.1-.1-.6-1.5-.8-2-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.5.1-.7.3-.3.3-1 1-1 2.4s1 2.8 1.2 3c.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.5-.1 1.7-.7 1.9-1.3.2-.7.2-1.2.2-1.3-.1-.1-.3-.2-.6-.3zM12 2C6.5 2 2 6.5 2 12c0 1.9.5 3.6 1.4 5.1L2 22l5-1.3c1.4.8 3.1 1.2 4.9 1.2 5.5 0 10-4.5 10-10S17.5 2 12 2z"/></svg>';
  document.body.appendChild(floatBtn);

  if (window.matchMedia && window.matchMedia("(max-width: 640px)").matches) {
    var bar = document.createElement("div");
    bar.className = "mobile-bar";
    bar.innerHTML =
      '<a class="call" href="tel:' + phone + '">📞 Call</a>' +
      '<a class="whatsapp" href="' + waHref + '" target="_blank" rel="noopener">💬 WhatsApp</a>';
    document.body.appendChild(bar);
  }
})();
