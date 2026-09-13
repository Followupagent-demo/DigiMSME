/*
 * Industries page: each card flips on hover to reveal a BPM-style
 * workflow (discovery through payment and referral) on its back. CSS
 * :hover already handles desktop; this just makes tapping the card body
 * toggle the same flip on touch devices, without swallowing taps on the
 * real "Explore" link on the back face.
 */
(function () {
  var cards = document.querySelectorAll(".flip-card");
  if (!cards.length) return;
  cards.forEach(function (card) {
    card.addEventListener("click", function (e) {
      if (e.target.closest("a")) return;
      card.classList.toggle("is-flipped");
    });
  });
})();
