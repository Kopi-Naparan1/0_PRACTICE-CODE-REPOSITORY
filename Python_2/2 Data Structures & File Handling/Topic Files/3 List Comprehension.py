
# numbers
# quadruple = [variable * 4 for variable in range(1,11)]
# print(quadruple)
#
# double = [x-expression for x in iterable]


#list of strings

#1 - long
# words = ['one', 'two', 'three', 'four', 'five']
# uppercase_words = []
#
# for word in words:
#     word = word.upper()
#     uppercase_words.append(word)
#
# print(words)
# print(uppercase_words)


#2 short
# words = ['one', 'two', 'three', 'four', 'five']
# uppercased = [word.upper() for word in words]
#
# print(words)
# print(uppercased)



# if condition


# numbers = [1,2,3,4,5,6,7,8,9,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,10]
#
#
#
# positive = [pos for pos in numbers if pos >= 0]
# print(sorted(positive))
#
# negative = [neg for neg in numbers if neg <= 0]
# print(sorted(negative))
#
# even = [e for e in numbers if e % 2 == 0]
# print(sorted(even))
#
# odd = [o for o in numbers if o % 2 == 1 ]
# print(sorted(odd))



# last exercise


grades = [12,66,33,56,27,8,34,19,89,86,80,78,90,94,99,67,78,83,92,98,100]
passed_grades = []
failed_grades = []


passing_grades = [passed_grades.append(Pass) for Pass in grades if Pass >= 75]
print(sorted(passed_grades))
print(f'Passed Grades #: {len(passed_grades)}')

failing_grades = [failed_grades.append(fail) for fail in grades if fail <= 74]
print('')
print(sorted(failed_grades))
print(f'Failed Grades #: {len(failed_grades)}')