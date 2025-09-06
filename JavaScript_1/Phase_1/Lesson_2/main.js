let score = 0;
const display = document.getElementById("display");
const addBtn = document.getElementById("add");

addBtn.addEventListener("click", function () {
  score++;
  display.textContent = "Score: " + score;
});
