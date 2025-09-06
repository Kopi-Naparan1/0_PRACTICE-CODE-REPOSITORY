const btn = document.getElementById("submitBtn");
btn.addEventListener("click", () => alert("Clicked!"));

const product = document.querySelector(".product");
console.log(product.dataset.price); // "29.99"
