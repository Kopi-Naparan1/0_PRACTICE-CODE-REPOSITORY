import random
import json

file_name = "questions.json"


def random_questions() -> dict:

    questions = {
        1: {"question": "What is the best programming language?",
            'choices': {'a': 'C#',
                        'b': 'C++',
                        'c': 'C',
                        'd': 'python',
                        },
            'answer': 'd'},
        2: {"question": "What is the best country?",
            'choices': {'a': 'Philippines',
                        'b': 'USA',
                        'c': 'UK',
                        'd': 'China',
                        },
            'answer': 'b'},
        3: {"question": "What is the best fruit?",
            'choices': {'a': 'Mango',
                        'b': 'Apple',
                        'c': 'Durian',
                        'd': 'Orange',
                        },
            'answer': 'd'},
        4: {"question": "What is the best snack?",
            'choices': {'a': 'Hamburger',
                        'b': 'Pizza',
                        'c': 'Spaghetti',
                        'd': 'Sandwich',
                        },
            'answer': 'd'},
        5: {"question": "What is the best money?",
            'choices': {'a': '$1',
                        'b': '$10',
                        'c': '$100',
                        'd': '$1M',
                        },
            'answer': 'd'},
        6: {"question": "What is the best color?",
            'choices': {'a': 'Blue',
                        'b': 'White',
                        'c': 'Black',
                        'd': 'Orange',
                        },
            'answer': 'a'},
        7: {"question": "What is the best brand?",
            'choices': {'a': 'Nike',
                        'b': 'Adidas',
                        'c': 'Windows',
                        'd': 'Apple',
                        },
            'answer': 'c'},

        8: {"question": "What is the best number?",
            'choices': {'a': '5',
                        'b': '6',
                        'c': '7',
                        'd': '8',
                        },
            'answer': 'c'},

    }

    return questions


def save_json():
    with open(file_name, 'w') as f:
        json.dump(random_questions(), f, indent=4)


def load_json():
    with open(file_name, 'r') as f:
        questions = json.load(f)
        return questions





