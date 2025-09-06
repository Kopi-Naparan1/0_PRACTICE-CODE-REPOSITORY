import json


def capitalize_name(file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)

            for user in data:
                user['name'] = user['name'].title()

        with open(file, 'w') as f:
            json.dump(data, f, indent=4)

    except json.JSONDecodeError as x:
        print(f'Error: {x}')

    except FileNotFoundError as y:
        print(f'Error: {y}')

    print(f'--- DONE CAPITALIZING NAMES ---\n')


def remove_inactive_users(file) -> dict:
    try:
        status = {
            "Active users": 0,
            "Removed users": 0,
        }

        with open(file, 'r') as f:
            data = json.load(f)

            new_data = [user for user in data if user["is_active"]]

        status["Active users"] = len(new_data)
        status["Removed users"] = len(data) - len(new_data)


        with open(file, 'w') as f:
            json.dump(new_data, f, indent=4)

        print(f'--- DONE REMOVING INACTIVE USERS---')
        return status
    except FileNotFoundError as x:
        print(f'Error: {x}')
        return {}

    except json.JSONDecodeError as y:
        print(f'Error: {y}')
        return {}


def lowercase_email(file):
    with open(file, 'r') as f:
        data = json.load(f)

        for user in data:
            user['email'] = user['email'].lower()

    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

    print(f'--- DONE LOWERCASING EMAILS ---\n')
