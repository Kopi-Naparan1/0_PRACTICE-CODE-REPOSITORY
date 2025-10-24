function celsiusToFahrenheit(value) {
  return (value * 9) / 5 + 32;
}

function celsiusToKelvin(value) {
  return value + 273.15;
}

function kelvinToFahrenheit(value) {
  return ((value - 273.15) * 9) / 5 + 32;
}

function kelvinToCelsius(value) {
  return value - 273.15;
}

function fahrenheitToCelsius(value) {
  return ((value - 32) * 5) / 9;
}

function fahrenheitToKelvin(value) {
  return ((value - 32) * 5) / 9 + 273.15;
}

console.log(`
    [1] Celsius to Fahrenheit
    [2] Celsius to Kelvin
    [3] Kelvin to Fahrenheit
    [4] Kelvin to Celsius
    [5] Fahrenheit to Celsius
    [6] Fahrenheit to Kelvin`);

const conversions = {
  1: { start: "Celsius", end: "Fahrenheit", fn: celsiusToFahrenheit },
  2: { start: "Celsius", end: "Kelvin", fn: celsiusToKelvin },
  3: { start: "Kelvin", end: "Fahrenheit", fn: kelvinToFahrenheit },
  4: { start: "Kelvin", end: "Celsius", fn: kelvinToCelsius },
  5: { start: "Fahrenheit", end: "Celsius", fn: fahrenheitToCelsius },
  6: { start: "Fahrenheit", end: "Kelvin", fn: fahrenheitToKelvin },
};

function converter() {
  const choice = Number(prompt("Choose a number: "));

  if (!conversions[choice]) {
    console.log("Invalid choice. Please select a valid option");
    return;
  }

  const convertValue = Number(prompt(`${conversions[choice].start} value: `));

  if (isNaN(convertValue)) {
    console.log("Invalid number input");
    return;
  }

  const value = conversions[choice].fn(convertValue);

  const converted = `${conversions[choice].start} to ${
    conversions[choice].end
  } value: ${value.toFixed(2)}`;

  console.log(converted);
}

converter();
