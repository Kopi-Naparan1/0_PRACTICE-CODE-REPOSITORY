## JSON

import json



# # JSON STRINGS
# Py = {
#     'Count': 3,
#     'Left': 9,
#     'All': 12,}
#
# JSON = """{
#     "Count": 3,
#     "Left": 9,
#     "All": }"""
#
#
# Py_JSON = json.dumps(Py)
# print(Py_JSON)
#
# JSON_Py = json.loads(JSON)
# print(JSON_Py)


#JSON FILES


with open('PRACTICE1.json', 'r') as file_1: #JSON to Python
    json_to_python_1 = json.load(file_1)
print(json_to_python_1)


with open("PRACTICE2.json", 'w') as file_2: # Python to JSON
    json.dump(json_to_python_1, file_2)

