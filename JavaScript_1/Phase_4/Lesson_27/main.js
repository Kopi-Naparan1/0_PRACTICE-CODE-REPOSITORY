let read = true;

let readBook = new Promise(function (resolve, reject) {
  setTimeout(() => {
    if (read) {
      resolve("I read the book");
    } else {
      reject("I didn't read the book");
    }
  }, 3000);
});

// then
readBook.then(
  (success) => console.log(success),
  (failure) => console.log(failure)
);

// catch
readBook.catch((failure) => console.log(failure));

// finally
readBook.finally(console.log("Done"));
