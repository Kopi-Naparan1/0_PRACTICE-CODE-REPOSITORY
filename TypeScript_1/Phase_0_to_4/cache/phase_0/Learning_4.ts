// // Lesson 4 Type Assertion or Type Casting

// function msgLogger(message: any): void {
//   console.log(message);
// }

// type One = string;
// type Two = string | number;
// type Three = "Hello";

// let a: One = "Hello";
// let b = a as Two;
// let c = a as Three;

// function addOrConcat(
//   a: number,
//   b: number,
//   c: "add" | "concat"
// ): number | string | void {
//   if (c === "add") {
//     return a + b;
//   } else if (c === "concat") {
//     return `${a}${b}`;
//   }
// }

// let value1: string | number | void = addOrConcat(2, 7, "add");

// // ===== DOM

// const img1 = document.querySelector("#img") as HTMLImageElement;
// const img2 = document.getElementById("img") as HTMLImageElement;

// img1.src;
// img2.src;

// ===== footer - copywright =====
const year = document.getElementById("year") as HTMLSpanElement;
const currentYear: string = new Date().getFullYear().toString();
if (year) {
  year.setAttribute("datetime", currentYear);
  year.textContent = currentYear;
}
