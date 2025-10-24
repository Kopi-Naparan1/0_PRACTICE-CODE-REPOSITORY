function hotOrCold(fahrenheit) {
  if (fahrenheit >= 101) {
    return `Extremely Hot`;
  } else if (fahrenheit >= 90) {
    return `Very Hot`;
  } else if (fahrenheit >= 75) {
    return `Warm to Hot`;
  } else if (fahrenheit >= 60) {
    return `Cool to comfortable`;
  } else if (fahrenheit >= 40) {
    return `Cold`;
  } else {
    return `Freezing Cold`;
  }
}

function convertCelsiusToFahrenheit(celsius) {
  return celsius * 1.8 + 32;
}

function askCelsius() {
  let celsius = Number(prompt("Input celsius: "));
  return celsius;
}

function main() {
  const celsius = askCelsius();
  const fahrenheit = convertCelsiusToFahrenheit(celsius);
  console.log(`Celsius: ${celsius}\nFahrenheit: ${fahrenheit.toFixed(2)}`);
  console.log();

  let result = hotOrCold(fahrenheit);
  console.log(result);
}
main();
