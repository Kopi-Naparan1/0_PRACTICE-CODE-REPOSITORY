const paragraph = document.getElementById("paragraph");
const button = document.getElementById("add_paragraph_button");

let num_of_paragraphs = 0;
button.addEventListener("click", function () {
  for (let i = 1; i <= 5; i++) {
    if (num_of_paragraphs === 20) {
      console.log("Reached the limit");
      break;
    }
    const p = document.createElement("p");

    num_of_paragraphs += 1;

    p.textContent = `Paragraph ${num_of_paragraphs}`;

    if (num_of_paragraphs % 2 === 0) {
      p.style.color = "green";
    } else {
      p.style.color = "blue";
    }
    paragraph.appendChild(p);
  }
});
