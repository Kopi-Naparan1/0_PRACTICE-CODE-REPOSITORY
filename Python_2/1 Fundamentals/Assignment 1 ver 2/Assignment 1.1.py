# 5:38 pm , march 15, 2025

def assignment1(): # START= 5:40 pm --- DONE=6:05 PM = 25 minutes
    contacts = {}

    def add_contact():
        name = input('Name: ').lower().strip()
        number = int(input('Contact #: '))

        if name in contacts.keys() or number in contacts.values():
            print(f"Contact information already Exists.")
            return
        else:
            contacts[name] = number
            print('Contact added')

    def view_contact():
        print('--- ALL CONTACTS ---')
        for k, v in contacts.items():
            print(f'{k}: #{v}')
        print('-' * 20)
        print('')

    def main_assignment_1():
        while True:
            choice = input("""
            CHOOSE
                [1] Add a contact
                [2] View a contact
                [3] Quit
                CHOICE: """)

            if choice == '1':
                add_contact()

            elif choice == '2':
                view_contact()

            elif choice == '3':
                print('QUITING...')
                break


    main_assignment_1()




def assignment2(): # START = 6:08 pm --- DONE = 6:19pm = 11 minutes
    from random import randint

    def assignment2_main():
        print('--- WELCOME TO NUMBER GUESSING GAME ---\n\n\n')
        print("--- GUESS THE NUMBER 1 - 50")

        random_number = randint(1, 50)

        while True:
            try:
                print('')
                user_guess = int(input('Guess the number:  '))
                print('')

                if user_guess > random_number:
                    print('Lower than that!')
                elif user_guess < random_number:
                    print('Higher than that!')
                elif user_guess == random_number:
                    print('=' * 30)
                    print(f'You guessed the random number [{random_number}]. Congrats!!!')
                    print('=' * 30)
                    break

            except SyntaxError:
                print('Input an INTEGER')

    assignment2_main()


def assignment3(): # START = 6:24 pm --- DONE = 7:50
    from string import punctuation

    def ask_sentence():
        sentence = input('Input a sentence: ').lower()
        return sentence

    def remove_extra_spaces(sentence: str):
        if '  ' in sentence:
            extra_spaces = sentence.count("  ")
            sentence = sentence.replace('  ', '')
            print(f'Cleaned {extra_spaces} extra spaces')
            return sentence, extra_spaces

        else:
            print('No extra spaces were detected')
            extra_spaces = 0
            return sentence, extra_spaces

    def remove_punctuation(sentence):
        original = len(sentence)
        cleaned_sentence = ''.join(char for char in sentence if char not in punctuation)
        new = len(cleaned_sentence)
        result = original - new
        print(f'Cleaned {original-new} punctuation/s.')
        return cleaned_sentence, result

    def assignment3_main():
        original_sentence = ask_sentence()
        print(f"Original Sentence Length: {len(original_sentence)}")
        new_sentence_space, extra_spaces = remove_extra_spaces(original_sentence)
        new_sentence_punc, punct = remove_punctuation(new_sentence_space)
        print(f"New Sentence Length: {len(new_sentence_punc)}")
    assignment3_main()


# =========================
# Re-do of Assignment 3
# =========================

def assignment4(): # Start = 10:00 pm # End = 11:35 pm

    from string import punctuation

    def ask_user_sentence() -> str:
        """Ask the user for a sentence, return that sentence to the main"""

        user_input_sentence = input('Input a sentence: ')
        return user_input_sentence

    def remove_punctuations(sentence) -> str :
        """Takes 1 argument,-> argument is a the string ,return it as no punctuations """

        while True:
            for p in punctuation:
                if p in sentence:
                    sentence.replace(p, '')
            break
        return sentence


    def remove_extra_spaces(sentence) -> str:
        """Takes 1 argument -> string returns as no extra spaces"""
        while "  " in sentence:
            sentence = sentence.replace("  ", '')
        return sentence

    def convert_lowercase(sentence) -> str:
        """take 2 arguments,
         first argument is a the string ,return it as lowercased
         second argument will be the counter, return it as updated argument"""
        sentence = sentence.lower()
        return sentence

    def count_length_original(original_sentence: str) -> int:
        """count the length of the original, return the length number"""
        length_original = len(original_sentence)
        return length_original

    def count_length_updated(updated_sentence: str) -> int:
        """Count the length of the original string and return the length of it  """
        length_updated = len(updated_sentence)
        return length_updated

    def display_length_original_and_updated(original, updated, original_string, updated_string) -> str:
        """Takes 2 arguments, Display both of those lengths and their difference,
        return it with a difference from those 2 argument"""

        display = (
            f'{'=' * 30}\n'
            f' LENGTH OF THE SENTENCES \n\n '
            f'Original Sentence: [{original_string}]\n'
            f'Original Sentence #: {original}\n'
            f'{'-' * 30}\n'
            f'Updated Sentence: [{updated_string}]\n'
            f'Updated Sentence #: {updated}\n'
            f'Difference: {original - updated}\n'
            f'{'=' * 30}\n'
        )
        return print(display)






    def assignment4_main():
        """Manage all the functions in assignment 4"""
        print('--- Welcome to Sentence Cleaner---')

        #Assigning into variables
        user_sentence_string = ask_user_sentence() # Converts the return string into the variable
        user_sentence_string_original = user_sentence_string # just want to make this original usable

        #Counting the original string
        original_string_count = count_length_original(user_sentence_string_original)

        #Cleaning the sentence
        user_sentence_string = remove_extra_spaces(user_sentence_string) #The return is converter into the variables for feasiblity
        user_sentence_string = remove_punctuations(user_sentence_string)
        user_sentence_string = convert_lowercase(user_sentence_string)

        # Counting the updated string
        updated_string_count = count_length_updated(user_sentence_string)

        # Displaying the difference and the original and updated strings
        display_length_original_and_updated(original_string_count, updated_string_count,
                                            user_sentence_string_original,user_sentence_string )

    assignment4_main()


def assignment5(): #5pm
    def make_food() -> list[str]:
        """
        step 1
        :return: list of 3 foods
        """
        food = ['Banana', "Apple", "Orange"]
        return food


    def display_foods(foods : list[str]) -> str:
        """
        step 2
        It just shows the food to the users
        :param foods: take that list of string and loop it for display
        :return: str
        """
        i = 1

        for food in foods:
            print(f"\t[{i}] {food}")
            i += 1


    def voting_for_food() -> list[dict]:
        """
        step 3
        This where voting happens
        : voters
        :return: list of dictionary of the foods including their votes the tally
        """
        list_votes = []

        voters = 1

        while voters != 6:
            user_vote = int(input(f"Hey #{voters}, which one would you choose? "))

            if user_vote == 1:
                one = {"Banana": 1}
                list_votes.append(one)
            elif user_vote == 2:
                two = {"Apple": 1}
                list_votes.append(two)
            elif user_vote == 3:
                three = {"Orange": 1}
                list_votes.append(three)
            voters += 1

        return list_votes

    def final_tally_(tally) -> dict :
        """
        This is the final part
        :param tally: dict
        :return: str
        """

        banana  = 0
        apple = 0
        orange = 0


        for t in tally:
            for key, value in t.items():
                if key == "Banana":
                    banana += 1
                elif key == "Apple":
                    apple += 1
                elif key == "Orange":
                    orange +=1


        last_dict = {"Banana" : banana,
                     "Apple" : apple,
                     "Orange": orange}

        return last_dict

    def diplay_winner(tally):
        print("-" * 30)
        print("Here's the result: ")

        print("-" * 30)
        i = 1
        for key, value in sorted(tally.items(), key= lambda item: item[1],reverse=True):
            print(f'Rank [{i}] - {key} : {value} votes')
            i += 1
        print("-" * 30)







    def assignment5_main():

        print('--- Welcome to Food Survey---')

        food_list = make_food() # convert in into a variable
        display_foods(food_list) # I passed the list of food here to display it
        print('Here are the foods: ')
        dict_of_votes = voting_for_food()
        final_display = final_tally_(dict_of_votes)
        diplay_winner(final_display)

    assignment5_main()












def main():
    # assignment1()
    # assignment2()
    assignment3()
    # assignment4()
    # assignment5()






if __name__ == "__main__":
    main()