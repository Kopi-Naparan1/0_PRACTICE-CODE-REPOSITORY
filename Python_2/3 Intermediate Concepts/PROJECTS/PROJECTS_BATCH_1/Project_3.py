import os


folder = os.path.join("C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course",
                      "3 Intermediate Concepts", "PROJECTS", "cache_files")


def food_categories() -> dict:
    categories = {
        "Food": {
            "Fruits": {
                "Citrus": {},
                "Berries": {}
            },
            "Vegetables": {}
        },
        "Drinks": {
            "Alcoholic": {},
            "Non-Alcoholic": {
                "Soda": {},
                "Juice": {}
            }
        }
    }

    return categories


def category_analyzer(data: dict, level=0) -> list[str]:
    list_data = []
    for key, value in data.items():
        indent = '    ' * level
        list_data.append(f'{indent}{key}')
        if isinstance(value, dict) and value:
            list_data.extend(category_analyzer(value, level + 1))
    print(list_data)
    return list_data


def text_saver(data: list[str]):
    name_new_file = input(f"Name your file: ")
    new_text_file = os.path.join(folder, f"{name_new_file}.txt")

    with open(new_text_file, 'w') as file:
        for line in data:
            file.write(line + '\n')
        print('File saved...')


def main():
    dictionary = food_categories()
    list_data = category_analyzer(dictionary)
    text_saver(list_data)


if __name__ == "__main__":
    main()