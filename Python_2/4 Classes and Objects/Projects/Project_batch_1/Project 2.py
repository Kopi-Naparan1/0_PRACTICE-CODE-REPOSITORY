
class BankSystem:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount: int):
        if amount > 0:
            self.__balance += amount
            print(f'Successfully Deposited ${amount}')

    def withdraw(self, amount: int):
        if self.__balance > amount > 0:
            self.__balance -= amount
            print(f'Successfully withdrew ${amount}')
        else:
            self.__balance += 0
            print(f'Failed to Deposited ${amount}')

    def check_balance(self):
        print(f'Current Balance: ${self.__balance}')


account_1 = BankSystem()
account_1.deposit(1000)
account_1.check_balance()
account_1.withdraw(243)
account_1.check_balance()
account_1.deposit(1929)