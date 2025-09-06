// Two player objects with greet method
const player1 = {
  name: "Nyro",
  greet: function () {
    document.getElementById("output").innerText = `Hello from ${this.name}`;
  },
};

const player2 = {
  name: "Ada",
  greet: player1.greet, // reusing method
};

// Bind buttons to greet methods
document
  .getElementById("btn1")
  .addEventListener("click", player1.greet.bind(player1));
document
  .getElementById("btn2")
  .addEventListener("click", player2.greet.bind(player2));
