#Start: 2:54 pm
import json


def adding_contacts(data) ->None:
    """
    1. Ask for info until user quit
    """

    print('--- ADDING A CONTACT---\n')

    i = 1
    while True:
        print(f'--- Contact [{i}] ---')

        name = input('Name: ').lower()
        email = input('Email: ').lower()
        phone = input("Phone #: ")
        city = input("City: ").lower()
        data[name] = {"Email": email,
                      "Phone #": phone,
                      "City": city,
                      }
        print(f'Contact [{i}] Saved')
        i += 1
        quitting = input('"q" to quit. (Any keys) to continue: ').lower()

        if quitting == 'q':
            break

def display_data(data: dict) -> None:
    """Sole purpose is to show data"""

    print(f"{'-' * 30}")
    i = 1
    for key, value in data.items():
        print(f"--- Contact {i}---")
        print(f'Name: {key}')
        for k, v in value.items():
            print(f'{k}: {v}')
        print(f"{'-' * 30}")
        i += 1

def updating_contacts(data: dict) -> None:
    """
    1. Display data
    2. Ask user a name (key)
    3. update depending on numbers 1-3 which corresponds to what to info to change
    4. exit
    """


    print('--- UPDATING A CONTACT---\n')

    if data == {}:
        print('--- Empty ---\n\n')
        return
    else:
        display_data(data)

    name = input('Contact Name: ').lower()

    if name in data:
        contact = data[name]
        print(f"--- Contact Information of {name}---")
        print(f'\t\t--- {contact} ---\n')

    functions = {1: "Email",
                 2: "Phone #",
                 3: "City",
                 }
    for key, value in functions.items():
        print(f'[{key}] : {value}')

    while True:
        try:
            update = int(input('Choose what to update: '))
            if update in functions:
                to_update = functions[update]  # It is connected to the function dict, making code short
                s = input(f"New {to_update}: ")
                data[name][to_update] = s
                print(f'{s} saved')
                print('-' * 30)
                return
            else:
                print('Enter a number...')
        except ValueError:
            print('Enter a number!')

def searching_contacts(data):
    choice = input('Search a city/name: ').lower()

    search = [name for name, info in data.items()
              if choice in name or any(choice in value for value in info.values())]
    print('Results: ')
    for x in search:
        print(f'\t{x}')

def save_contacts(data: dict):
    with open('Contacts.json', 'w') as file:
        json.dump(data, file, indent=4)
        print('--- CONTACTS ARE SAVED ---')

def load_contacts():
    try:
        with open('Contacts.json', 'r') as file:
            read = json.load(file)
            return read
    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        return {}

def main():
    contact_data = load_contacts()

    functions = {"1": adding_contacts,
                "2": updating_contacts,
                "3": searching_contacts,
                "4": save_contacts
                 }
    try:
        while True:
            print(f"[1] Add Contacts \n"
                  f"[2] Update Contact \n"
                  f"[3] Search Contact \n"
                  f"[4] Save then quit")

            choice = input("Choose: ")
            if choice == '4':
                functions[choice](contact_data)
                break
            elif choice in functions:
                functions[choice](contact_data)
            else:
                print('Invalid...')
    finally:
        print('\nGoodbye...')

















if __name__ == "__main__":
    main()


