function getUser() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({ name: "Nyro", age: 18 }, 2000);
    });
  });
}

getUser()
  .then((user) => {
    console.log("User: ", user.name);
    return `Welcome, ${user.name}`;
  })
  .then((greeting) => {
    console.log(greeting);
    return greeting.toUpperCase();
  })
  .then((upperGreeting) => {
    console.log("Upper:", upperGreeting);
  })
  .catch((error) => console.log(error));
