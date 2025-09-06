const title = document.querySelector("#mainTitle");
const btnStyle = document.querySelector("#btnStyle");
const btnClass = document.querySelector("#btnClass");
const btnRandom = document.querySelector("#btnRandom");

const colors = ["#f44336", "#2196F3", "#4CAF50", "#FF9800"];

btnStyle.addEventListener("click", function () {
  title.style.color = "crimson";
  title.style.backgroundColor = "lightyellow";
  title.style.padding = "0.85rem";
});

btnClass.addEventListener("click", function () {
  title.classList.toggle("styled");
});

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

btnRandom.addEventListener("click", function () {
  let min_num = 1;
  let max_num = colors.length;

  random_num_1 = getRandomInt(min_num, max_num);

  title.style.color = colors[random_num_1];
  title.style.backgroundColor = "black";
  title.style.padding = "0.85rem";
});
