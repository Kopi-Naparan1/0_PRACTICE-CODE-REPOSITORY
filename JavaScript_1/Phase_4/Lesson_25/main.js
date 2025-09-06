const countdown = document.querySelector("#countdown");
const input = document.querySelector("#countdownInput");
const surprise = document.querySelector("#surpise");
const startBtn = document.querySelector("#startBtn");

let intervalId;

startBtn.addEventListener("click", function () {
  clearInterval(intervalId);
  countdown.textContent = `0`;

  let seconds = parseInt(input.value);

  if (isNaN(seconds) || seconds <= 0) {
    countdown.textContent = `Enter a valid Number`;
    return;
  }

  intervalId = setInterval(() => {
    countdown.textContent = seconds;
    seconds--;

    if (seconds < 0) {
      clearInterval(intervalId);
      countdown.textContent = "🚀 LAUNCHED!";

      setTimeout(() => {
        countdown.textContent = "0";
      }, 3000);
    }
  }, 1000);
});
