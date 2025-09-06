#For Loops




#1
# for x in range(2,101, 2):
#     if x == 50:
#         print(x)
#         print(f'We have reach {x}')
#     else:
#         print(x)


#2
x_list = '128-12385=1245l620197'

cleaned = filter(lambda x: , x_list)
print(cleaned)

# While Loops


#1
# name = input('What is your name? ')
#
# while name == '':
#     print("You don't have any name?")
#     name = input('What is your name?')
# print(f'Your name is {name}.')


#2
# age = int(input('What is your age? '))
#
# while age < 0:
#     print('Your a God!')
#     age = int(input('What is your age? '))
# print(f'You are {age} year/s old. ')


#3


# like = input('What are the things that you like? (Press x to quit) ')
#
# while not like == 'x':
#     print(f'So you like {like}. That is great!')
#     like = input('What are the things that you like? (Press x to quit)')
# print('Bye-bye')


#4

# number = int(input('Enter a number between 1-10: '))
#
# while number <= 0 or number >= 11:
#     print('Embecile! ')
#     number = int(input('Enter a number between 1-10:'))
# print("You're Smart!")