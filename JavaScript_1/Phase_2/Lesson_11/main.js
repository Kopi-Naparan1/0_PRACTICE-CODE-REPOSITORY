const titleElement = document.getElementById("title");
const button = document.getElementById("changeBtn");

button.addEventListener("click", function () {
  titleElement.textContent = "Dom Changed Me!";
  titleElement.style.color = "crimson";
});
