# The purpose of this file is for me to practice every topic in my level 2 thoroughly
# Start: 12:46 am, may 18 , Finished:



def assignment1(): # 12:50 am - 1:22 am
    def ask_contact_info() -> dict:
        """This is here because I want to make an assignment where it ask for 3 contact infos,
        then asks the user for a name, then print if it is there or nor."""

        contacts = {}

        for i in range(1,4): # Ask for exactly 3 contacts
            name = input(f'Name of contact [{i}]: ')
            phone = input(f'Phone # of contact [{i}]: ')
            email = input(f'Email of contact [{i}]: ')
            contacts[name] = {
                            "Phone #": phone,
                            "Email": email,
                            }
        return contacts

    def display_contact_info(contact_info: dict) -> None:
        print('---- Contact List ----')
        for name, info in contact_info.items():
            print(f"Name: {name}")
            print(f"  Phone #: {info['Phone #']}")
            print(f"  Email: {info['Email']}")
            print("-" * 20)


    def is_user_a_name_found(contact_info: dict) -> bool:
        """This exist for checking if the name is there or not"""
        check_name = input('Check a name: ')

        return check_name in contact_info

    def update_email_contact(contact) -> None:

        # This block of code exist to make sure the user will type a valid name
        name = input('Update email of contact (name): ')

        while name not in contact.keys():
            name = input('Update email of contact (name): ')

        new_email = input('what should be the new email: ')
        contact[name]['Email'] = new_email
        print(f'New email is updated [{new_email}]')

    def display_result(result: bool):
        """If it receive a bool, it will then make the final result"""
        if result:
            print('Name is found')
        else:
            print('Name is not found')

    def assignment_main():
        """This block of code exist because I made this assignment in an organized manner"""

        # Main data
        contact_info = ask_contact_info()

        # The display contact info
        display_contact_info(contact_info)

        #Some checking functions
        ask_search_name = input("Want to search [1]name only or [2]update an email? ([1] or [2]) ")
        if ask_search_name == "1":
            is_name_found = is_user_a_name_found(contact_info)  # check for name
            display_result(is_name_found)
        elif ask_search_name == "2":
            update_email_contact(contact_info)
            display_contact_info(contact_info)

    assignment_main()

def assignment2():

    def ask_3_contacts() -> dict:
        """Only ask for 3 contacts that return that dict"""

        contacts = {}
        for i in range(1,4):
            name = input(f"[{i}] Name: ")
            phone = input(f'[{i}] Phone #: ')
            email = input(f"[{i}] Email: ")

            contacts[name] = {"Phone": phone,
                              "Email": email,
                              }
        return contacts

    def view_contacts(contact: dict) -> None:
        """Display contacts, printed it."""
        print('--- Contact Information---')
        for name, info in contact.items():
            print(f"'Name': {name}")
            print(f"Phone #: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print('-' * 30)

    def choose_search_or_update_or_exit() -> str:
        """Make user decide to , search, update, or exit"""

        while True:
            user_choice = input('Do you want to [1] search a name, [2] update an email, [3] exit? ')
            if user_choice in ['1', '2', '3']:
                return user_choice
            print("Invalid input. Please choose 1, 2, or 3.")

    def search_contact_name(contacts: dict) -> None:
        """Search a name, return None"""

        name = input("Search a name: ")
        if name in contacts:
            print(f"{name} is found.")
            print(f"Phone #: {contacts[name]['Phone']}")
            print(f"Email: {contacts[name]['Email']}")
        else:
            print(f"{name} is not found.")

    def display_updated_contact(contact: dict, name: str) -> None:
        print(f"Name: {name}")
        print(f"Phone #: {contact[name]['Phone']} ")  # Learning: Always link the keys to the original dict
        print(f"Email: {contact[name]['Email']} ")

    def update_email(contact: dict) -> str:
        """Update email when user input the name"""

        while True:
            name = input('Name of the email that you want to update: ')

            if name in contact.keys():
                new_email = input('New email: ')
                contact[name]["Email"] = new_email
                print(f'New email: {new_email}')
                return name
            else:
                print("Name not found")


    def main_assignment3():
        contacts = ask_3_contacts() # The data

        view_contacts(contacts)  # +


        # Prompts the user to decide finding name or updating an email or exit
        while True:
            user_choice = choose_search_or_update_or_exit() #+
            # This block of code is connected to user_choice, I put this like this to make sure that
            # Functions have one job and they do it well, and make things organized
            if user_choice == "1":
                search_contact_name(contacts)
            elif user_choice == "2":
                name = update_email(contacts)
                display_updated_contact(contacts, name)
            elif user_choice == "3":
                print("Exiting the program...")
                break


    main_assignment3()

def assignment3():
    students = {
        "Alice": {"Math": 90, "English": 85},
        "Bob": {"Math": 78, "English": 92},
        "Clara": {"Math": 88, "English": 79},
        "Kopi": {"Math": 99, "English": 89}
    }

    for name, subjects in students.items():
        score = subjects.values()
        average = sum(score) / len(score)
        if average > 84:
            print(f'{name}: {average} --- passed')
        elif average < 85:
            print(f'{name}: {average} --- failed')

def assignment4():

    def search_book(data:dict, genre= None, author= None ):

        result = []

        for books, infos in data.items():
            if infos["author"] == author:
                result.append(books)
            elif genre in infos["genres"]:
                result.append(books)


        return result if result else f'Not found'





    library = {
            "Book1": {"author": "George Orwell", "year": 1949, "genres": ["dystopian", "political"]},
            "Book2": {"author": "J.K. Rowling", "year": 1997, "genres": ["fantasy", "young adult"]},
            "Book3": {"author": "J.R.R. Tolkien", "year": 1954, "genres": ["fantasy", "epic"]}
                }


    print(search_book(library,"fantasy","J.R.R. Tolkien"))

    # print(library["Book1"]["genres"][0])



def main():
    # assignment1()
    # assignment2()
    # assignment3()
    assignment4()








if __name__  == "__main__":
    main()


















def main():
    pass












if __name__ == "__main__":
        pass