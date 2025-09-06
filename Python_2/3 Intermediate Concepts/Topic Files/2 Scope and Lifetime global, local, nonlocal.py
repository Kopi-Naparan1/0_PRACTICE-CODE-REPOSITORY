#practice 1

# x = 1
#
# def test():
#     global x
#     x = 20
#     print(f'This smaller box = {x} apples')
#
# (test())
# print(f'This bigger box = {x} apple/s')


#practice 2


# x = 1
#
# def test2():
#     global x
#     x = 2
#     print(f'This should be 2 = {x}')
#
#     def test3():
#         global x
#         x = 3
#         print(f'This should be 3 = {x}')
#     test3()
#
# #1st time
# print(f'This should be 1 = {x}') #This is to test whether the 1 will be = to 1. with respect to global
# (test2())# The idea is that the 1st print is independent. So I have to call the function to print the 2,3
#
# print('')
#
# #2nd time
# print(f'This should be 1 = {x}') #testing it again
# (test2())



#practice 3

y = 1

def two():
    # global y
    y = 2
    def three():
        # global y
        y = 3
        print(f'three = {y}') #this prints first because before any "prints" you call another function
    three()
    print(f'two = {y}') #after "three" this prints the "Two"

two()
print(f'one = {y}') #function is done, then this prints.








