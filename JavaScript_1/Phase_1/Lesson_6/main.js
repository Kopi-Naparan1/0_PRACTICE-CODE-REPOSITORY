const input = document.getElementById("score");
const button = document.getElementById("gradeBtn");
const display = document.getElementById("grade");

button.addEventListener("click", function () {
  const score = Number(input.value);
  let grade;

  if (score >= 90) {
    grade = "A";
  } else if (score >= 80) {
    grade = "B";
  } else if (score >= 70) {
    grade = "C";
  } else if (score >= 60) {
    grade = "D";
  } else {
    grade = "F";
  }

  display.textContent = `Grade: ${grade}`;
});
