function toFahrenheit(celsius) {
  return (celsius * 9) / 5 + 32;
}

const input = document.getElementById("celsius");
const button = document.getElementById("convert");
const output = document.getElementById("output");

button.addEventListener("click", function () {
  const c = Number(input.value);
  const f = toFahrenheit(c);
  output.textContent = `${c}°C = ${f}°F`;
});
