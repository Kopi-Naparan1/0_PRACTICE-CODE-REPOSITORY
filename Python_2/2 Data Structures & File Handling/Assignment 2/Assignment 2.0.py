


### 1 Dictionary

#task 1
contacts = {
    "Name": '',
    "Age": '',
    "Phone #": '',
    "More_contacts": [{
                                        "Name1": '',
                                        "Age1": '',
                                        "Phone #1": '',
    },
                       {
                                        "Name2": '',
                                        "Age2": '',
                                        "Phone #2": '',
    },
                       {
                                        "Name3": '',
                                        "Age3": '',
                                        "Phone #3": '',
    },



    ]
}
x = 0




#task 2
# For printing dictionary well

def print_dict():
    print('\n\n--- CONTACT INFORMATION ---')
    print(f'Name: {contacts.__getitem__("Name")}')
    print(f'Age: {contacts.__getitem__("Age")}')
    print(f'Phone #: {contacts.__getitem__("Phone #")}')
    print(f'\n --- Three Contacts ---')

    cont = contacts["More_contacts"]

    for i in range(3):
        print(F'--- CONTACT {i}---')

        for key, values in cont[i].items():
            print(f'{key} : {values}')
        print('')


# 1 - Updating the Dictionary Section

def input_contact_1():
    print('--- USER 1 ---')


    # 2 - The User 1 Input Profile

    name = str(input('What is your name? '))
    age = str(input('How old are you? '))
    phone_num = str(input("What is your phone number? (5 digits) "))

    while len(phone_num) != 5:  # Pretty smart
        phone_num = str(input("What is your phone number? (5 digits) "))


    contacts["Name"] = name
    contacts["Age"] = age
    contacts["Phone #"] = phone_num


    print('\n---- Time to add 3 Contacts----') # 3 - User add 3 Contacts Section
    print('')


    # 4 - Make user enter any key to add 3 contacts
    print("\n --- ADD THREE CONTACTS---")
    user_question_3_contact = input('Enter any number to add contact: ')


    x = 0

    if user_question_3_contact.isdigit():
        print(f'--- CONTACTS ---')

        while x <= 2 :
            print(f'\n\n--- CONTACT #{x+1} ---')

            # 5 - INPUT of each contact of the user1

            name = str(input('What is his/her name? '))
            age = str(input('How is old he/she? '))
            phone_num = str(input("What is his/her phone number? (5 digits) "))

            while len(phone_num) != 5:
                phone_num = str(input("What is his/her phone number? (5 digits) "))


            # 6 - Below is just connected to the top [input].
            contacts["More_contacts"][x][f"Name{x+1}"] = name
            contacts["More_contacts"][x][f"Age{x+1}"] = age
            contacts["More_contacts"][x][f"Phone #{x+1}"] = phone_num

            x += 1

        # 8 - ask whether user wants to see his info:

        see_info = input('Enter any number to see your Contact Information: ')

        if see_info.isdigit():
            print_dict()

input_contact_1()


def notes_to_self():
    print("""
    Use functions well, commenting
    I think this can be organized well, so do that
    - assign the dictionary path to a variable and use that instead. That way, it will be cleaner
    - Use functions well""")

