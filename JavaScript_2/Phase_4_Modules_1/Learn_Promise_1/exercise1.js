function loadData() {
  let data = Math.floor(Math.random() * 2) + 1;
  return new Promise((resolve, reject) => {
    if (data === 1) {
      resolve("Loaded");
    } else {
      reject("Not Loaded");
    }
  });
}

setTimeout(
  () =>
    loadData()
      .then((message) => {
        console.log(message);
      })
      .catch((message) => {
        console.log(message);
      }),
  1000
);
