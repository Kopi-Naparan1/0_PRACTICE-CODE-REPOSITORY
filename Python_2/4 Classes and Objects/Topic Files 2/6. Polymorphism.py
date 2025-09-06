import math
from abc import abstractmethod


# region Duck Typing/Informal Polymorphism

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#     def name(self):
#         return 'Circle'
#
#
# class Rectangle:
#     def __init__(self, side_1, side_2):
#         self.side_1 = side_1
#         self.side_2 = side_2
#
#     def area(self):
#         return self.side_1 * self.side_2
#
#
#     def name(self):
#         return 'Rectangle'
#
#
# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return 0.5 * self.base * self.height
#
#     def name(self):
#         return "Triangle"
#
#
# def print_area(shape):
#     print(f"Area of {shape.name()}: {shape.area()}")
#
# print_area(Circle(10))
# print_area(Rectangle(10, 5))
# print_area(Triangle(10,7))
#
# # endregion


# region Inheritance-Based Polymorphism (Formal)

class Shape:

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def name(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def name(self):
        return 'Circle'


class Rectangle(Shape):
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def area(self):
        return self.side_1 * self.side_2


    def name(self):
        return 'Rectangle'


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def name(self):
        return "Triangle"


shapes = [Circle(10), Rectangle(10,5), Triangle(20,5)]
for shape in shapes:
    print(f"Area of {shape.name()}: {shape.area().__round__(2)}")


# endregion


