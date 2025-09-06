const button = document.querySelector("#greetBtn");
const output = document.querySelector("#output");

const player = {
  name: "Nyro",
  level: 5,
  greeting: function () {
    return `Hi ${this.name} you are level ${this.level}!`;
  },
};

button.addEventListener("click", function () {
  const greet = player.greeting();
  output.innerText = greet;
});
