import csv
import os
import json

folder = os.path.join(
        "C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course",
        "2 Data Structures & File Handling", "PROJECTS 2", "Cache_files"
    )


def csv_loader():
    x = input('Search csv filename: ').strip()
    file_name = os.path.join(folder, f"{x}.csv")

    try:
        with open(file_name, 'r') as file:
            read = csv.DictReader(file)
            data = list(read)
            print('Data is loaded...')
            return data

    except FileNotFoundError:
        print('New File is made...')
        return []


def to_dict_format(dictionary: list[dict]) -> dict:
    dict_users = {}
    for i in dictionary:
        dict_users[i["name"]] = i
    return dict_users


def dict_cleaner(dictionary: dict) -> dict:
    cleaned_dict = {}
    for key, user_data in dictionary.items():
        cleaned_user = {}
        for k, v in user_data.items():
            if v == '':
                continue
            if k == 'age':
                if v.isdigit():
                    cleaned_user['age'] = int(v)
            else:
                cleaned_user[k] = v
        if cleaned_user:
            cleaned_dict[key] = cleaned_user
    return cleaned_dict


def json_saver(data):
    x = input('Name your json file: ')
    file_name = os.path.join(folder, f"{x}.json") if x else os.path.join(folder, "user.json")

    try:
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
            print('Tasks saved')

    except FileNotFoundError:
        print('FNF - Failed to save tasks')

    except json.JSONDecodeError:
        print('JSONDE - Failed to save tasks')


def main():
    list_users= csv_loader()
    dict_users = to_dict_format(list_users)
    cleaned_data = dict_cleaner(dict_users)
    json_saver(cleaned_data)


if __name__ == "__main__":
    main()
