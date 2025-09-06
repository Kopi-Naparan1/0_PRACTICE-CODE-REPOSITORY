

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
        print(f'Deposited ${amount} successfully...')

    def withdraw(self, amount):
        self.__balance -= amount
        print(f'Withdrew ${amount} successfully...')

    def get_balance(self):
        print(f"Current Balance: ${self.__balance}")


account_1 = BankAccount()
account_1.deposit(1000)
account_1.withdraw(500)
account_1.deposit(123)
account_1.get_balance()



