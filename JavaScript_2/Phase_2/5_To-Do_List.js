function add(tasks) {
  const task = prompt("What do you need to do? ");
  tasks.push(task);
  console.log(`Task: ${task} is added.`);
}

function remove(tasks) {
  const taskNumber = Number(prompt("Input a task number to remove: "));
  if (taskNumber > tasks.length) {
    console.log(`You may input number from 1 to ${tasks.length}`);
    return;
  }

  if (tasks.length === 0) {
    console.log("There are no available tasks yet.");
    return;
  }

  if (taskNumber >= 1 && taskNumber <= tasks.length) {
    tasks.splice(taskNumber - 1, 1);
    console.log("Task is removed");
  } else {
    console.log(`You may input number from 1 to ${tasks.length}`);
  }
}

function view(tasks) {
  if (tasks.length === 0) {
    console.log("No available tasks");
  }

  for (let i = 0; i < tasks.length; i++) {
    console.log(`[${i + 1}] ${tasks[i]}`);
  }
}

const menu = {
  1: add,
  2: remove,
  3: view,
};

function main() {
  console.log("Welcome to To-Do List");

  console.log(`
    [1] Add
    [2] Remove
    [3] View`);

  let tasks = [];

  let isOn = true;

  while (isOn) {
    const choice = Number(prompt("Choose a Number: "));

    if (isNaN(choice) && !(choice in menu)) {
      console.log("You may input number from 1 to 3");
      isOn = false;
    } else {
      menu[choice](tasks);
    }
  }
}

main();
