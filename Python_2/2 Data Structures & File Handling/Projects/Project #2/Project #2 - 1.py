import json
import os


### Section: 1 - The Json file - I made this so that I can store my info to the json file

JSON_1_DATA = {} #This is the original dictionary
JSON_FILE_PATH = 'Contacts1.json'


if os.path.exists(JSON_FILE_PATH):
    with open(JSON_FILE_PATH,'r') as file1:
        try:
            JSON_1_DATA = json.load(file1)

        except json.JSONDecodeError:
            JSON_1_DATA = {}
        print(f'{JSON_FILE_PATH} was found and loaded')

else:
    with open(JSON_FILE_PATH, 'w') as file1:
        json.dump(JSON_1_DATA, file1, indent=5, sort_keys=True)
        print(f'{JSON_FILE_PATH} was created\n')

def file_help1(): # ?
    with open(JSON_FILE_PATH, 'w') as file1:
        json.dump(JSON_1_DATA, file1, indent=5, sort_keys=True)
        print(f'{JSON_FILE_PATH} was created\n')


### Section: 2 The user input - I used function instead so that logic will be broken into chunks

# >2.1 the purpose of this function is to initialize the code and pass the result to
# the >2.2 function

def ask_info():
    while True:
        name = input('\n\n\nWhat is your full name? (type "q" to quit) ')

        if name.lower() == 'q':
            print(f'POWER OFF')
            break
        elif name == '':
            print('--ASSUMED AS CONTINUING--')
            name = 'UNKNOWN'

        email = input('What is your email address ')
        phone = input('What is your phone number? ')
        city = input('What city do you live in? ')

        append_info(name,email,phone,city) #CONNECTS TO 2.2

# >2.2 - the purpose of this function is to update the info in the original dictionary

def append_info(a,b,c,d):

    JSON_1_DATA[a] = {
        "email" : b,
        "Phone #" : c,
        "City" : d,
    }

    file_help1()
    print('Contact Saved')



### Section: 3 User searching for contacts
# THIS IS AFTER THE USER QUIT THE FIRST PART (SECTION 1,2)

# 3.1 This will layout the contacts keys (Username of the contact information) -
def layout_contacts():
    keys_contacts = [keys for keys in JSON_1_DATA.keys()]
    print(keys_contacts)

### Section: 4 Updating infos of a user

def update_info(searching_input):

    print("'1' = searching_input "
          "\n'2' = 'email' "
          "\n'3' = 'Phone #' "
          "\n'4' = 'City'")

    choice = str(input('Pick a number: '))

    if choice == '1':
        ask_1 = input('What should be its new name? ')
        JSON_1_DATA[ask_1] = JSON_1_DATA.pop(searching_input)
        file_help1()
        print('done')


    elif choice == '2':
        ask_2 = input('What should be its new email?' )
        JSON_1_DATA[searching_input]['email'] = ask_2

        file_help1()

    elif choice == '3':
        ask_3 = input("What should be its new Phone #? ")
        JSON_1_DATA[searching_input]['Phone #'] = ask_3

        file_help1()

    elif choice == '4':
        ask_4 = input("What should be its new City? ")
        JSON_1_DATA[searching_input]['City'] = ask_4

        file_help1()





# 3.2 I want to make user get the keys in the contact
def searching_key():

    layout_contacts()

    while True:
        searching_input =  input('\nWho do you want to search? (type "q" to quit): ')
        if searching_input.lower() == 'q':
            print('Power Off')
            return
        if searching_input in JSON_1_DATA:
            break
        else:
            print(f'{searching_input} is not found! ')





    ask_to_update = input('Do you want to update information? (y/n): ') #this proceeds to Section 4
    ask_to_update = ask_to_update.lower()
    if ask_to_update == 'y':
        print('--- UPDATING INFORMATION ---')
        update_info(searching_input)

    elif ask_to_update.lower() != 'y':
        print('Bye')



## 3.3 This prompts the user to search (initialize the section 3)





def main():
    ask_info()

    user_search_contact = str(input('Do you want to search contacts: (y/n)'))

    if user_search_contact.lower() == 'y':
        searching_key()
    else:
        print('Okay bye')

if __name__ == "__main__":
    main()