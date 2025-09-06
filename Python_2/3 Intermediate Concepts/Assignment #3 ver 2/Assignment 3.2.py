# Start 10:32 pm , May 20, 2025
import json
from functools import reduce


def assignment1():
    def flexible_calculator(*args, **kwargs):

        for operation in kwargs.values():
            for arg in args:
                if operation == "+":
                    equals = sum(args)
                    return equals
                elif operation == "-":
                    equals = reduce(lambda x,y: x - y, args)
                    return equals
                elif operation == "*":
                    result = reduce(lambda x, y: x * y, args)
                    return result
                elif operation ==  "/" and any(False for arg in args if arg == 0):
                    return f'Error'
                elif operation == "/":
                    result = reduce(lambda x, y : x / y, args)
                    return result

    print(flexible_calculator(5,5, operation = "/"))

def assignment2():
    """The idea is to practice using local, nonlocal, global"""
    score = 0
    print(f"Initial: {score}")

    def game1():
        nonlocal score
        score = 10
        print(f'Game 1: {score}')
        def game2():
            nonlocal score
            # nonlocal score -> Why this doesnt work when I uncomment this
            score = 20
            print(f'Game 2: {score}')
        game2()
        # print(f"Set 1: {score}")
    game1()
    print(f"Last score: {score}")

def assignment3():
    """Lambda. To sort student based on grades, and assign grades"""

    names = ["Ana", "Brad", "Colt", "Dexter", "Elliot"]
    grades = [90, 100, 80, 60, 70]

    # Zip grades together
    students = list(zip(names, grades))

    # Sort students by their grades
    sort = list(sorted(students, key=lambda x: x[1], reverse=True ))

    # Assign their letter grades
    letter = ["A", "B", "C", 'D', 'E']

    student_final_grades = [(name, grade, letter[i]) for i, (name, grade) in enumerate(sort)]

    print(student_final_grades)

def assignment4():
    names = ['Kopi',"Alice",'Bob','Ann']
    lowercase_name = list(map(lambda x: x.strip().lower(), names))
    print(lowercase_name)

    no_to_3 = list(filter(lambda x: len(x) > 3, lowercase_name))
    print(no_to_3)

    into_1 = reduce(lambda x, y: x + y,no_to_3 )
    print(into_1)

def assignment5():
    from math_utility import add as a
    print(a(50,50,5))

def assignment6():
    import datetime
    import random
    import os

    def current_date():
        today = datetime.date.today()
        return today

    def random_prompt() ->str:
        prompt = [
            "How are you? :",
            "Hello, what's up? ",
            "What's great about your day? ",
            "Come on, why you're so good today? ",
            "I know you're happy. Tell be more about it: ",
        ]
        question = random.choice(prompt)
        return question

    def ask_journal(prompt, date, dictionary) -> dict:
        journal = dictionary
        answer = input(prompt())
        mood = input('Happiness (1 - 10): ')

        journal[f"{date()}"] = {"Mood": mood,
                                "Entry": answer,
                                }
        return journal

    def file_path() ->str:
        folder = 'Journal Entry'
        file_name = 'Journal.json'

        os.makedirs(folder, exist_ok=True)
        file_path_to_use = os.path.join(folder, file_name)
        return file_path_to_use

    def save_json(data: dict, path):

        with open(path(), 'a') as file:
            json.dump(data, file, indent=4)
            print('--- DAILY JOURNAL SAVED---')

    def load_json(path) -> dict:
        try:
            if os.path.exists(path()):
                with open(path(), 'r') as file:
                    read = json.load(file)
                    return read
        except FileNotFoundError:
            return {}

        except json.JSONDecodeError:
            return {}

    def daily_journal_logger_main():
        """
        There's a problem on saving the journal inside the json file. Fix it.

        :return:
        """
        print("----- Daily Journal Entry-----")
        dictionary = load_json(file_path)

        data = ask_journal(random_prompt, current_date, dictionary)

        save_json(data, file_path)



    daily_journal_logger_main()







def main():
    # assignment1()
    # assignment2()
    # assignment3()
    # assignment4()
    # assignment5()
    assignment6()






if __name__ == "__main__":
    main()