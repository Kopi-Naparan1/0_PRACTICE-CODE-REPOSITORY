## File Handling

def divide(x, y):
    return print(x / y)

try:
    while True:
        user1 = int(input('Enter the first num: '))
        user2 = int(input('Enter the second num: '))
        divide(user1, user2)
        break
except ValueError:
    print('Please enter a number!')
except ZeroDivisionError:
    print("Error. Don't divide it by 0")
finally:
    print('Thankyou for using the calculator')




