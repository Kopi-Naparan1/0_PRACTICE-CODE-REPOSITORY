
from log_in_helper_functions import (log_in_authenticator,
                                     sign_up_authenticator,
                                     home_page,
                                     users_loader,
                                     user_login,
                                     user_signup,
                                     todo_authentication,
                                     users_saver)


def main():
    users = users_loader()

    while True:
        choice = home_page()
        if choice == '1':
            username, password = user_login()
            result = log_in_authenticator(username, password, users)
            if result:
                todo_authentication(result, username)

        elif choice == '2':
            username, password = user_signup()
            result = sign_up_authenticator(username, password, users)
            if result:
                users[username] = password
                users_saver(users)
        elif choice == '3':
            print('--- Leaving---')
            break
        else:
            print('Error: Choose between [1] or [2].')


if __name__ == '__main__':
    main()
