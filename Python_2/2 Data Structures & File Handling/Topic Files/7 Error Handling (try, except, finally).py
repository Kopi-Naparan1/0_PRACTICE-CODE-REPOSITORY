


try:
    user = int(input('Enter a number: '))
    print(1 / user )
except ZeroDivisionError:
    print('You moron. You can not divide with zero')
except ValueError:
    print('Letters are not numbers. Try again ')
except Exception:
    print("We still don't know what's going on!")
finally:
    print('Rest assured.This will work')