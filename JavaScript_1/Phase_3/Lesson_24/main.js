let choices = ["rock", "paper", "scissors"];
let wins = 0,
  losses = 0,
  draws = 0,
  round = 1;

const buttons = document.querySelectorAll("#buttons button");

const playerChoiceHTML = document.querySelector(".playerChoice");
const computerChoiceHTML = document.querySelector(".computerChoice");
const winnerResultHTML = document.querySelector(".winnerResult");

const winsHTML = document.querySelector(".wins");
const lossesHTML = document.querySelector(".losses");
const drawsHTML = document.querySelector(".draws");

buttons.forEach((button) => {
  button.addEventListener("click", function () {
    console.log("Round:", round);
    document.querySelector(".round").textContent = `Round ${round + 1}`;

    const playerChoice = button.dataset.choice.toLowerCase();
    console.log("Player chose:", playerChoice);
    playerChoiceHTML.textContent = `Player: ${playerChoice}`;

    const computerChoice = getComputerChoice();
    console.log("computer chose:", computerChoice);
    computerChoiceHTML.textContent = `Computer: ${computerChoice}`;

    const result = getResult(playerChoice, computerChoice);
    console.log("Result:", result);
    winnerResultHTML.textContent = `Result: ${result}`;

    UpdateScore(result);
  });
});

function UpdateScore(result) {
  if (result === "win") {
    wins++;
    winsHTML.textContent = `wins: ${wins}`;
  } else if (result === "lose") {
    losses++;
    lossesHTML.textContent = `losses: ${losses}`;
  } else if (result === "draw") {
    draws++;
    drawsHTML.textContent = `draws: ${draws}`;
  }
  round++;
}

function getComputerChoice() {
  const randomIndex = Math.floor(Math.random() * choices.length);
  return choices[randomIndex];
}

function getResult(player, computer) {
  if (player === computer) return "draw";
  if (
    (player === "rock" && computer === "scissors") ||
    (player === "paper" && computer === "rock") ||
    (player === "scissors" && computer === "paper")
  )
    return "win";
  return "lose";
}
