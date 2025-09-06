import json
import os
import copy
from collections import defaultdict
from typing import List, Dict
import textwrap

folder = os.path.join("C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course",
                      "3 Intermediate Concepts", "PROJECTS", "cache_files")


def json_searcher() -> List[str]:
    """Required for getting the filenames of the json datas that will be used
    to the data loader - Using the strings as the filenames"""
    list_valid_json = []

    while True:
        search_file = input('Search File_name ("done" to process datas): ')
        if search_file == 'done':
            break

        else:
            file_path = os.path.join(folder, f"{search_file}.json")
            list_valid_json.append(file_path)
    return list_valid_json


def data_loader(*filepaths):
    """Accepts those filenames: strings. And use those filenames
    in this loop so that no matter how many filenames this function accepts, it will be loaded"""
    list_valid_expenditures = []
    i = 1
    for file_path in filepaths:
        try:
            with open(file_path, 'r') as file:
                list_of_dictionary = json.load(file)
                print(f'--File {i} Found--')
                list_valid_expenditures.extend(list_of_dictionary)
                i += 1
        except FileNotFoundError:
            print(f"-- File {i} not found: Try again..--")
            i += 1
    return list_valid_expenditures


def clean_expenses(expenses, lowercase=True, minimum_amount=0) -> List[Dict]:
    """Required for cleaning the data: no empty values, and must be >= to the minimum_amount set"""
    valid_expenses = []

    for expense in expenses:  # This acts as a filter for empty values, expenses below minimum and, lowercaser
        if not all(expense.values()):
            continue

        try:
            amount = int(expense['amount'])
        except (ValueError, TypeError):
            continue

        if int(expense['amount']) < minimum_amount:
            continue

        if lowercase:
            expenses = map(expense["category"].lower(), expenses)
        valid_expenses.append(expense)

    return valid_expenses


def data_analyzer(clean_data: List[Dict]):
    """In order to get the final amount of each category and overall."""
    if not clean_data:
        return {}, 0, {}

    highest_amount = max(clean_data, key=lambda x: x["amount"])
    total_spent = 0
    categories = defaultdict(int)

    for expense in clean_data:  # This gets overall expenses each category
        category = expense["category"]
        amount = expense["amount"]
        categories[category] += amount
        total_spent += amount

    return highest_amount, total_spent, categories


def data_summarizer(highest_amount: dict, total_spent: int, categories: dict) -> str:
    """Formats a clean and simple summary of the expenses."""

    category_lines = [f"{k.lower():<15}: ${v}" for k, v in categories.items()]
    category_summary = '\n'.join(category_lines)

    # Build the entire string without multiline indentation
    summary = (
        f"Highest Purchase : ${highest_amount['amount']} on {highest_amount['category'].lower()}\n\n"
        f"Notes            : {highest_amount['notes'] if highest_amount['notes'] else 'None'}\n\n"
        f"Total Spent      : ${total_spent}\n\n"
        f"Category Breakdown:\n"
        f"{category_summary}"
    )

    return summary



def txt_saver(data):

    file_name = input('Name your file: ')
    file_path = os.path.join(folder, f"{file_name}.txt")
    with open(file_path, 'w') as file:
        file.write(data)
        print('File is saved successfully')


def main():
    json_files = json_searcher()

    copied_data = copy.deepcopy(json_files)

    valid_expenditures = data_loader(*copied_data)

    clean_data = clean_expenses(valid_expenditures)

    highest_amount, total_spent, categories = data_analyzer(clean_data)

    summary = data_summarizer(highest_amount, total_spent, categories)

    txt_saver(summary)


if __name__ == "__main__":
    main()
