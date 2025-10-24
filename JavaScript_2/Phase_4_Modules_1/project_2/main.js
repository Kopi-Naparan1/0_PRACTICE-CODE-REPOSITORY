import expenses from "./data/expenses.js";
import addExpense from "./utils/addExpense.js";
import totalExpenses from "./utils/getTotal.js";
import listExpenses from "./utils/listExpenses.js";

const database = expenses();

addExpense(100, database);
addExpense(1003, database);
addExpense(10012, database);

listExpenses(database);

const total = totalExpenses(database);
console.log(`Total: ${total}`);
