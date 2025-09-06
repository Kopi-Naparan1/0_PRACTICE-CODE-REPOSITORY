letter_int = {'Bb' : 'Gm', 'Eb' : 'Cm', 'Ab' : 'Fm', 'Db' : 'Bbm' }



print(letter_int.get('Bb'))



for key , value in letter_int.items():
    print(f'This is the key of: {key} and its relative minor key: {value}')


print(letter_int)