from abc import ABC, abstractmethod


class CartSystem(ABC):

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def calculate_products(self):
        pass

    @abstractmethod
    def __len__(self):
        pass


class Cart(CartSystem):
    def __init__(self, discount=0.0):
        self.__items = []
        self.__discount = discount

    def add_product(self, product):
        self.__items.append(product)

    def calculate_products(self):
        total = sum(item.price for item in self.__items)
        discounted = total * (1 - self.__discount)
        return f'Discount: {self.__discount*100}% From: {total} To: {discounted}'

    def __str__(self):
        return "\n".join(str(item) for item in self.__items)

    def __len__(self):
        return len(self.__items)


class Product:
    def __init__(self, product, price):
        self.product = product
        self.price = price

    def __str__(self):
        return f'{self.product} - {self.price}'


paper = Product("Paper", 100)
pencil = Product("Pencil", 50)
sharpener = Product("Sharpener", 25)
guitar = Product("Guitar", 2000)


cart_1 = Cart(0.1)
cart_1.add_product(paper)
cart_1.add_product(pencil)
cart_1.add_product(guitar)
cart_1.add_product(sharpener)


cart_2 = Cart(0.2)
cart_2.add_product(sharpener)
cart_2.add_product(guitar)


print("Cart 1: ")
print(cart_1)
print(cart_1.calculate_products())
print(f'Number of items in the cart: {len(cart_1)}')