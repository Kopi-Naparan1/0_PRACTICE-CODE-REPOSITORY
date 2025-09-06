# 1 PRINT NAME, FAVORITE QUOTE
# print('Kopi')
# print('I am building the best version of my self, one choice at a time')



#2 age,name, height, like python?

# age = 18
# name = 'Kopi'
# height = 161.2
# do_you_like_python = True
#
# print(type(age))
# print(type(name))
# print(type(height))
# print(type(do_you_like_python))

#3 input function

# user_input_fav_color = input(f'What is your favorite color? ')
# print(f"Oh! You like color {user_input_fav_color}?")




#4 Operators

def addition(x,y):
    if x > y:
        message = (f'{x} is greater than {y}')
    elif x < y:
        message = (f'{x} is less than {y}')
    elif x == y:
        message = (f'{x} is equals to {y}')

    result = x + y

    print(message)
    print(f'{x} + {y} = {result}\n')

def subtraction(x,y):
    if x > y:
        message = (f'{x} is greater than {y}')
    elif x < y:
        message = (f'{x} is less than {y}')
    elif x == y:
        message = (f'{x} is equals to {y}')

    result = x - y

    print(message)
    print(f'{x} - {y} = {result}\n')

def multiplication(x,y):
    if x > y:
        message = (f'{x} is greater than {y}')
    elif x < y:
        message = (f'{x} is less than {y}')
    elif x == y:
        message = (f'{x} is equals to {y}')


    result = x * y

    print(message)
    print(f'{x} x {y} = {result}\n')

def division(x,y):
    if x > y:
        message = (f'{x} is greater than {y}')
    elif x < y:
        message = (f'{x} is less than {y}')
    elif x == y:
        message = (f'{x} is equals to {y}')

    result = x / y

    print(message)
    print(f'{x} / {y} = {result.__round__(2)}\n')

# addition(4,5)
# subtraction(6,5)
# multiplication(7,6)
# division(8,7)

#5 Control Flow

# print('---You must enter your name to determine if you can ride it---')
# user_age = int(input('What is your age: '))
#
# if user_age < 0:
#     print('You are not yet born!')
# elif user_age < 18:
#     print("You are a minor")
# elif user_age <= 65:
#     print('You are an adult')
# elif user_age >= 66:
#     print("You are a senior citizen")
# else:
#     print('Please enter an integer')




#6 Loops


#for loop


# for x in range(1,11):
#     if x == 5:
#         continue
#     if x == 7:
#         print(f"Count  Ascending: {x}")
#         break
#     else:
#         print(f"Count  Ascending: {x}")





#while loop

u = 100

# while u > 0:
#     if u != 66 and u != 50:
#         print(f'count down {u} ')
#     if u == 66:
#         u -= 1
#         continue
#     if u == 50:
#         print(f'Half way there. {u}')
#     u -= 1




# 7 Functions and Parameters

# def greet(name):
#     print(f'Hey there {name}')
#
# def multiply(x,y):
#     return (x * y)
#
#
#
# y = 2
# print(multiply(5,y))
# greet('Kopi')


# 8 Basic String Manipulation

# first_name1 = "Kopi"
# first_name2 = "Anan"
# last_name = "Naparan"
# full_name = f'{first_name1} {first_name2} {last_name}'
#
#
# print(full_name) #1st Task
# reversed_name = ''.join(reversed(full_name)) #2nd Task
# print(reversed_name) #3rd Task
#
#
# a = 'a' # 4th task
# determine = a in full_name
# print(determine)


#9 Lists and Indexing

# favorite_foods = ['Banana','Apple','Orange','Durian','Grapes'] # 1st task
#
# print(favorite_foods[0])
# print(favorite_foods[4]) #2nd task
#
#
# favorite_foods[1] = 'Papaya' #3rd task
#
# favorite_foods.append('Guava') #4th task
#
# favorite_foods.remove('Banana') #5th task
#
# print(sorted(favorite_foods)) #6th task


## Tuple & sets


# TUPLE
tuple1 = ('Hacksawridge', "Endgame", 'Thor') #1st task

print(tuple1[1]) #2nd task


# SET

set1 = {'Chess', 'Guitar', 'Jogging', 'Riding', 'Reading'} # 3rd task
set1.add('Swimming') # 4th task

set1.remove('Chess') # 5th task

























