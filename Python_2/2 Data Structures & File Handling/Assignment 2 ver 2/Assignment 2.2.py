
def assignment1():

    def asks_contacts() -> dict:
        """Ask 3 contacts and return dict"""

        contacts = {}

        for i in range(1 ,4):
            name = input(f'[{i}] Input name : ')
            phone = input(f'[{i}] Input Phone #:  ')
            email = input(f'[{i}] Input Email: ')

            contacts[name] = {"Phone": phone,
                              "Email": email,
                              }

        return contacts if contacts else f'Something is wrong in ask_contacts...'

    def displays_contacts(contacts: dict) -> None:
        """Sole purpose is to display that dict"""
        print("--- CONTACTS' INFORMATION ---")

        for key, value in contacts.items():
            print(f"Name: {key}")
            print(f"Phone #: {value['Phone']}")
            print(f"Email: {value['Email']}")
            print('-' * 30)
        print('=' * 30)

    def searches_contact(contacts :dict) -> str:
        """Prompts a user to search a contact"""
        choice = input("Want to search a contact? (y/n): ")
        print(contacts)

        if choice.lower() == 'y':
            name = input("Input a name: ")
            return name
        elif choice.lower() == 'n':
            return 'n'

    def updates_email(contacts :dict, name :str) -> None:
        """After the contacts are displayed,
        user will be prompted, what should be the new email is"""

        new_email = input("New email: ")
        contacts[name] ={"Phone": contacts[name]["Phone"],
                          "Email": new_email,
                          }
        print(contacts[name])

    def display_a_contact(contacts: dict, name: str) -> None:
        """sole purpose is to display 1 specific contact. I separated 3 displays thing because that
        tends to be easier to debug, make, and think."""
        print(contacts[name])

    def assignment1_main():
        contact = asks_contacts()

        displays_contacts(contact)

        while True:
            name = searches_contact(contact)

            if name == 'n':
                print("1 Exiting...")
                break
            elif name:
                display_a_contact(contact, name)

            update = input('Want to update email? (y/n)')

            if update.lower() == 'y':
                updates_email(contact, name)
            elif update.lower() == 'n':
                print('2 Exiting...')
                break

    assignment1_main()

def assignment2():
    numbers = [num for num in range(1, 31)]
    print(numbers)

    even_odd = [f"Even" if num % 2 == 0 else "Odd" for num in range(1, 31)]
    print(even_odd)

    div3 = list((num, "divby3") for num in range(1, 31) if num % 3 == 0)

def assignment3():
    list_skills = []
    name = input("Name: ")
    age = int(input("Age: "))
    location = input('Location: ')

    while True:
        skills = input("Skills: ('quit' if done)")
        list_skills.append(skills)
        if skills.lower() == "quit":
            break
    profile = f"Hi I am {name}. {age} years old. My skills are/is {list_skills})"
    profile2 = "Hi I am {}. {} years old.I live in {} . My skills are/is {}".format(name, age, location, list_skills)
    print(profile)
    print(profile2)

def assignment4():
    with open("log.txt", 'w') as log_file:
        for i in range(1, 4):
            user_log = input(f'Log [{i}]: ')
            log_file.write(f"[{i}] {user_log}\n")

    with open("log.txt", 'r') as log_file:
        print(log_file.read())

def assignment5():
    def add_task() -> None:
        """When user input: 1, this will show"""

        with open("tasks.txt",'w') as file:
            i = 1
            print("q to quit adding task/s")

            while True:

                task = input(f"Task [{i}]:   ")
                if task.lower() == 'q':
                    break
                file.write(f"[{i}] {task}\n")
                i += 1


    def show_task() -> None:
        """Display current task, """
        with open('tasks.txt', 'r' ) as file:
            print('--- To-do list ---')
            print(file.read())
            print(f"{'-' * 30}\n")

    def main_assignment():

        while True:

            choice = input('[1] Add task/s \n'
                               '[2] See task/s\n'
                               '[3] quit\n'
                               'Input: ')
            if choice == "1":
                add_task()
            elif choice == "2":
                show_task()
            elif choice == "3":
                print('\n\tExiting to-do list program...')
                break

    main_assignment()

def assignment6():
    from datetime import datetime

    def ask_mood() -> None:
        print("'q' to quit")
        with open('mood.txt', 'w') as file:

            while True:
                now = datetime.now()
                mood = input(f'What is your mood right now ({now.strftime("%Y-%m-%d-%I-%p-%M")}):')
                file.write(f'{now.strftime("%Y-%m-%d-%I-%p-%M")}: {mood}\n')
                if mood.lower() == 'q':
                    break

    def display_mood() -> None:
        print('--- MOOD TRACKER ---')
        with open('mood.txt', 'r') as file:
            print(file.read())
            print('')


    def assignment6_main():
        ask_mood()
        display_mood()

    assignment6_main()

def assignment7():
    import csv

    # Step 1: Write to CSV
    people = [
        ["name", "skill", "age"],
        ["Alice", "Python", 22],
        ["Bob", "C++", 17],
        ["Charlie", "Design", 19],
        ["Dana", "Java", 16],
        ["Eve", "HTML", 20]
    ]

    with open("people.csv", 'w', newline='') as file:
        write = csv.writer(file)
        write.writerows(people)

    with open("people.csv", 'r') as file:
        read = csv.DictReader(file)
        for row in read:
            if int(row['age']) < 18:
                print(row['name'])

def assignment8():
    """The purpose of this assignment was to practice:
    1. function usage
    2. cleaner code
    3. practice error handling
    4. Make a basic calculator
    5. HIGHLIGHT OF NEW LEARNING: learned to use dictionary to make easier
    usage of functions"""

    def add() -> int:
        print('--- ADDITION ---')
        first = int(input("First number: "))
        second = int(input("Second number: "))

        result = first + second
        return result

    def subtract() -> int:
        print('--- SUBTRACTION ---')
        first = int(input("First number: "))
        second = int(input("Second number: "))

        result = first - second
        return result



    def multiply() -> int:
        print('--- MULTIPLICATION ---')
        first = int(input("First number: "))
        second = int(input("Second number: "))
        result = first * second
        return result


    def divide():
        print('--- DIVISION ---')
        try:
            first = int(input("First number: "))
            second = int(input("Second number: "))
            result = first / second
            return result
        except ZeroDivisionError:
            return 'Error'




    def assignment8_main():
        print('--- CALCULATOR ---')

        print('[1] Addition \n'
              '[2] Subtraction \n'
              '[3] Multiplication \n'
              '[4] Division \n'
              '[5] (quit the calculator)')



        print("")
        while True:

            functions = {1: add,
                         2: subtract,
                         3: multiply,
                         4: divide,
                         }
            operation = int(input('What operation to use?  '))

            if operation == 5:
                print('quitting the calculator...')
                break

            for key, value in functions.items():
                if operation == key:
                    print(f" = {value()}")

    assignment8_main()

def assignment9():
    """The purpose of this assignment is to improve my:
    1. file handling: writing and reading json
    2. dictionary handling
    3. Write cleaner, comprehensive code

    TASKS:
    1. Let user add unlimited contacts until user stops it
    2. save it to json
    3. read and display that json
    """

    import json

    def make_dictionary() -> dict:
        result = {}
        i = 1
        while True:
            print('')
            print('-' * 30)
            print(f"Contact {i}")
            name = input("Name: ").strip()
            email = input("Email: ").strip()

            try:
                phone = int(input("Phone #").strip())

            except ValueError:
                print(f'Invalid Phone #. Re-type again the contact [{i}]...')
                continue

            result[name] = {
                            "Email": email,
                            "Phone": phone,
                            }
            i += 1
            more = input('Add more contacts [y/n]? ').lower()

            if more == 'n':
                print('Quitting the adding of contacts...')
                break

        return result

    def write_json(data: dict)-> None:

        with open("Contact.json", 'w') as file:
            json.dump(data, file, indent=4)

    def view_json() -> None:
        print('--- Your Contacts---')
        with open("Contact.json", 'r') as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))

    def assignment9_main():
        """ To-do
        1. Search: How to format json, my problem is the printing of json is
        unorganized """

        print('--- Add Contacts---')
        data = make_dictionary()
        write_json(data)
        view_json()


    assignment9_main()

def assignment10():
    """Same purpose as assignment 9"""

    def ask_tasks() -> list[str]:
        tasks = []

        for i in range(1,4):
            task = input(f"Task [{i}]: ")
            tasks.append(f"[{i}] {task}")

        return tasks


    def write_text(tasks: list[str]) -> None:
        with open('Tasks.txt', 'w') as file:
            for task in tasks:
                file.write(task + '\n')

    def delete_line() -> None:
        remove = int(input('Which task number would you want to remove? '))

        with open("Tasks.txt", 'r') as file:
            lines = file.readlines()

        with open("Tasks.txt", 'w') as file:
            for line in lines:
                if not line.startswith(f"[{remove}]"):
                    file.write(line)


    def display_text() -> None:
        with open("Tasks.txt", 'r') as file:
            print('--- Tasks ---')
            for line in file:
                print(f"{line}", end='')

    def assignment10_main():
        """
        To-do list:
        1. None
        """

        tasks = ask_tasks()
        write_text(tasks)
        delete_line()
        display_text()
    assignment10_main()








def main():
    # assignment1()
    # assignment2()
    # assignment3()
    # assignment4()
    # assignment5()
    # assignment6()
    # assignment7()
    # assignment8()
    assignment9()
    # assignment10()



if __name__ == "__main__":
    main()
