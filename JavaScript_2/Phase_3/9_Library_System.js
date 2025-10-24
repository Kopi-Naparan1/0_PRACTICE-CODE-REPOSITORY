function addBook(DataBase, serialNum) {
  const title = prompt("Book title: ");
  const author = prompt("Author: ");
  const yearPublished = prompt("Year Published: ");

  const book = {
    serialNumber: serialNum,
    title: title,
    author: author,
    published: yearPublished,
  };

  DataBase.push(book);

  console.log(`${title} is added to the database.\n`);
}

function borrowBook(DataBase, borrowedBookDataBase, showBooks) {
  showBooks(DataBase);

  if (DataBase.length === 0) {
    console.log("There is no book to borrow.");
    return;
  }
  let isOn = true;
  while (isOn) {
    const choice = Number(
      prompt("Choose a book by its serial number - 0 to exit: ")
    );

    if (isNaN(choice)) {
      console.log("Please enter a number");
      continue;
    }

    if (!DataBase.some((b) => b.serialNumber === choice) && choice !== 0) {
      console.log("Invalid serial number");
      continue;
    }

    if (choice === 0) {
      isOn = false;
    }

    const borrow = DataBase.find((b) => b.serialNumber === choice);
    const index = DataBase.findIndex((b) => b.serialNumber === choice);

    if (borrow) {
      borrowedBookDataBase.push(borrow);
    }
    if (index !== -1) {
      console.log(`Borrowed ${DataBase[index].title}`);
      DataBase.splice(index, 1);

      return null;
    }
  }
}

function removeBook(DataBase, showBooks) {
  showBooks(DataBase);
  if (DataBase.length === 0) {
    console.log("There is no book to remove.");
    return;
  }
  let isOn = true;
  while (isOn) {
    const choice = Number(
      prompt("Choose a book by its serial number - 0 to exit: ")
    );

    if (isNaN(choice)) {
      console.log("Please enter a number");
      continue;
    }

    if (!DataBase.some((b) => b.serialNumber === choice) && choice !== 0) {
      console.log("Invalid serial number");
      continue;
    }

    if (choice === 0) {
      isOn = false;
    }
    const index = DataBase.findIndex((b) => b.serialNumber === choice);

    if (index !== -1) {
      console.log(`${DataBase[index].title} is removed`);
      DataBase.splice(index, 1);
    }
  }
}

// IMPROVE THIS SOON
// function updateBook(DataBase) {
//   showBooks(DataBase);

//   let isOn = true;
//   while (isOn) {
//     const choice = Number(
//       prompt("Choose a book by its serial number - 0 to exit: ")
//     );

//     if (DataBase.length === 0) {
//       console.log("There is no book to borrow.");
//       return;
//     }

//     if (isNaN(choice)) {
//       console.log("Please enter a number");
//       continue;
//     }

//     if (!DataBase.some((b) => b.serialNumber === choice) && choice !== 0) {
//       console.log("Invalid serial number");
//       continue;
//     }

//     if (choice === 0) {
//       isOn = false;
//     }

//     const book = Object.find((b) => b.serialNumber === choice);
//   }
//   if (book !== null) {
//   }
// }

function returnBook(DataBase, borrowedBookDB, showBooks) {
  showBooks(borrowedBookDB);

  if (borrowedBookDB.length === 0) {
    console.log("There is/are no books to return.");
    return null;
  }

  let isOn = true;
  while (isOn) {
    const choice = Number(
      prompt("Choose a book by its serial number - 0 to exit: ")
    );

    if (isNaN(choice)) {
      console.log("Please enter a number");
      continue;
    }

    if (
      !borrowedBookDB.some((b) => b.serialNumber === choice) &&
      choice !== 0
    ) {
      console.log("Invalid serial number");
      continue;
    }

    if (choice === 0) {
      isOn = false;
    }
    const index = borrowedBookDB.findIndex((b) => b.serialNumber === choice);

    if (index !== -1) {
      const returned = borrowedBookDB.splice(index, 1)[0];
      DataBase.push(returned);
      console.log(`Borrowed book: ${returned.title} is returned`);
    }
  }
}

function showBooks(DataBase) {
  for (let i = 0; i < DataBase.length; i++) {
    console.log(`[${DataBase[i].serialNumber}] ${DataBase[i].title}`);
  }
}

function userChoice() {
  const choice = Number(prompt("Choose a number [1-5]: "));

  if (isNaN(choice)) {
    console.log("Please enter a number");
    return null;
  }

  if (choice < 1 || choice > 5) {
    console.log("Make sure you choose numbers from 1 to 5");
    return null;
  }

  return choice;
}

function borrowedDataBase() {
  const database = [];
  return database;
}
function libraryDataBase() {
  const database = [];
  return database;
}

function libraryMenu() {
  const menu = {
    1: { label: "Add Book", action: addBook },
    2: { label: "Borrow Book", action: borrowBook },
    3: { label: "Remove Book", action: removeBook },
    4: { label: "Return Book", action: returnBook },
  };

  return menu;
}

function showLibraryMenu(menu) {
  for (const [key, value] of Object.entries(menu)) {
    console.log(`[${key}] ${value.label}`);
  }
  console.log(`[${Object.keys(menu).length + 1}] Quit`);
}

function main() {
  let isOn = true;
  const menu = libraryMenu();
  const libaryDB = libraryDataBase();
  const borrowedDB = borrowedDataBase();
  let i = 1;

  while (isOn) {
    showLibraryMenu(menu);

    const choice = userChoice();

    if (choice === null) {
      continue;
    }

    if (choice === 5) {
      console.log("Quitting... \n");
      isOn = false;
    } else if (choice === 1) {
      menu[choice].action(libaryDB, i);
      i += 1;
    } else if (choice === 2) {
      menu[choice].action(libaryDB, borrowedDB, showBooks);
    } else if (choice === 3) {
      menu[choice].action(libaryDB, showBooks);
    } else if (choice === 4) {
      menu[choice].action(libaryDB, borrowedDB, showBooks);
    } else {
      continue;
    }
  }
}

main();
