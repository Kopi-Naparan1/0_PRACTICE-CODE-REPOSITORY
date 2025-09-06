// return number
function minutesToHours(minutes: number): number {
  return minutes / 60;
}

// return string
function greetCLient(name: string): string {
  return `Welcome, ${name}! `;
}

const greet = greetCLient("nyro khufraleq");
console.log(greet);
