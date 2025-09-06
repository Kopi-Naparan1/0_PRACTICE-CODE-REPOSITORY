const heading = document.querySelector(".heading");
const firstParagraph = document.querySelector(".desc");
const button = document.querySelector("#updateBtn");

button.addEventListener("click", function () {
  heading.textContent = "Update by JS";
  firstParagraph.style.color = "darkgreen";
});
