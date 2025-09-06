
#

def assignment1():  # Start: 7:45 am,  May 17 --- Done 8:36 am, May 17
    from string import ascii_uppercase as uppercase
    from string import ascii_lowercase as lowercase
    from string import digits
    from string import punctuation

    def user_input_password() -> str:
        """This function returns an str"""

        user_password = input('Input your password: ')
        return user_password

    def check_length(user_password: str) -> bool:
        if len(user_password) >= 8:
            return True
        else:
            return False

    def check_uppercase(user_password: str) -> bool:
        return any(character in uppercase for character in user_password)

    def check_lowercase(user_password: str) -> bool:
        return any(character in lowercase for character in user_password)

    def check_digit(user_password: str) -> bool:
        return any(character in digits for character in user_password)

    def check_special_characters(user_password: str) -> bool:
        return any(character in punctuation for character in user_password)

    def display_strong_password(user_password: str) -> str:
        print(f'\n\n[{user_password}] is a STRONG PASSWORD')

    def display_weak_password(user_password: str) -> str:
        print(f'\n\n[{user_password}] is a WEAK PASSWORD')
        print('-' * 35)

    def main_assignment_1():
        """Manage everything"""
        print('--- Welcome to Password Checker ---')
        print('Strong password contains:\n'
              '\t- >8 Characters\n'
              '\t- Uppercase\n'
              '\t- Lowercase\n'
              '\t- Digit\n'
              '\t- Special Characters\n')
        user_password = user_input_password()

        print('-' * 35)

        if not check_length(user_password):
            print('----- Failed length test')
            display_weak_password(user_password)
            return

        print('----- Passed the length test')

        if not check_uppercase(user_password):
            print('---- Failed uppercase test')
            display_weak_password(user_password)
            return

        print('---- Passed the uppercase test')

        if not check_lowercase(user_password):
            print('--- Failed lowercase test')
            display_weak_password(user_password)
            return
        print('--- Passed the lowercase test')

        if not check_digit(user_password):
            print('-- Failed digit test')
            display_weak_password(user_password)
            return
        print('-- Passed the punctuation test')

        if not check_special_characters(user_password):
            print('- Failed special characters test')
            display_weak_password(user_password)
            return
        print('- Passed the special characters test')

        display_strong_password(user_password)

    main_assignment_1()

def assignment2():
    def order():
        ordered_items = {"paid": True,
                         "items": ['Banana', 'Orange'],
                         }
        return ordered_items

    def process_order(ordered_items: dict) -> bool:
        if not ordered_items:
            print('Invalid Order')
            return False
        print('--- Valid Order')

        if not ordered_items['paid']:
            print('You need to pay first')
            return False
        print('-- Paid Order')

        if not ordered_items['items']:
            print('No items in order')
            return False
        print('- Items in order ')

        return True

    def display_order(order: dict):
        print('-' * 30)
        print(f'Delivering your order:')

        i = 1
        for value in order["items"]:
            print(f"[{i}]{value}")
            i += 1
        print('=== PAID === ')

        print('-' * 30)

    def process_order_main():
        ordered_items = order()
        processed_order = process_order(ordered_items)
        if processed_order:
            display_order(ordered_items)

    process_order_main()

def assignment3():
    def give_user_data() -> dict:  # I put this here to have a data
        user_data = {"email_verified": True,
                     "terms_and_conditions": True,
                     "age": 20, }
        return user_data

    def check_email(user_data):  # I split 3 checkers (email,TaC, age) so that the logic is much easy to flow and debug
        try:
            if user_data['email_verified']:
                return True
            else:
                return False
        except KeyError:
            print('Error: Checking email gone wrong...')
            return False

    def check_terms_and_condition(user_data):
        try:
            if user_data['terms_and_conditions']:
                return True
            else:
                return False

        except KeyError:
            print('Error: Checking Terms and Conditions...')
            return False

    def check_age(user_data):
        try:
            if user_data['age'] > 18:
                return True
            else:
                return False
        except KeyError:
            print("Error: Checking age gone wrong... ")
            return False

    def data_processing(user_data):  # I made this to put those checkers in use. They will be used here..

        checks = [check_email, check_terms_and_condition, check_age]

        if all(check(user_data) for check in
               checks):  # I put all () to make sure every checkers return True, if not, itll return false
            print("---Registration Successful---")
        else:
            print('---Registration Unsuccessful---')

    def assignment_3_main():
        user_data = give_user_data()
        data_processing(user_data)

    assignment_3_main()

def assignment4(): # Start, around 9:30, may 17 or so, Done 10:50 pm, may 17
    import string

    def give_password() -> str:  # I want the user_password to be checked easily so I made the user input password
        user_password = input('Input password: ')
        return user_password

    # The idea behind why I separated 3 checks is because it is easier to debug and makes the
    # convention true: One function, one function.
    def check_length(user_password: str) -> bool:
        try:
            if len(user_password) > 8:
                return True
            else:
                return False
        except TypeError:
            print('Something is wrong...(Check_length)')
            return False

    def check_digit(user_password: str) -> bool:
        try:
            if any(character for character in user_password if character in string.digits):
                return True
            else:
                return False
        except TypeError:
            print('Something is wrong...(check_digit)')
            return False

    def check_uppercase(user_password: str) -> bool:
        try:
            if any(character for character in user_password if character in string.ascii_uppercase):
                return True
            else:
                return False
        except TypeError:
            print('Something is wrong...(check_uppercase)')
            return False

    def main_assignment4():
        password = give_password()

        # This dictionary exist because I want easier and cleaner code
        checks = {check_length: "Passed the length test",
                  check_digit: "Passed the digit test",
                  check_uppercase: "Passed the uppercase test",
                  }

        for key, value in checks.items(): # I want to iterate the dictionary (checks) like a polymorphism
            if key(password):
                print(value)
            else:
                print(value.replace("Passed", "Failed"))

        # After the iteration of dictionary (checks), I want this to output whether the password is strong or not
        if all(key(password) for key in checks.keys()):
            print('--- Strong Password ---')
        else:
            print("--- Weak Password ---")

    main_assignment4()

def main():
    # assignment1()
    # assignment2()
    # assignment3()
    # assignment4()


if __name__ == "__main__":
    main()
