const input = document.getElementById("age");
const button = document.getElementById("check");
const result = document.getElementById("result");

button.addEventListener("click", function () {
  const age = Number(input.value);

  const canDrive = age >= 18;

  result.textContent = canDrive
    ? "You can legally drive"
    : "You cant drive yet";
});
