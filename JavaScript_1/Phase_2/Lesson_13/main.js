const title = document.querySelector("#mainTitle");
const content = document.querySelector("#contentBox");
const button = document.querySelector("#btnChange");
const reset = document.querySelector("#btnReset");

button.addEventListener("click", function () {
  title.textContent = "Updated with TextContent";
  content.innerHTML =
    "<strong>Now this is bold!</strong><br><em>And this is italic</em>";
});

reset.addEventListener("click", function () {
  title.textContent = "Original Title";
  reset.disabled = true;
  content.innerHTML = "";
  setTimeout(() => {
    content.innerHTML = "Reset Complete";
    reset.disabled = false;
  }, 1000);
});
