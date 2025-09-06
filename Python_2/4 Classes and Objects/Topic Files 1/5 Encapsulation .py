

def assignment6():
    class SecureNote:
        def __init__(self, password):
            self.__note = None #Just an empty one
            self.__password = password

        def incorrect_pass(self, password):
            print('')
            print('!' * 30)
            print(f'Your Password: {password} is Incorrect')
            print('!' * 30)

        def change_password(self, old_password, new_password): #I put old and new pass, to check if the user knows the pass first before changing the pass
            if self.__password == old_password:
                print("-" * 30)
                print(f"Old password: {old_password}")
                self.__password = new_password
                print(f"New password: {new_password}")
                print("-" * 30)
            else:
                self.incorrect_pass(old_password)

        def writenote(self, note, password): #if pass is correct, user can change the note
            if password == self.__password:
                print("-" * 30)
                print(f'Previous note: {self.__note}')
                self.__note = note
                print(f'New note: {note}')
                print("-" * 30)
            else:
                self.incorrect_pass(password)

        def read_note(self, password):
            if password == self.__password:
                print("-" * 30)
                return print(f"Current Note: {self.__note} \n {'-' * 30} ")


            else:
                self.incorrect_pass(password)


    person1 = SecureNote("123")
    person1.writenote("First", "123")
    person1.writenote("Second", "123")
    person1.read_note("123")
    person1.change_password("123", "4321")
    person1.writenote("Third", "4321")






















def main():
    print("=" * 30)
    print('STARTING THE #5')
    print("=" * 30)
    print('\n' * 5)

    assignment6()



if __name__ == "__main__":
    main()