const input = document.getElementById("ageInput");
const button = document.getElementById("check");
const result = document.getElementById("result");

button.addEventListener("click", function () {
  let value = input.value;
  console.log("Raw value:", value);
  console.log("Type of value:", typeof value);

  let num = Number(value);
  console.log("Converted to Number:", num);
  console.log("Type of num:", typeof num);

  result.textContent = `You entered a ${typeof num}: ${num}`;
});
