from string import ascii_uppercase

UPPER_CASE = ascii_uppercase
NUMBER = "0123456789"

def get_password() -> str:
    return input("Enter your password: ")

def check_length(password) -> bool:
    return len(password) >= 8


def has_number(password) -> bool:
    for character in password:
        if character in NUMBER:
            return True
    return False


def has_uppercase(password) -> bool:
    for character in password:
        if character in UPPER_CASE:
            return True
    return False


def main():

    password = get_password()


    is_length = check_length(password)
    is_number = has_number(password)
    is_uppercase = has_uppercase(password)

    if is_number and is_length and is_uppercase:
        print("Your Password is strong")
        return
    print("Your password is weak")

main()