// Home hero: the background grid's spotlight follows the cursor on
// desktop. Pure progressive enhancement — no mousemove ever fires on
// touch, so the grid just sits at its default center position there,
// which is a perfectly fine static look.
(function () {
  var hero = document.getElementById("home-hero");
  if (!hero) return;
  hero.addEventListener("mousemove", function (e) {
    var rect = hero.getBoundingClientRect();
    var x = ((e.clientX - rect.left) / rect.width) * 100;
    var y = ((e.clientY - rect.top) / rect.height) * 100;
    hero.style.setProperty("--hx", x + "%");
    hero.style.setProperty("--hy", y + "%");
  });
})();
