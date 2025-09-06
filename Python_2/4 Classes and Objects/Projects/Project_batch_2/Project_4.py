from abc import ABC, abstractmethod


class UserDataBase(ABC):
    def __init__(self):
        self._users = {}

    def log_in(self, username, password):
        user = self._users.get(username)
        if user and user.check_password(password):
            print('Logged-In Successfully')
            return True
        else:
            print('Log-in Failed')
            return False

    def change_password(self, username, old_password, new_password):
        user = self._users.get(username)
        if user and user.check_password(old_password):
            return user.change_password(old_password, new_password)
        else:
            return False

    def add_user(self, user_name, password, role='user'):
        if user_name in self._users:
            print(f'{user_name} already existed')
            return False
        else:
            if role == 'admin':
                self._users[user_name] = Admin(user_name, password, role)
                print(f'Admin: {user_name} added')
                return True

            else:
                self._users[user_name] = User(user_name, password, role)
                print(f'User: {user_name} added')
                return True

    def list_users(self):
        for user in self._users.values():
            print(user)

    @property
    def users(self):
        return self._users


class User:
    def __init__(self, username, password, role):
        self.username = username
        self.__password = password
        self.role = role

    def change_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            print('Password Change Successfully')
            return True

        else:
            print('Password Change Failed')
            return False

    def check_password(self, password):
        if password:
            return password == self.__password
        else:
            return False

    def buy_product(self, product, product_db):
        if product:
            product = product_db.buy_product(product)
            print(f'{self.username} bought {product}')
            return True
        else:
            return False

    def __str__(self):
        return f'{self.username} - {self.role}'


class Admin(User):
    def __init__(self, username, password, role):
        super().__init__(username, password, role)

    def add_product(self, product_db, product_name, price):
        if self.role == 'admin':
            product_db.add_products(product_name, price)
        else:
            return False

    def remove_product(self, product_db, product_name):
        if self.role == 'admin':
            product_db.remove_products(product_name)
        else:
            return False


class ProductDataBase:
    def __init__(self):
        self.products = {}

    def add_products(self, product_name, price):
        if product_name in self.products:
            print(f'Product: {product_name} already existed')
            return False
        else:
            self.products[product_name] = price
            print(f'Product: {product_name}: $ {price} added successfully')
            return True

    def remove_products(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
            print('Removing product was successful')
        else:
            print('Removing product was unsuccessful')
            return False

    def list_products(self):
        print('\n----Products----\n')
        i = 1
        for name, price in self.products.items():
            print(f'{i} {name}: {price}')
            i += 1
        print('-------------------------')

    def buy_product(self, product):
        if product in self.products:
            return f'{product}: {self.products[product]}'
        else:
            print('Product is not available')
            return False


def main():
    # Step 1: Create database objects
    user_db = UserDataBase()
    product_db = ProductDataBase()

    # Step 2: Add users
    user_db.add_user('Nyro', '1234', 'user')
    user_db.add_user('Kophalem', 'admin123', 'admin')
    #
    # Step 3: List users
    print("\n--- User List ---")
    user_db.list_users()
    #
    # Step 4: Add products (via Admin)
    admin = user_db._users['Kophalem']  # this has the admin instance
    admin.add_product(product_db, 'Laptop', 1500)
    admin.add_product(product_db, 'Phone', 800)
    #
    # Step 5: List products
    print("\n--- Product List ---")
    product_db.list_products()
    #
    # Step 6: Let Nyro buy a product
    nyro = user_db._users['Nyro']
    nyro.buy_product('Phone', product_db)

    # Step 7: Attempt login
    user_db.log_in('Nyro', '1234')

    # Step 8: Change password
    nyro.change_password('1234', '5678')
    user_db.log_in('Nyro', '5678')






if __name__ == "__main__":
    main()