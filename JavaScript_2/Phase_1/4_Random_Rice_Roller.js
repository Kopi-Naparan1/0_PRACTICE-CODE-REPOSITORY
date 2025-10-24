const diceOne = () => {
  const result = Math.floor(Math.random() * 6) + 1;
  return result;
};

const diceTwo = () => {
  const result = Math.floor(Math.random() * 6) + 1;
  return result;
};

function main() {
  const result = diceOne() + diceTwo();

  if (result < 6) {
    console.log("Unlucky");
  } else if (result < 12) {
    console.log("Lucky!");
  } else {
    console.log("Youre awesome!");
  }

  console.log(result);
}

main();
