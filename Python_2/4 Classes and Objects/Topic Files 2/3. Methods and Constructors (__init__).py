

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hi my name is {self.name}. I am {self.age} years old.')


person_1 = Person("Kopi", 19)
person_1.greet()




