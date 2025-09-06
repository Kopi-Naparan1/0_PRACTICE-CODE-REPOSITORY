import os
import json


folder = os.path.join("C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course",
                      "3 Intermediate Concepts", "PROJECTS", "cache_files")


def json_loader():
    search_file = input('Search a json file: ')
    file_path = os.path.join(folder, f"{search_file}.json")

    try:
        with open(file_path, 'r') as file:
            dictionary = json.load(file)
            print('File found...')
            return dictionary
    except FileNotFoundError as x:
        print(f'{x} - Try again')

    except json.JSONDecodeError as y:
        print(f'{y} - Try again')


def find_files(structure: dict, keyword: str, path=''):

    list_path = []

    for key, value in structure.items():
        current_path = os.path.join(path, key)

        if keyword in key.lower() and value is None:
            list_path.append(current_path)

        elif isinstance(value, dict):
            list_path.extend(find_files(value, keyword, current_path))
    return list_path


def txt_saver(data):
    name_new_file = input(f"Name your file: ")
    new_text_file = os.path.join(folder, f"{name_new_file}.txt")

    with open(new_text_file, 'w') as file:
        for line in data:
            file.write(line + '\n')
        print('File saved...')


def main():
    file_system = json_loader()
    search_keyword = input('Search a Keyword: ')
    list_path = find_files(file_system, search_keyword)
    txt_saver(list_path)


if __name__ == "__main__":
    main()
