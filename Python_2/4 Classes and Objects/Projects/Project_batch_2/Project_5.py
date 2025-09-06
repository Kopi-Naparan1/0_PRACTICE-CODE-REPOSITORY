from collections import Counter

class UserDatabase:
    def __init__(self):
        self.users = {}

    def add_user(self, user_name, password, role):
        if user_name not in self.users:
            self.users[user_name] = UserFactory.create_user(user_name, password, role)
            return True
        else:
            print(f'User: {user_name} already exists')
            return False

    def log_in(self, username, password):
        user = self.users.get(username)
        if user and user.check_password(password):
            print(f'{username} Logged-In')
            return True
        else:
            print(f'{username} not found or wrong password')
            return False

    def change_password(self, username, old_password, new_password):
        user = self.users.get(username)
        if user and user.change_password(old_password, new_password):
            print(f'{username} - Password Changed Successfully')
            return True
        else:
            print(f'{username} - Password Change is Unsuccessful')
            return False

    def get_user(self, username):
        user = self.users.get(username)
        if user:
            print(f'Username: {username} Found')
            return user
        else:
            print(f'{username} is not found')
            return None

    def list_users(self):
        return list(self.users.values())


class UserFactory:
    @staticmethod
    def create_user(username, password, role='user'):
        if role == 'admin':
            print(f'Admin: {username} is added')
            return AdminUser(username, password, role)
        elif role == 'manager':
            print(f'Manager: {username} is added')
            return ManagerUser(username, password, role)
        else:
            print(f'User: {username} is added')
            return RegularUser(username, password, role)


class User:
    def __init__(self, username, password, role):
        self.username = username
        self._password = str(password)
        self.role = role

    def change_password(self, old_password, new_password):
        if old_password == self._password:
            self._password = new_password
            return True
        return False

    def check_password(self, password):
        return self._password == password

    def __str__(self):
        return f'{self.username} - [{self.role}]'


class RegularUser(User):
    def buy_product(self, product_name, quantity, product_database, transaction_log):
        result = product_database.buy_product(product_name, quantity)
        if result:
            name, total_price = result
            transaction_log.record(self.username, name, total_price)
        else:
            print("Purchase failed.")


class AdminUser(User):
    def __init__(self, user_name, password, role):
        super().__init__(user_name, password, role)

    def add_product(self, name, price, quantity, product_database):
        product_database.add_product(name, price, quantity)

    def remove_product(self, name, product_database):
        product_database.remove_product(name)

    def update_product(self, name, field, new_value, product_database):
        product_database.update_product(name, field, new_value)


class ManagerUser(User):
    def view_sales(self, transaction_log):
        for user, records in transaction_log.logs.items():
            print(f"User: {user}")
            for product, price in records:
                print(f"  - {product}: ${price}")

    def view_inventory(self, product_database):
        for product in product_database.list_products():
            print(product)


class ProductDatabase:
    def __init__(self):
        self.products = {}

    @staticmethod
    def normalize_name(name):
        return name.strip().lower()

    def add_product(self, name, price, quantity):
        name = self.normalize_name(name)
        try:
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            print("Invalid input: price must be a number, quantity must be an integer")
            return

        if name not in self.products:
            self.products[name] = Product(name, price, quantity)
            print(f'Product: {name} ${price} added successfully')
        else:
            print(f'Product: {name} Already Exists')

    def buy_product(self, name, quantity):
        name = self.normalize_name(name)
        product = self.products.get(name)

        if not product:
            print(f'{name} is not found')
            return None

        if product.quantity >= quantity:
            product.quantity -= quantity
            total_price = product._price * quantity
            invoice = f'{quantity} {name}(s) = ${product._price} * {quantity} = ${total_price}'
            print(invoice)
            return product.name, total_price
        else:
            print('Product is unavailable. Possible reasons: (1) Out of stock')
            return None

    def remove_product(self, name):
        name = self.normalize_name(name)
        if name in self.products:
            del self.products[name]
            print(f'Product: {name} removed')
        else:
            print(f'Product: {name} not found')

    def update_product(self, name, field, new_value):
        name = self.normalize_name(name)
        product = self.products.get(name)
        if not product:
            print('Product not found')
            return

        if field == "name":
            new_name = self.normalize_name(new_value)
            if new_name in self.products:
                print("New name already exists")
                return
            product.name = new_name
            self.products[new_name] = self.products.pop(name)
        elif field == "price":
            try:
                product._price = float(new_value)
            except ValueError:
                print("Invalid price value")
        elif field == "quantity":
            try:
                product.quantity = int(new_value)
            except ValueError:
                print("Invalid quantity value")
        else:
            print("Invalid field")

    def list_products(self):
        return self.products.values()


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self._price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return f"[{self.name} - ${self._price} - {self.quantity} pcs]"


class TransactionLog:
    def __init__(self):
        self.logs = {}

    def record(self, username, product, price):
        if username not in self.logs:
            self.logs[username] = []
        self.logs[username].append((product, price))
        print(f'Recorded: {username}: {product} - {price}')

    def get_user_history(self, username):
        return self.logs.get(username, [])

    def get_top_sellers(self):
        all_purchases = [prod for purchases in self.logs.values() for prod, _ in purchases]
        return Counter(all_purchases).most_common()


def main():
    user_db = UserDatabase()
    product_db = ProductDatabase()
    transaction_log = TransactionLog()

    user_db.add_user('Nyro_1', '11111', 'user')
    user_db.add_user('Nyro_2', '22222', 'manager')
    user_db.add_user('Nyro_3', '33333', 'admin')

    user_db.log_in("Nyro_1", '11111')
    user_db.log_in("Nyro_2", '22222')
    user_db.log_in("Nyro_3", '33333')

    user_db.change_password("Nyro_1", '11111', 'aaaaa')
    user_db.log_in("Nyro_1", '11111')
    user_db.log_in("Nyro_1", 'aaaaa')

    print('--- User List ---')
    for user in user_db.list_users():
        print(user)

    nyro_1 = user_db.get_user("Nyro_1")
    nyro_2 = user_db.get_user("Nyro_2")
    nyro_3 = user_db.get_user("Nyro_3")

    nyro_3.add_product("Laptop", 1999, 100, product_db)
    nyro_3.add_product("Cellphone", 999, 1000, product_db)
    nyro_3.add_product("Mouse", 129, 1293, product_db)

    field = input("Update [name/price/quantity]: ").strip().lower()
    if field in ['price', 'quantity']:
        try:
            new_value = float(input("New value: ")) if field == 'price' else int(input("New value: "))
        except ValueError:
            print("Invalid number")
            return
    elif field == 'name':
        new_value = input("New product name: ").strip()
    else:
        print("Invalid field")
        return
    nyro_3.update_product("Laptop", field, new_value, product_db)

    nyro_3.remove_product("Mouse", product_db)

    print('--- Product List ---')
    for product in product_db.list_products():
        print(product)

    try:
        quantity = int(input("How many Laptops? "))
        nyro_1.buy_product("Laptop", quantity, product_db, transaction_log)
        quantity = int(input("How many Cellphones? "))
        nyro_1.buy_product("Cellphone", quantity, product_db, transaction_log)
    except ValueError:
        print("Invalid quantity input")

    nyro_2.view_inventory(product_db)
    nyro_2.view_sales(transaction_log)


if __name__ == "__main__":
    main()

# Project has lots of bugs. NOTE: in 6 months. Maybe in December 2025, recode this
# but use multiple files and use what you have learned so far. Anyways, I am proud of you
# THis has probably less than 10 bugs, fix it anytime. BUt, I want you to recode this in
# future
