const input = document.getElementById("todoInput");
const addBtn = document.getElementById("addBtn");
const list = document.getElementById("todoList");

addBtn.addEventListener("click", function () {
  const task = input.value.trim();
  if (task === "") return;

  //1. Create List item - invisible
  const li = document.createElement("li");
  li.textContent = task;

  //2. Add a remove button - invisible
  const removeBtn = document.createElement("button");
  removeBtn.textContent = "Remove";
  removeBtn.classList.add("remove");

  //3. Handle removal
  removeBtn.addEventListener("click", function () {
    list.removeChild(li);
  });

  //4. Append button to li, and li to ul
  li.appendChild(removeBtn);
  list.appendChild(li);

  //5. Clear input
  input.value = "";
});
