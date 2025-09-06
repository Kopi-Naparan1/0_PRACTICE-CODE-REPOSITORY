

#  region - first
def ask_age() -> int:

    age = int(input("How old are you? "))
    return age


def check_age(age) -> bool:
    if age < 18:
        print(f'{age}. Minor. Not allowed')
        return False
    elif age < 65:
        print(f'{age} Adult. You are allowed')
        return True
    elif age >= 65:
        print(f'{age}. Old. Not allowed')
        return False
    else:
        print("I don't know! Leave!")
        return False


def ask_name() -> str:
    name = str(input('What is your name? ')).lower()
    return name


def ask_color() -> str:
    favorite_color = str(input("What is your favorite color? ")).lower()
    return favorite_color


def ask_hobbies() -> list[str]:
    three_hobbies = []

    for i in range(1, 4):
        hobby = input(f'Hobby [{i}]:').lower()
        three_hobbies.append(hobby)

    return three_hobbies


def display_original_profile(name, age, color, hobbies) -> dict:
    print('-' * 30)
    print('---PROFILE---')
    print(f'Fullname: {name.title()}')
    print(f'Age: {age}')
    print(f'Favorite color: {color}')
    print(f'Hobbies:')

    i = 1
    for hobby in hobbies:
        print(f"\t- [{i}] {hobby}")
        i += 1

    print('-' * 30)

    return {"name": name,
            "age": age,
            "color": color,
            'hobbies': [hobby for hobby in hobbies],
            }
# endregion

# region - updating


def update_name(information: dict) -> str:
    old_name = input('Name of the user: ').lower()

    if old_name in information:
        new_name = information[old_name] = input('New name: ').lower()
        print(f'{old_name} is updated to {new_name}')
        return new_name
    else:
        print(f'{old_name} not found...')


def update_age(information):
    name = input('Name of the user: ').lower()

    if name in information:
        old_age = information[name]['age']
        new_age = input('New age: ')
        x = information[name]['age'] = new_age
        print(f'{old_age} is updated to {new_age}')
        return x
    else:
        print(f'{name} not found...')


def update_color(information):
    name = input('Name of the user: ').lower()

    if name in information:
        old_color = information[name]['color']
        new_color = information[name]['color'] = input('New color: ')
        print(f'{old_color} is updated to {new_color}')
        return new_color
    else:
        print(f'{name} not found...')


def update_hobbies(information):

    """Get the name of the user so that I can use to get the key of the dictionary,
    print's out the dictionary, let user choose a hobby, then let the user change it.
    Then ask the user if he wants to change again."""
    name = input('Name of the user: ').lower()

    if name in information:
        while True:

            print('--- Choose a hobby---')
            i = 1
            hobbies = information[name]['hobbies']
            for hobby in hobbies:
                print(f'[{i}] {hobby}')
                i += 1

            choice = int(input('Input a number to change it: '))

            if choice.is_integer():
                old_hobby = hobbies[choice-1]
                new_hobby = input('New hobby:')
                hobbies[choice-1] = new_hobby
                print(f'{old_hobby} is updated to {new_hobby}')

            change_more = input('Want to change more? [y/n]')
            if change_more == 'n':
                return
            else:
                pass

    else:
        print(f'{name} not found...')


def display_updated_info(information: dict):
    for name in information:
        print(f'Name: {name}')
        for k, v in information[name].items():
            print(f'{k} {v}')


def helper_main(information) -> None:
    while True:
        choice = input('Choose a number (q to quit...): ')

        helper_functions = {1: update_name,
                            2: update_color,
                            3: update_hobbies,
                            4: update_age}
        choice = int(choice)
        if choice in [x for x in range(1,5)]:
            for k, v in helper_functions.items():
                if k == choice:
                    v(information)
                    update_information(information)
                else:
                    pass
        elif choice == 'q':
            print('quiting...')
            return

        else:
            print(f'Make sure you choose from 1 to {len(helper_functions.keys())}')


def update_information(information:dict) -> None:
    print('\n--- CHOOSE --- \n')

    i = 1
    for name in information:
        print(f'{i} {name} ')
        for k, v in information[name].items():
            print(f"{i+1} {k}: {v}")
            i += 1
    print('-' * 30)
# endregion


def main():
    """This assignment is called adulthood profile creator.
     The aim of this program is to ask user about age, name, fav_color, 3 hobbies.
     If user is not 18 years old, and older than 65, it will return false ano not
     let the user get into the next line of questions.
     After that, it will prompt to let the user change the info"""

    print('=' * 35)
    print('Welcome to the Adulthood Profile Creator')
    print('=' * 35)

    information = {}

    age = ask_age()
    allowed = check_age(age)

    if allowed:

        name = ask_name()
        color = ask_color()
        hobbies = ask_hobbies()
        age = age

        information[name] = {
                            "color": color,
                            "hobbies": [hobby for hobby in hobbies],
                            "age": age,
                            }

        display_original_profile(name, age, color, hobbies)

    elif not allowed:
        return

    while True:
        change = input('Do you want to change your information? (y/n)').lower()
        if change == 'y':
            update_information(information)
            helper_main(information)
            display_updated_info(information)
            break

        elif change == 'n':
            print('--- Quitting.... ---')


def notes_to_self():
    print("""Hi, so, this is like done for the assignment purposes, this is the first revision
    for the sunday review. (may25, 2025) What I've done was to organize everything and made it readable as possible.
    TO DO ON THE NEXT REVIEW:
    1. error handling
    2. More comments if possible
    3. try incorporating OOP if possible. (I applied what I've learned now about lots of things. It is worth doing it
        again)
    4. As much as possible, never AI something, maybe if you forgot how to do something that's fine. But refrain from it.
    5. Make the UI better. Make it user friendly.
    6. If you can code it shorter, that would be better.""")



if __name__ == "__main__":
    main()
