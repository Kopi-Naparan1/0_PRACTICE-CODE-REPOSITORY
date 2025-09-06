
class Animal:
    def speak(self):
        print('The animal makes a sound')


class Cat(Animal):
    def speak(self) -> None:
        print('Meow')

#  1
animal_1 = Animal().speak()
cat_1 = Cat().speak()

#2
animal = Animal()
cat = Cat()

animal.speak()
cat.speak()

