import ListItem from "../model/ListItem"; // Filter out item data to have an expected value.

interface List {
  list: ListItem[]; // Read 1
  load(): void; // Create 2
  save(): void; // Create 3
  clearList(): void; // Delete 4
  addItem(itemObj: ListItem): void; // Create 5
  removeItem(id: string): void; // Delete 6
}

export default class FullList implements List {
  static instance: FullList = new FullList();

  private constructor(private _list: ListItem[] = []) {} // 1

  get list(): ListItem[] {
    return this._list;
  }

  load(): void {
    const storedList: string | null = localStorage.getItem("myList"); // retrieve the persistent local storage
    if (typeof storedList !== "string") return;

    const parsedList: {
      _id: string;
      _item: string;
      _checked: boolean;
    }[] = JSON.parse(storedList); // extract the JSON data saved locally

    // For each object in the array of the parsed JSON, you assign the values into the new instance object.
    parsedList.forEach((itemObj) => {
      const newListITem = new ListItem(
        itemObj._id,
        itemObj._item,
        itemObj._checked
      );
      FullList.instance.addItem(newListITem);
    });
  }

  save(): void {
    localStorage.setItem("myList", JSON.stringify(this._list)); // save the data as JSON locally so it persist
  }

  clearList(): void {
    this._list = []; // clears out the list
    this.save(); // saved the empty list
  }

  addItem(itemObj: ListItem): void {
    this._list.push(itemObj);
  }

  removeItem(id: string): void {
    this._list = this._list.filter((item) => item.id !== id); // removes the IDs that arent passed
    this.save();
  }
}
