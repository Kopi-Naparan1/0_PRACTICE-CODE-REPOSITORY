from functools import reduce
import sys
import os
from datetime import datetime
import math

sys.path.append(r"C:\KOPI ANAN PASCO NAPARAN\PROGRAMMING\Python Course\3 Intermediate Concepts")
import math_formulas





#1 Function
def flexible_calculator(*args,**kwargs):

    print('--- Welcome to Calculator---')
    total = 0
    for value in kwargs.values():
        if value == "+":
            for arg in args:
                total = total + arg
            return total

        if value == "-":
            for arg in args:
                total = total - arg
            return total

        if value == "*":
            for arg in args:
                total = total * arg
            return total

        if value == "/":
            divide = reduce(lambda x, y: x / y , args)
        return divide
def factorial(x):
    if x == 1:
        return x
    else:
        y = x * factorial(x - 1)
        return y



#2 Scope and Lifetime
def one():
    x = 1
    print(x)

    def two():
        nonlocal x
        x = 2
        print(x)

        def three():
            nonlocal x
            x = 3
            print(x)

            def four():
                nonlocal x
                x = 4
                print(x)
            four()
        three()
    two()



#3 Lambda
def assignment_3_1():
    #capitalizing my list
    list_names = ['kopi','anan','naparan','john','lloyd','cruz']
    capitalized_names = list(map(lambda x: x.capitalize(), list_names))
    return capitalized_names
def assignment_3_2():
    #if it is a palindrome, then it goes to printing
    list_words = ["banana", "apa", 'drd', 'brb', 'ahaha','canac']
    palindromes = filter(lambda x: x == ''.join(reversed(x)), list_words)
    return list(palindromes)
def times_3():
    # I have to make a list first, before cubing it :)
    list_numbers: list[int] = [x for x in range(1,11)]
    times3_numbers = map(lambda x: x * 3, list_numbers)
    return list(times3_numbers)



#4 Map, Filter, Reduce
def celsius_to_fahrenheit():
    list_celsius = [23,12,56,32,33,22,11,19,18,2]
    to_fahrenheit = map(lambda x: x * 9/5 + 32, list_celsius)
    return list(to_fahrenheit)
def even_num():
    numbers = [x for x in range(1,21)]
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    return list(even_numbers)
def summing():
    list_numbers = [x for x in range(1,51)]
    summed_numbers = (reduce(lambda x, y: x + y, list_numbers))
    return summed_numbers


# 5 modules and import system
def math_testing():
    print(math_formulas.area_rectangle(55,8))
    print(math_formulas.area_trapezoid(5,6,23))


# 6 Working with the standard library
def current_time():
    now = datetime.now()
    return now
def folder_paths():

    folder_path = r'C:\KOPI ANAN PASCO NAPARAN\PROGRAMMING\Python Course\3 Intermediate Concepts'

    # List all files and directories
    files_and_directories = os.listdir(folder_path)
    print(f'{files_and_directories}')

    # # To filter only files, you can check if it is a file:
    # files_only = [file for file in files_and_dirs if os.path.isfile(os.path.join(folder_path, file))]
    # print("Files only:", files_only)
def math_import_test():
    print(f'Square root of 10: {math.sqrt(10).__round__(2)}')
    print(f'logarithm of 10: {math.log(10).__round__(2)}')










def main():

    #1
    # print('One operation only')
    # print(flexible_calculator(5,5,5,5,operation ='/'))
    # print(factorial(4))

    #2
    # one()

    #3
    # assignment_3_1()
    # print(assignment_3_2())
    # print(times_3())


    #4
    # print(celsius_to_fahrenheit())
    # print(even_num())
    #print(summing())

    #5
    # math_testing()

    #6
    # print(current_time())
    # folder_paths()
    # math_import_test()

    #7


if __name__ == "__main__":
    main()