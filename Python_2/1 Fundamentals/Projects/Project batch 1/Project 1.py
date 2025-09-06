

def ask_questions():
    name = input('Name: ').lower()

    while not name.isalpha():
        name = input("Please enter a valid name: ")

    while True:
        try:
            age = int(input("Age: "))
            break
        except ValueError:
            print('Please enter an Integer')
    email = input('Email: ').lower()

    while "@" not in email or "." not in email:
        email = input("Invalid email. Try again: ")

    return name, age, email


class User:
    users = {}
    __num_users = 0

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def register_user(self):
        info = {"Name": self.name,
                "Age": self.age,
                "Email": self.email,
                }

        User.users[self.__num_users+1] = info
        User.__num_users += 1

    def __str__(self):
        return f'---User {User.__num_users} is registered---'


def main():
    while True:

        name, age, email = ask_questions()
        user = User(name, age, email)
        user.register_user()
        print(user)

        shall_continue = input('N to stop: ').lower()
        if shall_continue == 'n':
            break

    print("\nAll Registered Users:")
    for uid, info in User.users.items():
        print(f"User {uid}: {info}")


if __name__ == "__main__":
    main()