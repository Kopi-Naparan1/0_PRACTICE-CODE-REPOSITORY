const ul = document.getElementById("user-list");

const users = ["Alice", "Bob", "Catty", "David"];
const fruits = ["apple", "banana", "orange", "durian", "mango"];

console.log(fruits[0]);
fruits.push("grapes");
fruits.unshift("rambutan");

fruits.forEach(function (fruit) {
  console.log(fruit);
});

const upperFruits = fruits.map((f) => f.toUpperCase());
console.log(upperFruits);

upperFruits.forEach(function (fruit) {
  console.log(fruit);
});

const longNames = fruits.filter((f) => f.length > 5);
console.log(longNames);

users.forEach(function (user) {
  const li = document.createElement("li");
  li.textContent = user;
  ul.appendChild(li);
});
