## ARGS and KWARGS

#
#ARGS1

# def test1(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
#
# iteration1 = test1(5,5,5)
# print(iteration1)
#


# #ARGS2
#
# def test2(*args):
#     for arg in args:
#         print(arg, end= " ")
#
#
# iteration2 = test2("Mr", "Kopi")
# print('\n')
#
#
# ##KWARGS
#
#KWARGS1
# def test3(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
# test3(money1= 100,
#       money2= 200,
#       money3= 300,
#       money4= 400,
# )
#
#
#
# #ARGS AND KWARGS
# #
# def shipping_distination(*args,**kwargs):
#     print('\n')
#     for arg in args:
#         print(arg, end=" ")
#     print('\nLOCATION: ')
#
#     for key, value in kwargs.items():
#         print(f'\t{key} : {value}')
#
# shipping_distination("Mr.", "Kopi", "Naparan", "II",
#                      province= "Bukidnon",
#                      city= "Valencia City",
#                      purok= 4,
#                      street= "Mt. Kitanglad street",
#
#                      )
# # print('')

#RECURSION


#1 - recursive
# def walk(steps):
#     for step in range(1, steps+1):
#         print(f"You've taken {step} step/s")
#
# walk(10)


###FACTORIAL - iterative - practice
def factorial(n):
    total = 1
    if n >= 0:
        for n in range(1, n + 1):
            total = n * total
        return total
    elif n <= -1:
        x = ('Negative number is not allowed')
        return x

print(factorial(10))
