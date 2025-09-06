
#1 Example

# chords = [
#     {
#     'Root' : 'C',
#     '3rd' : 'E',
#     '5th' : 'G'
#     },
#
#     {
#     'Root' : 'G',
#     '3rd' : 'B',
#     '5th' : 'D'
#     },
#
#     {
#     'Root' : 'D',
#     '3rd' : 'F#',
#     '5th' : 'A'
#     },
# ]
#
# root = chords[2].values()
# print(root)
#
# for key , value in chords[2].items():
#     print(f'{key} = {value} ')

#2

# chords2 = {
#     'Count': 3,
#     'Left': 9,
#     'All': 12,
#     'Keys' : [
#     {
#     'Root' : 'C',
#     '3rd' : 'E',
#     '5th' : 'G'
#     },
#
#     {
#     'Root' : 'G',
#     '3rd' : 'B',
#     '5th' : 'D'
#     },
#
#     {
#     'Root' : 'D',
#     '3rd' : 'F#',
#     '5th' : 'A'
#     },
#     ]
# }
#
# Keys_dict = chords2['Keys']
#
# Key_of_C = Keys_dict[0]
# Key_of_D = Keys_dict[1]
#
#
# print('This is key of C Major')
# for key , value in Key_of_C.items():
#     print(f'{key} : {value}')
# print('')
#
# print('This is key of D Major')
# for key , value in Key_of_D.items():
#     print(f'{key} : {value}')
# print('')



#3




chords3 = {
    'Count':
        {
        'One': 1,
        'Two': 2,
        'Three': 3
        },
    'Left': 9,
    'All': 12,
    'Keys':
    [
    {
    'Root' : 'C',
    '3rd' : 'E',
    '5th' : 'G'
    },

    {
    'Root' : 'G',
    '3rd' : 'B',
    '5th' : 'D'
    },

    {
    'Root' : 'D',
    '3rd' : 'F#',
    '5th' : 'A'
    },
    ]
}


Counted_Dict = chords3['Count']
Biggest_Num = Counted_Dict['Three']
print(Biggest_Num)


Keys_Extracted = chords3['Keys']
key_G = Keys_Extracted[1]
fifth_G = key_G['5th']
print(fifth_G)