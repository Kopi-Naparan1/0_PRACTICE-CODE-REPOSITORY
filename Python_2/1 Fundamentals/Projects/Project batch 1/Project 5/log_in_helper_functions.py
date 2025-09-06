from todo_system import main
import json
import getpass
import hashlib

file_path = (r"C:\KOPI ANAN PASCO NAPARAN\PROGRAMMING\Python Course\1 Fundamentals\Projects\Project batch 1\Project "
             r"5\data\users.json")


def home_page() -> str:
    print('')
    print('-' * 30)
    choice = input("""
    [1] Log-in
    [2] Sign-up
    [3] Exit
    Choice: """)
    print('-' * 30)
    print('')
    return choice


def user_login():
    print('--- LOGIN ---')
    username = input('Username: ')
    password_unsafe = getpass.getpass('Password: ')
    password_safe = hashlib.sha256(password_unsafe.encode()).hexdigest()

    return username, password_safe


def user_signup():
    print('--- SIGNUP ---')
    username = input('Username: ').strip()
    password_unsafe = getpass.getpass('Password: ')
    password_safe = hashlib.sha256(password_unsafe.encode()).hexdigest()

    return username, password_safe


def log_in_authenticator(username, password, users) -> bool:
    if username in users and password == users[username]:
        print(f'Verified: {username} Logged-in.')
        return True

    elif username in users and users[username] != password:
        print(f'Unverified: {username} - Wrong Password')
        return False

    elif username not in users:
        print(f'Unverified: {username} is not found.')
        return False

    else:
        print('Error: Something is not right...')
        return False


def sign_up_authenticator(username, password, users: dict) -> bool:
    if username not in users and password not in users.values():
        print(f'Registered: {username}. You can now log-in.')
        return True

    elif username in users and users[username] == password:
        print(f'Data already exist. Try logging in.')
        return False

    elif username in users and users[username] != password:
        print(f'Incorrect Password.')
        return False

    else:
        print('Error: Something is not right...')
        return False


def users_saver(users):

    with open(file_path, 'w') as file:
        json.dump(users, file, indent=4)
        print('User is saved into the data base..')


def users_loader() -> dict:
    try:
        with open(file_path, 'r') as file:
            read = json.load(file)
            if read:
                return read
            else:
                return {}
    except FileNotFoundError:
        print('File not found...')
        return {}

    except json.JSONDecodeError:
        print('Json decode error...')
        return {}


def todo_authentication(verified, username):
    if verified:
        main(username)

    elif not verified:
        return None

