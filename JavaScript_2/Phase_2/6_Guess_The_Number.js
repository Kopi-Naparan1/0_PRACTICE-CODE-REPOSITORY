function randomNumber() {
  return Math.floor(Math.random() * 100) + 1;
}

function indicator(number, guess) {
  if (guess > number) {
    return "Too high";
  } else if (guess < number) {
    return "Too low";
  } else {
    return "You guessed it right";
  }
}

function main() {
  const number = randomNumber();
  let life = 3;
  let isOn = true;

  while (isOn) {
    const guess = Number(prompt("Guess the number: "));

    const indi = indicator(number, guess);
    console.log(indi);

    if (indi === "You guessed it right") {
      isOn = false;
    } else {
      life -= 1;
      console.log(`Remaining life: ${life}`);
    }
    if (life === 0) {
      console.log("You lost!!!");
      isOn = false;
    }
    console.log("\n");
  }
}

main();
