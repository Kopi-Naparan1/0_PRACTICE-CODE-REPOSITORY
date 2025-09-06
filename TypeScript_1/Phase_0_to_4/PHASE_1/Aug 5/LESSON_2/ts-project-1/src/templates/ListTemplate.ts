import FullList from "../model/FullList";
import type ListItem from "../model/ListItem"; // This is the ID of the html

interface DOMlist {
  ul: HTMLUListElement;
  clear(): void;
  render(fullList: FullList): void;
}

export default class ListTemplate implements DOMlist {
  ul: HTMLUListElement;

  static instance: ListItem = new ListTemplate();

  private constructor() {
    this.ul = document.getElementById("listItems") as HTMLUListElement;
  }

  clear(): void {
    this.ul.innerHTML = "";
  }

  render(fullList: FullList): void {
    this.clear();

    fullList.list.forEach((item) => {
      const li = document.createElement("li") as HTMLLIElement;
      li.className = "item";

      const check = document.createElement("input") as HTMLInputElement;
      check.type = "checkbox";
      check.id = item.id;
      check.tabIndex = 0;
      check.checked = item.checked;
      li.append(check);

      check.addEventListener("change", () => {
        item.checked = !item.checked;
        fullList.save();
      });
      const label = document.createElement("label") as HTMLLabelElement;
      label.htmlFor = item.id;
      label.textContent = item.item;
      li.append(label);

      const button = document.createElement("button") as HTMLButtonElement;
      button.className = "buttom";
      button.textContent = "X";
      li.append(button);

      button.addEventListener("click", function () {
        fullList.removeItem(item.id);
        this.render(fullList);
      });

      this.ul.append(li);
    });
  }
}
