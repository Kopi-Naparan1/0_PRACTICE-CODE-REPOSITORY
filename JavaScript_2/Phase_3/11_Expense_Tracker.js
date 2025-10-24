function showMenu(menu) {
  console.log("");
  for (let i = 1; i < 6; i++) {
    let label = menu[i].label;
    console.log(`[${i}] ${label}`);
  }
  console.log("");
}

function showTotal(database) {
  if (database.length === 0) {
    console.log("There is no categories. Please add categories.");
  }

  for (let i = 0; i < database.length; i++) {
    if (database[i].expenses.length <= 0) {
      console.log("No expenses to be calculated");
      continue;
    } else {
      for (let j = 0; j < database[i].expenses.length; j++) {
        let lableExpense = database[j].name;
        const totalExpense = database.expenses.reduce((x, y) => {
          return x + y;
        }, 0);
        console.log(`[${lableExpense}}] ${totalExpense}`);
      }
    }
  }
}

function showCategories(categories) {
  if (categories.length === 0) {
    console.log("There is no categories. Please add categories.");
  }

  for (let i = 0; i < categories.length; i++) {
    let num = categories[i].serialNumber;
    let label = categories[i].name;

    console.log(`[${num}] ${label}`);
  }
}

function categoryObjectMaker(serialNumber, name) {
  categoryObject = {
    serialNumber: serialNumber,
    name: name,
    expenses: [],
  };

  return categoryObject;
}

function expenseObjectMaker(name, expense) {
  expenseObject = {
    name: name,
    expense: expense,
  };

  return expenseObject;
}

function categoryAdder(database, serialNumber, categoryObjectMaker) {
  let category = prompt("Name your new category: ");

  if (database.some((c) => c.name === category)) {
    console.log(`${category} is already available in the data base\n`);
  } else {
    let categoryObj = categoryObjectMaker(serialNumber, category);
    database.push(categoryObj);
    console.log(`Category ${categoryObj.name} is added.\n`);
  }
}

function expenseAdder(database, expenseObject) {
  if (database.length === 0) {
    console.log("There is no available category. Add a category first");
    return;
  }

  let choice = Number(prompt("Choose a category: "));
  let categoryIndex = database.findIndex((x) => x.serialNumber === choice);

  if (!(choice >= database.length && choice <= database.length)) {
    console.log(`Please choose a number between 1 to ${database.length}.`);
  }

  let objName = prompt("Expense name: ");
  let objExpense = Number(prompt("How much: "));

  let expense = expenseObject(objName, objExpense);

  console.log(`Expense: ${expense.name} - $${expense.expense} is added`);
  database[categoryIndex].expenses.push(expense);
}

function userChoice() {
  let choice = Number(prompt("Choose a number: "));
  return choice;
}

function menu() {
  m = {
    1: { label: "Add Expense", fn: expenseAdder },
    2: { label: "Add Category", fn: categoryAdder },
    3: { label: "Show Total", fn: showTotal },
    4: { label: "Show Categories", fn: showCategories },
    5: { label: "Quit" },
  };

  return m;
}

function main() {
  let isOn = true;
  let categoryNum = 1;

  let database = [];

  while (isOn) {
    const menus = menu();
    showMenu(menus);
    choice = userChoice();

    if (choice === 5) {
      console.log("Quiting...");
      isOn = false;
    } else if (choice === 1) {
      showCategories(database);
      menus[choice].fn(database, expenseObjectMaker);
    } else if (choice === 2) {
      menus[choice].fn(database, categoryNum, categoryObjectMaker);
    } else if (choice === 3) {
      menus[choice].fn(database);
    } else if (choice === 4) {
      menus[choice].fn(database);
    }
  }
}
main();
