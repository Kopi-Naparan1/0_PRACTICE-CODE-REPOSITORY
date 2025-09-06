
try:
    with open('File.tx') as file1:
        print(file1.read())

except FileNotFoundError:
    print('File not found')




