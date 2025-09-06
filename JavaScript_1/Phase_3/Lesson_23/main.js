const products = [
  { name: "Keyboard", price: 1500 },
  { name: "Mouse", price: 800 },
  { name: "Monitor", price: 5500 },
  { name: "USB Cable", price: 250 },
  { name: "Laptop", price: 30000 },
  { name: "Phone", price: 2999 },
];

// 1. Filter: Only show items above ₱1000
const expensiveItems = products.filter((item) => item.price > 1000);

// 2. Map: Convert to display strings
const itemStrings = expensiveItems.map(
  (item) => `$${item.name} - ${item.price}`
);

// 3. Reduce: Sum the total price
const total = expensiveItems.reduce((sum, item) => sum + item.price, 0);

// Inject into HTML
const ul = document.querySelector("#productList");
itemStrings.forEach((str) => {
  const li = document.createElement("li");
  li.textContent = str;
  ul.appendChild(li);
});

document.querySelector("#totalValue").textContent = `$${total}`;
