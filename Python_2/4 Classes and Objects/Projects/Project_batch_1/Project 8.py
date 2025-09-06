from abc import ABC


class InventorySystem(ABC):
    pass


class Inventory(InventorySystem):
    def __init__(self):
        self.__stocks = []

    def add_product(self, *products: list):
        for product in products:
            self.__stocks.append(product)

    def bill(self):
        for product in self.__stocks:
            print(f'- {product.product} -- ${product.price}')

        prices = [product.price for product in self.__stocks]
        total = sum(prices)

        print(f'Total price: ${total}')


class MakeProducts:
    def __init__(self, product, price):
        self.product = product
        self.price = price


paper = MakeProducts("paper", 100)
pen = MakeProducts("pen", 120)
guitar = MakeProducts("guitar", 2000)
cellphone = MakeProducts("cellphone", 1500)
laptop = MakeProducts("laptop", 5000)
bond_paper = MakeProducts("bond paper", 392)

products_bought_1 = [paper, pen, guitar, cellphone, laptop, bond_paper]
store = Inventory()
store.add_product(*products_bought_1)
store.bill()












