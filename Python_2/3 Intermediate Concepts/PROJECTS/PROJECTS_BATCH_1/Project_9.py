import os
import json
import copy
from typing import List, Dict
from collections import defaultdict

folder = os.path.join("C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course",
                      "3 Intermediate Concepts", "PROJECTS", "cache_files")


def file_name_searcher() -> List[str]:
    """Searches json filenames.
    If user is done, [filenames] -> json loader"""
    print('--- Batch Search Files ---')
    i = 1
    file_names = []
    while True:
        file_name = input(f'Search a json file {i} ("d" to search): ')

        if file_name == 'd':
            print('Searching files...')
            break
        file_names.append(file_name)
        i += 1

    return file_names


def json_loader(*filenames: List[str]) -> List[Dict]:
    """Tries to find and load the filenames.
    If found, extended to the warehouse data.
    If not, not included
    If all are loaded, it is appended"""

    warehouse_data = []

    for filename in filenames:
        file_path = os.path.join(folder, f"{filename}.json")

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                warehouse_data.extend(data)
                print(f'--File [{filename}.json] is FOUND--.')

        except FileNotFoundError:
            print(f'--Error: [{filename}.json] is not found--.')

        except json.JSONDecodeError:
            print(f'--Error: [{filename}.json] is not decoded successfully.--')

    return warehouse_data


def data_cleaner(warehouse_data: List[Dict]) -> List[Dict]:
    """This cleans any stock that has: empty name, stock, and price"""

    clean_warehouse_data = list(filter(lambda data: data['name'] and data['stock'] and data['price'], warehouse_data))
    return clean_warehouse_data


def ask_user_filter_options():
    print('Filter Product Search')
    under_price = input('Below what price range? $')

    print('Tags: electronics, furniture, office, stationery, school, paper, accessory')
    what_tag = input("What is the tag: ")
    stock_below = input('Below what available stocks? ')

    return int(under_price), what_tag, int(stock_below)


def data_analyzer(valid_data: List[Dict], under_price=0, with_tags=None, stock_below=0):
    """This analyzes the valid data and make sense out if it so that it will be used for saving.
    This function will analyze for: how many times a tag is used, most expensive item,
                                    products with less than 5 stocks, and some filtering of the user such as:
                                    products under a certain price, product with tags, and products below certain stocks
                                    """

    if not valid_data:
        return {}, {}, [], [], [], []

    tags_usage = defaultdict(int)
    most_expensive_item = max(valid_data, key=lambda item: item['price'])
    less_than_5_stock = list(filter(lambda item: item['stock'] < 5, valid_data))
    products_under_price_range = list(filter(lambda item: item['price'] < under_price, valid_data))
    products_below_stocks = list(filter(lambda item: item['stock'] < stock_below, valid_data))
    products_with_the_tag = []

    for data in valid_data:
        for d in data.get('tags', []):
            tags_usage[d] += 1  # For counting how many times tags are used

        if with_tags in data.get('tags', []):  # For the products with that tag
            products_with_the_tag.append(data)

    return (tags_usage, most_expensive_item, less_than_5_stock, products_under_price_range,
            products_below_stocks, products_with_the_tag)


def analyzed_data_into_dictionary(tags_usage: dict, most_expensive_item: dict, less_than_5_stock: list,
                                  products_under_price_range: list, products_below_stocks: list,
                                  products_with_the_tag: list, under_price: int, what_tag: str,
                                  stock_below: int) -> dict:

    summary = {"Currency": "USD or $",
               "Tags Usage": tags_usage,
               "Most expensive Item": most_expensive_item,
               "Items with less than 5 stocks": less_than_5_stock,
               f"Products Under ${under_price}": products_under_price_range,
               f"Product with tag/s [{what_tag}]": products_with_the_tag,
               f"Product Under {stock_below} available stocks": products_below_stocks}

    return summary


def analyzed_data_into_string(tags_usage: dict, most_expensive_item: dict, less_than_5_stock: list,
                              products_under_price_range: list, products_below_stocks: list,
                              products_with_the_tag: list,
                              under_price: int, what_tag: str, stock_below: int) -> str:

    tags_usage_line = [f"____-{key}: {value} times"for key, value in tags_usage.items()]
    tags_usage_summary = '\n'.join(tags_usage_line)

    less_than_5_stock_line = [f"____-{stock['name']}" for stock in less_than_5_stock]
    less_than_5_stock_summary = '\n'.join(less_than_5_stock_line)

    products_under_price_range_list_line = [f"____-{stock['name']}: ${stock['price']}" for stock in products_under_price_range]
    products_under_price_range_summary = '\n'.join(products_under_price_range_list_line)

    products_below_stocks_line = [f"____-{stock['name']}: {stock['stock']} stock/s" for stock in products_below_stocks]
    products_below_stocks_line_summary = '\n'.join(products_below_stocks_line)

    products_with_the_tag_line = [f"____-{stock['name']}: ${stock['price']}" for stock in products_with_the_tag]
    products_with_the_tag_line_summary = '\n'.join(products_with_the_tag_line)

    summary = f"""\n
    
    ==================================
    SUMMARY
    
    \nMOST EXPENSIVE ITEM:\n
    {most_expensive_item['name']} : ${most_expensive_item['price']}
    
    \nTAGS USAGE SUMMARY:\n
    {tags_usage_summary}
    
    \nPRODUCTS WITH <5 STOCKS SUMMARY:\n
    {less_than_5_stock_summary}
      
    \nPRODUCTS UNDER ${under_price}: \n
    {products_under_price_range_summary}
    
    \nPRODUCTS UNDER {stock_below} AVAILABLE STOCK/S:\n
    {products_below_stocks_line_summary}
    
    \nPRODUCTS WITH TAG: {what_tag}:\n
    {products_with_the_tag_line_summary}
    \n
    ================================
    """

    return summary


def save_to_txt_or_json(summary_dictionary, summary_text):
    file_name = input('Name your file: ')
    file_type = input('txt or json (default: .txt if any error will happen)')

    if file_type == 'json':
        file_path = os.path.join(folder, f"{file_name}.json")

        with open(file_path, 'w') as file:
            json.dump(summary_dictionary, file, indent=4)
            print(f"{file_name}.json is saved successfully")

    else:
        file_path = os.path.join(folder, f"{file_name}.txt")
        with open(file_path, 'w') as file:
            file.write(summary_text)
            print(f"{file_name}.txt is saved successfully")


def main():
    """Smart Inventory Checker.
    This projects will accept Json files that has
    the data of about the products and summarize that by saving it
    as a .txt or .json
    """

    file_names = file_name_searcher()
    original_stocks_data = json_loader(*file_names)
    copied_stocks_data: List[Dict] = copy.deepcopy(original_stocks_data)

    if not copied_stocks_data:
        print('--NOTICE: File/s has no data--')
        return

    valid_data: List[Dict] = data_cleaner(copied_stocks_data)

    under_price, what_tag, stock_below = ask_user_filter_options()

    tags_usage, most_expensive_item, less_than_5_stock, products_under_price_range, products_below_stocks, products_with_the_tag = data_analyzer(
        valid_data, under_price=under_price, with_tags=what_tag, stock_below=stock_below)

    summary_dictionary = analyzed_data_into_dictionary(tags_usage, most_expensive_item, less_than_5_stock,
                                                       products_under_price_range, products_below_stocks,
                                                       products_with_the_tag, under_price, what_tag, stock_below)

    summary_text = analyzed_data_into_string(tags_usage, most_expensive_item, less_than_5_stock,
                                             products_under_price_range, products_below_stocks,
                                             products_with_the_tag, under_price, what_tag, stock_below)

    save_to_txt_or_json(summary_dictionary, summary_text)


if __name__ == "__main__":
    main()
