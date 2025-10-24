function password() {
  const pass = prompt("Enter a password: ");
  return pass;
}

function checkLength(password) {
  return password.length > 8;
}

function checkNumber(password) {
  return /\d/.test(password);
}

function checkCapitalLetter() {
  return /[A-Z]/.test(password);
}

function main() {
  const pass = password();

  const isLength = checkLength(pass);
  const isNumber = checkNumber(pass);
  const isCapital = checkCapitalLetter(pass);

  if (isLength && isNumber && isCapital) {
    console.log("Password is Strong");
  } else {
    console.log("Password is weak");
  }
}
main();
