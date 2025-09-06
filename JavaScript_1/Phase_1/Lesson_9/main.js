const user = {
  name: "Nyro",
  age: 21,
  location: "Philippines",
  skills: ["guitarist", "produces", "programmer"],
  isLoggedIn: true,
};

const ul = document.getElementById("ul");

document.getElementById("location").textContent = `Location: ${user.location}`;
document.getElementById("name").textContent = `Name: ${user.name}`;
document.getElementById("age").textContent = `age: ${user.age}`;
document.getElementById("status").textContent = user.isLoggedIn
  ? "Status: Logged In"
  : "Status: Guest";

user.skills.forEach(function (skill) {
  const li = document.createElement("li");
  li.textContent = skill;
  ul.appendChild(li);
});

console.log(user);
