const header = document.querySelector("#header");
const btn1 = document.querySelector("#btn1");
const btn2 = document.querySelector("#btn2");
const btn3 = document.querySelector("#btn3");

btn1.addEventListener("click", function () {
  alert("Hello from JavaScript!");
});

btn2.addEventListener("click", function () {
  header.style.color = "tomato";
});

btn3.addEventListener("click", function () {
  if (header.textContent === "Click the buttons!") {
    header.textContent = "You clicked the toggle!";
  } else {
    header.textContent = "Click the buttons!";
  }
});
