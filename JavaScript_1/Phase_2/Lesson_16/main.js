const form = document.querySelector("#Form");
const nameInput = document.querySelector("#nameInput");
const ageInput = document.querySelector("#ageInput");
const greeting = document.querySelector("#greeting");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const name = nameInput.value.trim();
  if (name === "") return;

  const age = ageInput.value.trim();
  if (age === "") return;

  greeting.textContent = `Hello there ${name}! You are ${age} years old!`;
  nameInput.value = "";
  ageInput.value = "";
});
