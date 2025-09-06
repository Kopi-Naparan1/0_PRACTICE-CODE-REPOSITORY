import json
import os


# region main_functions

def add_product():
    name = input('Name: ').lower
    price = int(input("Price: $ "))
    quantity = int(input("Quantity: "))
    return name, price, quantity


def view_products(products: dict):
    print('----------------')
    print('----- Products -----')
    for key, val in products.items():
        print(f"---{key.title()}---")
        print(f'Price: {val["Price"]}')
        print(f'Quantity: {val["Quantity"]}')

    print('----------------')


def search_product(products: dict):
    product_searched = input("Search a product: ").lower()
    print('-' * 30)
    for product in products:
        if product_searched in product.lower():
            print(f'{product.title()}')
            print(f'  - $ {products[product]["Price"]} each')
            print(f'  - {products[product]["Quantity"]} qty')
    print('-' * 30)
    print('')

# endregion

# region backend_functions
def product_info_loader():
    folder = os.path.join(
        "C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course",
        "2 Data Structures & File Handling", "PROJECTS 2", "Cache_files"
    )

    file_name = os.path.join(folder, 'Products.json')

    try:
        with open(file_name, 'r') as file:
            read = json.load(file)
            return read
    except FileNotFoundError:
        print('New File is made...')
        return {}

    except json.JSONDecodeError:
        print('Json decode error - task loader...')
        return {}


def product_info_saver(product_info):
    folder = os.path.join(
        "C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course",
        "2 Data Structures & File Handling", "PROJECTS 2", "Cache_files"
    )

    file_name = os.path.join(folder, 'Products.json')


    with open(file_name, 'w') as file:
        json.dump(product_info, file, indent=4)
        print('Data is saved')
# endregion


def main():
    products_dict = product_info_loader()

    while True:
        choice = input("""
        [1] ADD A PRODUCT
        [2] VIEW PRODUCT/S
        [3] SEARCH A PRODUCT
        [4] QUIT and save
        CHOICE: """)

        if choice == '1':
            name, price, quantity = add_product()
            products_dict[name] = {"Price": price,
                                   "Quantity": quantity,
                                   }
            print(products_dict)

        elif choice == '2':
            view_products(products_dict)

        elif choice == '3':
            search_product(products_dict)

        elif choice == '4':
            product_info_saver(products_dict)
            print('---SAVED---')
            break




if __name__ == "__main__":
    main()