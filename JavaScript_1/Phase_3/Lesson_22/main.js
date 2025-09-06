const modal = document.getElementById("modal");
const openBtn = document.getElementById("openBtn");
const closeBtn = document.getElementById("closeBtn");

openBtn.addEventListener("click", function () {
  modal.classList.remove("hidden");
});

closeBtn.addEventListener("click", function () {
  modal.classList.add("hidden");
});

document.addEventListener("keydown", function (input) {
  if (input.key === "Escape" && !modal.classList.contains("hidden")) {
    modal.classList.add("hidden");
  }
});

document.addEventListener("keydown", function (input) {
  if (input.key === "Enter" && modal.classList.contains("hidden")) {
    modal.classList.remove("hidden");
  }
});
