# Simulate a basic product catalog using lists of dictionaries


class Product:
    products = {}

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.products[name] = price


def display_product():
    i = 1
    print('\n---Products---')
    for k, v in Product.products.items():
        print(f'Product {i} - {k}: ${v}')
        i += 1
    print('-' * 20)
    print('\n')


def update_product():
    print('\n---- Updating a product ----\n')
    while True:
        try:
            product = input('What product to update:').lower().strip()

            if product in Product.products:
                break

        except KeyError:
            print('Not found. Please try again.')

    choice = input("""--- CHOOSE ---
    [1] Change name
    [2] Change price
    [3] Change both
    Choice: """)

    if choice == '1':
        new_name = input('Input new name: ').lower().strip()
        Product.products[new_name] = Product.products.pop(f"{product}")
        print('New name is updated...')

    elif choice == '2':
        new_price = input('Input new price: ')
        Product.products[product] = new_price
        print('New price is updated...')

    elif choice == '3':
        del Product.products[product]

        new_name = input('Input new name: ').lower().strip()
        new_price = int(input('Input new price: '))

        Product.products[new_name] = new_price
        print('New name and price is updated...')


def delete_product():

    while True:
        try:
            product = input('What product to delete? ').lower().strip()

            if product in Product.products:
                del Product.products[product]
                print(f'{product} is deleted')
                break

        except KeyError:
            print('Not found. Please try again.')


def make_product():
    name = input('Name: ').lower().strip()
    price = int(input('Price: '))
    return name, price


def main():
    """June 14, to fix:
    1. price must be float
    2. prevention of duplicates
    3. If el-if will do, then don't use try-except
    4. This can be better with OOP (I need to practice OOP again)"""

    functions = {"2": display_product,
                 "3": update_product,
                 "4": delete_product,
                 }
    i = 1
    while True:
        choice = input(""""--- CHOOSE ---
        [1] Create a product
        [2] Display products
        [3] Update a product
        [4] Delete a product
        [5] Exit
        Choice: """)

        if choice == '1':
            print(f'\n---Product {i}---')
            name, price = make_product()
            Product(name, price)
            print(f'{name.title()}: ${price} is added')
            print('-' * 10)
            print('\n')
            i += 1

        elif choice in "234":
            for k, v in functions.items():
                if k == choice:
                    v()
        elif choice == '5':
            print('Exiting...')
            break

if __name__ == "__main__":
    main()