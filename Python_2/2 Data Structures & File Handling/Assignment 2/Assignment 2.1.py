import os


## 3 LC = List Comprehension
# list = [x for x in range(1,21)] # task 1 - make a list using LC
#
#
# list1 = [y for y in list if y % 2 == 0] # task 2 - use prev list - make - even list.
# print(list1)
#
#
# list3 = [z ** 2 for z in list if z % 3 == 0] # num that div by 3 will be squared
#
# print(list3)
import json

##4 String Formatting

# name = 'Kopi'
# age = 18.23426
# city = 'Valencia City'
#
# print(f'{name}, {age} years old, who lives in {city} \n')
#
# print(f'{name:^10}')
# print(f'{age:^+10.2f}')
# print(f'{city:^.10}')



### 5 File Handling


# f = open("File 1.txt", "r")
# print(f.readline())




# 7 Error Handling ( connection to #5 )

# try:
#     f = open("File 2.txt", 'r')
#     print(f.read())
#
# except SyntaxError and FileNotFoundError:
#     print('File not found')
#
# finally:
#     f.close()



# 5.1 appending

# text_test1 = open("Text1", "a")
# text_test1.write('Whats up!\n')
# text_test1.close()
#
# text_test2 = open("Text1", "r")
# print(text_test2.read())
# text_test2.close()




# 5.2 writing

text_test3 = open("Apple 1.0", "w")
text_test3.write('Deleted 1')
text_test3.close()


text_test4 = open("Apple 1.0", 'r')
print(text_test4.readline())
text_test4.close()


# 5.3 File Existence

if not os.path.exists("Apple 2.0"):
    f1 = open("Apple 2.0", 'x')
    f1.close()

elif os.path.exists("Apple 2.0"):
    f2 = open("Apple 2.0", "w")
    f2.write('Hahaha Apple 2')


## Deletion

if os.path.exists("Apple 1.0"):
    os.remove('Apple 1.0')
else:
    print('The file does not exist')





def note_to_self():
    print("""
    - Try redoing it all again from scratch but now, apply your previous learnings
    """)




