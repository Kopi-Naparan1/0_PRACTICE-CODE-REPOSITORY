import json
import os

folder = os.path.join("C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course",
                      "3 Intermediate Concepts", "PROJECTS", "cache_files")


def build_menu():
    menu = {}

    while True:
        category = input('Add category or ("done" to finish): ').lower().strip()
        if category == 'done':
            break
        menu[category] = build_category(category)
    return menu


def build_category(category):
    items = {}

    while True:
        action = input(f'Add item to {category} or "sub" to make a sub category or "done" to finish: ')

        if action == 'done':
            break

        elif action == 'sub':
            sub_name = input("Input subcategory name: ")
            items[sub_name] = build_category(sub_name)

        else:
            price = int(input("Price: "))
            description = input("Description: ")
            items[action] = {"Price": price,
                             "Description": description,
                             }
        return items


def json_saver(menu: dict):
    name_new_file = input(f"Name your file: ")
    new_json_file = os.path.join(folder, f"{name_new_file}.json")

    with open(new_json_file, 'w') as file:
        json.dump(menu, file, indent=4)
        print('--- File is saved ---')


def main():
    menu = build_menu()
    json_saver(menu)



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")



# 70% written by AI, not passed