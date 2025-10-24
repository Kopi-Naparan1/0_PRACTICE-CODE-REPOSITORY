function addition(x, y) {
  return x + y;
}

function subtraction(x, y) {
  return x - y;
}

function multiplication(x, y) {
  return x * y;
}

function division(x, y) {
  return x / y;
}

const functions = {
  "+": addition,
  "-": subtraction,
  "*": multiplication,
  "/": division,
};

function main() {
  let isTurnOn = true;
  while (isTurnOn) {
    const choice = prompt("(+ - * /) q to quit: ");

    if (choice === "q") {
      console.log("Quitting...");
      isTurnOn = false;
      continue;
    }

    if (!(choice in functions)) {
      console.log("Invalid Operator. Try Again.");
      continue;
    }

    const x = Number(prompt("value 1: "));
    const y = Number(prompt("value 2: "));

    if (isNaN(x) || isNaN(y)) {
      console.log("Invalid number input. Try again");
      continue;
    }

    if (choice === "/" && y === 0) {
      console.log("You cannot divide by zero. Try again");
    }
    const value = functions[choice](x, y);
    console.log(`${x} ${choice} ${y} = ${value}`);
  }
}

main();

// Learning: make sure you look for the quitting first
