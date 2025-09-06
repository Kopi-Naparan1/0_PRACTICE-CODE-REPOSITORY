import string
from math import pi
import string



def assignment1():
    def greet_user(greeting, name="Person", ):
        return f"{greeting}, {name}"

    print(greet_user("Hallo!"))

def assignment2():
    def add(a, b):
        return a + b

    print(add(5,5))

def assignment3():
    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False

    print(is_even(4))

def assignment4():
    def circle_area(radius):
        result =  pi *  radius ** 2
        return result.__round__(2)

    print(circle_area(5))

def assignment5():
    def convert_celsius_to_fahrenheit(celsius):
        result = (celsius * 9/5) + 32
        return result
    print(convert_celsius_to_fahrenheit(12))

def assignment6():
    def count_vowel(text):
        vowel = ['a', 'e', 'i', 'o', 'u']
        counter = 0


        for letter in text.lower():
            if letter in vowel:
                counter += 1
            else:
                counter += 0

        return counter
    print(count_vowel("Banana"))

def assignment7():# Need to improve recursion thinking
    def fibonacci(number):

        if number == 0 or number == 1:
            return number

        elif number > 1:

            return  fibonacci(number - 1) + fibonacci(number - 2)


    print(fibonacci(5))

def assignment8():
    def is_palindrome(word):
        word = word.lower()
        if word == word[::-1]:
            return True
        else:
            return False

    print(is_palindrome("sWowS"))

def assignment9(): #Not done.
    cart = {}

    def assignment9_main(cart):
        print('--- SHOPPING ---\n')

        while True:

            is_user_buy = input('Do you want to buy? (y/n). ("q" to quit)')
            if is_user_buy.lower() == 'q':
                show_total_price()
                break
            if is_user_buy.lower() == 'y':
                add_items(cart)

            elif is_user_buy.lower() == 'n':
                remove_items(cart)

    def add_items(cart):
        view_cart(cart)
        product = input('What product did you buy? ')
        price = float(input('What is the price of the product?'))
        cart[product] = price

    def remove_items(cart):

        while True:
            is_user_remove = input('Do you want to remove a product? (y). ')

            if is_user_remove == 'n':
                break

            if is_user_remove.lower() == "y":
                while True:
                    view_cart(cart)
                    what_product = input('What product do you want to remove?')

                    if what_product in cart:
                        del cart[what_product]
                    elif what_product not in cart:
                        print(f'{what_product} is not in the cart')

            else:
                print(f'{is_user_remove} not in the cart')

    def show_total_price():
        print(cart)

        total = 0
        for price in cart.values():
            total += price

        print(f"Total Price: {total}")

    def view_cart(cart):
        if not cart:
            print('cart is empty')

        else:
            print(f"\n--- YOUR CART ----")

            for product, price in cart.items():
                print(f'{product}: ${price:2f}')

    assignment9_main(cart)

def assignment10():

    def calculator_main():
        while True:
            user_operation = input('What operation: (+,-,*,/) ---- "q" to power-off: ')

            if user_operation == "q":
                print('power off')
                break

            elif user_operation == '+':
                print('--- ADDITION ---')
                x = int(input('First number:'))
                y = int(input('Second number:'))
                print(f"Result: {add(x, y)}")

            elif user_operation == '-':
                print('--- SUBTRACTION ---')
                x = int(input('First number:'))
                y = int(input('Second number:'))
                print(f"Result: {sub(x, y)}")

            elif user_operation == '*':
                print('--- MULTIPLICATION ---')
                x = int(input('First number:'))
                y = int(input('Second number:'))
                print(f"Result {mul(x, y)}")

            elif user_operation == '/':
                print('--- DIVISION ---')
                x = int(input('First number:'))
                y = int(input('Second number:'))
                div(x, y)



    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x ,y):
        try:
            return print(f"Result: {x / y}")
        except ZeroDivisionError:
            print("Result: ERROR")


    calculator_main()

def assignment11():
    def password_check():
        digit = [x for x in range(10)]


        while True:

            user_password = input("Input at least 8 characters password (must contain: uppercase, lowercase, digit, and special character): ")

            #Just check if user_password contain -> must contain
            if (len(user_password) >= 8) and \
                (user_password.count(string.ascii_lowercase) > 0) and \
                (user_password.count(string.ascii_uppercase) > 0) and \
                (user_password.count(string.digits) > 0) and \
                (user_password.count(string.punctuation) > 0):
                print('What a strong password')

            elif len(user_password) < 8:
                print('Must be at least 8 characters')


    password_check()























def main():
    #Basic part 1-5
    # assignment1()
    # assignment2()
    # assignment3()
    # assignment4()
    # assignment5()


    #Intermediate part 6-10
    # assignment6()
    # assignment7()
    # assignment8()
    # assignment9()
    # assignment10()
    assignment11()







if __name__ == "__main__":
    main()