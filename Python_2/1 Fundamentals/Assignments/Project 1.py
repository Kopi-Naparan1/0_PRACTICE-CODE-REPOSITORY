### Project: "Simple Personal Profile Creator"




print('----- WELCOME TO THE SIMPLE PERSONAL PROFILE CREATOR-----') #1ST TASK - GREAT THE USER



while True:
    print('\n---PROFILE SECTION---')
    #2ND TASK - PERSONAL DETAILS
    f_name = str(input('What is your first name? '))
    l_name = str(input('What is your last name? '))
    full_name = f'{f_name.capitalize()} {l_name.capitalize()}'


    fav_color = str(input('What is your favorite color? '))
    three_hobbies = []
    hobby1 = []
    hobby2 = []
    hobby3 = []

    age = int(input('What is your age? '))



    # 3rd task - Flow statement
    if age < 0:
        print('Please be born first!')
    elif age < 18:
        print('Not allowed. Minor!')
    elif age < 66:
        print('Allowed: Adult')
    elif age > 65:
        print('Not Allowed: Too old')
    else:
        print('Please try again.')



    #Three Hobbies
    i = 3
    print('\n\n---Please Input your three hobbies---')
    while i > 0:
        if i == 3:
            hobby = str(input('What is your 1st hobby? '))
            hobby1.append(hobby.capitalize())
            i -= 1
        if i == 2:
            hobby = str(input('What is your 2nd hobby? '))
            hobby2.append(hobby.capitalize())
            i -= 1
        if i == 1:
            hobby = str(input('What is your 3rd hobby? '))
            hobby3.append(hobby.capitalize())
            i -= 1
    print('----------')



    # 4th Task - Function

    def display_profile(name,age,color,*hobbies):
        print('\n\n----- PROFILE -----')
        print(f'Full Name: {name}')
        print(f'Age: {age}')
        print(f'Favorite color: {color}')
        print(f"These are the three {name}'s Hobbies: ")

        a = 3
        for hobby in hobbies:
            if a == 3:
                print(f'\tFirst Hobby : {hobby}')
            if a == 2:
                print(f'\tSecond Hobby : {hobby}')
            if a == 1:
                print(f'\tThird Hobby : {hobby}')
            a-=1
        print('--------------')
        print('')

    display_profile(full_name,age,fav_color,hobby1[0], hobby2[0], hobby3[0])



#5 Using a loop to user interact
    user_input_changes = str(input('want to change a Hobby? (y/n) '))
    user_input_changes = user_input_changes.lower()

    # This part is for the user to change 1 hobby and then display.
    if user_input_changes == 'y':
        while True:
                change_hobby = int(input(f"What hobby would you like to remove? "
                                         f"\n 1 {hobby1[0]},"
                                         f"\n 2 {hobby2[0]},"
                                         f"\n 3 {hobby3[0]}"
                                         f"\n(Number only): "))


                if change_hobby == 1: #HOBBY 1
                    popped1 = hobby1.pop(0)
                    to_change = str(input('What should I change it with? '))
                    hobby1.append(to_change)
                    display_profile(full_name,age,fav_color,
                                    hobby1[0], hobby2[0], hobby3[0])
                    break

                if change_hobby == 2: #HOBBY 2
                    popped2 = hobby2.pop(0)
                    to_change = str(input('What should I change it with? '))
                    hobby2.append(to_change)
                    display_profile(full_name,age,fav_color,
                                    hobby1[0], hobby2[0], hobby3[0])
                    break

                if change_hobby == 3: #HOBBY 3
                    popped3 = hobby3.pop(0)
                    to_change = str(input('What should I change it with? '))
                    hobby3.append(to_change)
                    display_profile(full_name,age,fav_color,
                                    hobby1[0], hobby2[0], hobby3[0])
                    break
    break




### 70% DONE April 30
# TO-DP

# 1. all inputs, what if some user won't follow it or mis type? it'll cause an
# error, so you have to put if statements there.

# 2. Section 5 input is still not done. it needs some if statements if not

# 3. Only 1 hobby is supported for removing.









