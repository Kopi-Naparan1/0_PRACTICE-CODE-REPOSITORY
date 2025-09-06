from functools import reduce

##lambda



#practice 1
# add2 = lambda x , y : (x + 1) * y
#
# result = add2(5,2)
# print(result)



#practice 2
#using for loop

# number = [1,2,3,4,5,6,7,8,9,10]
# squared = []
#
#
# for num in number:
#     squared.append(num**2)
#
# print(squared)


# practice3
# using lambda


# number2 = [1,2,3,4,5,6,7,8,9,10,11,12]
# number3 = [2,3,4,5,6,7,8,9,10,11,12,13]
# squared2 = list(map(lambda x, y: (x+y)**2, number2, number3)) #map is like putting a list as an argument
#
# print(squared2)



#practice4
#filter function

# max_num = 50
# number4 = [x for x in range(1, max_num+1)]
# number4_even = list(filter(lambda x: x % 2 == 1, number4)) #filter is looking for the True
# print(number4_even)


#practice5
#sort


# test5 = (1,'a','apple'), (2,'b','banana'), (3,'c', 'cat')
#
# sort_test5 = sorted(test5, key=lambda x: x[1] + x[2]) # "key" works as a switch to customize how to sort it.
# print(sort_test5)



practice6
reduce

number6 = [1,2,3,4,5,6,7,8,9,10]
looped = []

reduce = reduce(lambda storage, x: storage + x, number6)
looped.append(reduce)
print(looped)





#practice 7

# number7 = [5,4,6,2,1]
#
# reduced2 = reduce(lambda storage, x: storage if storage > x else x, number7)
#
# print(reduced2)

