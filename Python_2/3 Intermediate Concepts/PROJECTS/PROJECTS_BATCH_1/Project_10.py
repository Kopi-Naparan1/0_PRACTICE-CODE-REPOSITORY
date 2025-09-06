import os
import json
from typing import List, Dict
import copy
from collections import defaultdict

folder = os.path.join("C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course",
                      "3 Intermediate Concepts", "PROJECTS", "cache_files")


def file_name_searcher() -> List[str]:
    print('Batch Search json files')
    file_names = []

    while True:
        file_name = input('Search a file name ("s" to search): ').strip()
        if file_name == 's':
            break
        file_names.append(file_name)

    return file_names


def transaction_data_loader(*filenames) -> List[Dict]:
    transactions = []

    for filename in filenames:
        file_path = os.path.join(folder, f'{filename}.json')

        try:
            with open(file_path, 'r') as file:
                transaction = json.load(file)
                transactions.extend(transaction)
                print(f'- File: {filename}.json found')

        except FileNotFoundError:
            print(f'- File: {filename} not found')

        except json.JSONDecodeError:
            print(f'- File: {filename}.json Json Decode Error ')

    return transactions


def user_filter_choice():
    products_exceed_budget = int(input("Products that exceed what amount? $ "))
    print("Tags: food, fastfood, transport, commute, snacks, health, personal, school, supplies, "
          "electronics, home, entertainment, utilities, groceries,delivery")
    products_with_tag = input('Search products with a tag: ')

    try:
        products_about_amount = int(input("Products above what amount: $"))
    except ValueError:
        print('Error: 0 was registered due to some error. ')
        products_about_amount = 0

    return products_exceed_budget, products_with_tag, products_about_amount


def filter_transaction_data(transaction_data: List[Dict], products_exceed_budget=0, tag=None, products_above_amount=0):
    valid_transaction_data = list(
        filter(lambda transaction: transaction['name'] and int(transaction['amount']) and list(transaction['tags']),
               transaction_data))

    highest_transaction = max(valid_transaction_data, key=lambda x: x['amount'])

    tags_usage_times = defaultdict(int)

    for data in valid_transaction_data:
        tags = data.get('tags', [])
        for tag in tags:
            tags_usage_times[tag] += 1

    products_exceeded = []
    if products_exceed_budget > 0:
        products_exceeded.extend(list(
            filter(lambda transaction: int(transaction['amount']) > products_exceed_budget, valid_transaction_data)))

    products_with_tag = []
    if tag is not None:
        for valid_transaction in valid_transaction_data:
            if tag in valid_transaction['tags']:
                products_with_tag.append(valid_transaction)

    products_above_that_amount = []
    if products_above_amount > 0:
        products_above_that_amount.extend(list(
            filter(lambda transaction: int(transaction['amount']) > products_above_amount, valid_transaction_data)))

    return highest_transaction, tags_usage_times, products_exceeded, products_with_tag, products_above_that_amount


def summarizer(highest_transaction: dict, tags_usage_times: dict, products_exceeded: List[dict],
               products_with_tag: List[dict], products_above_that_amount: List[dict],
               exceed_budget, product_tag, above_amount):
    tags_usage_times_line = [f"{key} : {value}" for key, value in tags_usage_times.items()]
    tags_usage_times_summary = '\n'.join(tags_usage_times_line)

    products_exceeded_line = [f"{key['name']} : {key['amount']}" for key in products_exceeded]
    products_exceeded_summary = '\n'.join(products_exceeded_line)

    products_with_tag_line = [f"{key['name']} : {key['amount']}" for key in products_with_tag]
    products_with_tag_summary = '\n'.join(products_with_tag_line)

    products_above_that_amount_line = [f"{key['name']} : {key['amount']}" for key in products_above_that_amount]
    products_above_that_amount_summary = '\n'.join(products_above_that_amount_line)

    summary = (f"===== SUMMARY =====\n"
               f"HIGHEST TRANSACTION: {highest_transaction['name']} : {highest_transaction['amount']}\n\n"
               f"---TAGS USAGE---: \n\n"
               f"{tags_usage_times_summary}"
               f"\n\n\n"
               f"---TRANSACTIONS EXCEEDED ${exceed_budget}---:\n\n"
               f"{products_exceeded_summary}"
               f"\n\n\n"
               f"---TRANSACTIONS WITH [{product_tag}] TAG---:\n\n"
               f"{products_with_tag_summary}"
               f"\n\n\n"
               f"---TRANSACTIONS ABOVE ${above_amount}: \n\n"
               f"{products_above_that_amount_summary}\n"
               f"======================")

    return summary


def data_into_dictionary(highest_transaction: dict, tags_usage_times: List[dict], products_exceeded: List[dict],
                         products_with_tag: List[dict], products_above_that_amount: List[dict],
                         exceed_budget, product_tag, above_amount):
    summary = {
        "Highest Transaction": highest_transaction,
        "Tags Usage Times": tags_usage_times,
        f"Transaction/s Exceeded ${exceed_budget}": products_exceeded,
        f'Transaction/s with Tag [{product_tag}]': products_with_tag,
        f'Transaction/s Above ${above_amount}': products_above_that_amount
    }

    return summary


def save_txt_json(txt, dict):
    print('Incase of any errors, the file will be saved as .txt as default')
    file_type = input('Save as .txt [1] or .json [2]')
    file_name = input('Input new file name: ')

    if file_type == '2':
        file_path = os.path.join(folder, f"{file_name}.json")
        with open(file_path, 'w') as file:
            json.dump(dict, file, indent=4)
            print(f'{file_name}.json saved successfully')
    else:
        file_path = os.path.join(folder, f"{file_name}.txt")
        with open(file_path, 'w') as file:
            file.write(txt)
            print(f'{file_name}.txt saved successfully')


def main():
    file_names = file_name_searcher()
    transaction_data = transaction_data_loader(*file_names)
    transaction_data_copy = copy.deepcopy(transaction_data)
    exceed_budget, product_tag, above_amount = user_filter_choice()

    highest_transaction, tags_usage_times, products_exceeded, products_with_tag, products_above_that_amount = filter_transaction_data(
        transaction_data_copy, products_exceed_budget=exceed_budget, tag=product_tag,
        products_above_amount=above_amount)
    summary_string = summarizer(highest_transaction, tags_usage_times, products_exceeded, products_with_tag,
                                products_above_that_amount, exceed_budget, product_tag, above_amount)
    summary_dictionary = data_into_dictionary(highest_transaction, tags_usage_times, products_exceeded,
                                              products_with_tag,
                                              products_above_that_amount, exceed_budget, product_tag, above_amount)

    print(summary_string)
    choice = input('"S" to save data: ').lower()
    if choice == 's':
        save_txt_json(summary_string, summary_dictionary)
    else:
        print('BYE')


if __name__ == "__main__":
    main()
