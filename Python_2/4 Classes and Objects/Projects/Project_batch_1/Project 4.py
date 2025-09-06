from abc import ABC, abstractmethod
from math import pi
# Assignment
# #""" 4. Shape Calculator (OOP Geometry App)
# 	• 🧠 Concepts: Inheritance, method overriding, polymorphism
# 	• 📄 Features: Create shapes: Circle, Rectangle, Triangle, etc.
# 	• 👥 Use: Abstract base class (Shape), overridden area() and name()
# class Shape: # abstract base class
# class Circle(Shape): # area method overridden
# """


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def shape_name(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        result = self.radius * pi ** 2
        return result

    def shape_name(self):
        return 'Circle'


class Square(Shape):
    def __init__(self, sides):
        self.sides = sides

    def calculate_area(self):
        result = self.sides ** 2
        return result

    def shape_name(self):
        return 'Square'


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        result = (self.base * self.height) / 2
        return result

    def shape_name(self):
        return 'Triangle'


class Rectangle(Shape):
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def calculate_area(self):
        result = self.side_1 * self.side_2
        return result

    def shape_name(self):
        return 'Rectangle'


shapes = [Circle(10), Square(10), Triangle(10,7), Rectangle(8,6)]

for shape in shapes:
    print(f'{shape.shape_name()}: {shape.calculate_area().__round__(2)}')



