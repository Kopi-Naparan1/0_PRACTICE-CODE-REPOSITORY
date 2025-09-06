

class UserDataBase():
    def __init__(self):
        self._users = {}  # accepts the objects which has the attributes of username, password, and email

    def log_in(self, username, password):
        user = self._users.get(username)
        if user and user.check_password(password):
            print('Log-in was Successful')
            return True
        else:
            print("Log-in was Unsuccessful")
            return False

    def change_password(self, username, old_password, new_password):
        user = self._users.get(username)
        if user:
            return user.change_password(old_password, new_password)
        else:
            return False

    def add_user(self, username, password, email):
        user = self._users.get(username)
        if username in self._users:
            print('User already Exist.')
            return False
        else:
            self._users[username] = User(username, password, email)
            print('User is Registered')
            return True

    def list_user(self):
        for user in self._users.values():
            print(user)



class User:
    def __init__(self, name, password, email):
        self.__name = name
        self.__password = str(password)
        self.email = email

    def check_password(self, password):
        return password == self.__password

    def change_password(self, old, new):
        if self.__password == old:
            self.__password = new
            print('Password changed was successful.')
            return True
        else:
            print('Password change was unsuccessful.')
            return False

    def __str__(self):
        return f'{self.__name}: {self.email}'


def main():
    data_base_1 = UserDataBase()
    data_base_1.add_user("nyro", 1111, 'nyro@gmail.com')
    data_base_1.log_in('nyro', 1111)
    data_base_1.change_password('nyro', 1111, 2222)
    data_base_1.log_in('Nyro', 1111)
    data_base_1.add_user('nyro', 1111, 'ands@gmial.com')
    data_base_1.list_user()





if __name__ == "__main__":
    main()