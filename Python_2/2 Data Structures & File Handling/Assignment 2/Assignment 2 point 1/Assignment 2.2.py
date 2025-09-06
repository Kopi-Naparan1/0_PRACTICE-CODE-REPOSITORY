## Learn how to do the file handling
## Text, CSV, and JSON

import json
import csv


### TEXT

# 1 Relative File Path

# txt_data_1 = 'Apple'
#
# file_path_1 = 'Banana'
#
# with open(file_path_1, 'w') as a: # Name of the file
#     a.write(txt_data_1)
#     print(f' "{file_path_1}" was created')
#
#
#
# print(file_path_1)



# 2 Absolute File Path

# txt_data_2 = 'Cat'
#
# file_path_2 = 'C:/Users/Admin/Desktop/Dog.txt'
#
# with open(file_path_2, 'w') as b:
#     b.write(txt_data_2)
#     print(f'{file_path_2} was created! ')



# 3 Using List

# letters = ['a','b','c','d','e']
#
#
# txt_data_3 = 'Elephant'
#
# file_path_3 = 'C:/Users/Admin/Desktop/Falcon.txt'
#
# with open(file_path_3, 'w') as c:
#     for letter in letters:
#         c.write(f'{letter}\n')
#     print(f'{file_path_3} was created! ')



### JSON

# dictionary = {'a' : 'one',
#               'b' : 'two',
#               'c' : 'three',
#               }
#
# dict_file = 'C:/Users/Admin/Desktop/Goat.json'
#
# try:
#     with open(dict_file, 'w') as g:
#         json.dump(dictionary, g, indent= 5)
#         print(f'{dict_file} was created - JSON 1')
# except FileNotFoundError:
#     print('file was not found')




### CSV

# csv_file = [['one','two','three'],
#             ['a','b','c'],
#             [1,2,3],]
#
#
# filepath_csv1 = 'C:/Users/Admin/Desktop/Horse.csv'
#
# try:
#     with open(filepath_csv1, 'w', newline='') as h:
#         x = csv.writer(h)
#
#         for csv1 in csv_file:
#             x.writerow(csv1)
#
#         print(f'{x} was created')
#
# except FileNotFoundError:
#     print('file was not found')



## Assignment 1 - CSV


# csv_assign_1 = [["name","Kopi"],
#                 ["age", "18"],
#                 ["city", "Valencia City"]]
#
# file_path_assign_csv_1 = 'data.csv'
#
# with open(file_path_assign_csv_1,'w', newline='') as assign:
#     write = csv.writer(assign)
#
#     for i in csv_assign_1:
#         write.writerow(i)


## Assignment 2 - JSON - using dump

# json_dict_assignment = {
#     "name": "Kopi",
#     "age": 18,
#     "city": "Valencia",
# }
#
# json_file_path_assignment = 'assignment_json.json'
#
# with open(json_file_path_assignment,'w') as x:
#     json.dump(json_dict_assignment,x, indent=5)



## JSON using Load


with open('assignment_json.json', 'r') as y:
    x = json.load(y)
print(x)



