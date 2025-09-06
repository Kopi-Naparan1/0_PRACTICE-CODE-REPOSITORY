


def assignment8():
    class Shape():

        def area(self):
            pass

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            print(f"Area of the Circle: {3.14 * self.radius ** 2}")

    class Rectangle(Shape):
        def __init__(self,side1, side2):
            self.side1 = side1
            self.side2 = side2

        def area(self):
            print(f"Area of the Rectangle: {self.side1 * self.side2}")

    class Triangle(Shape):
        def __init__(self, base, height):
            self.base = base
            self.height = height

        def area(self):
            print(f"Area of the Triangle: {0.5 * self.base * self.height}")


    circle1 = Circle(10)
    rectangle1 = Rectangle(10,15)
    triangle1 = Triangle(10,12)



    shapes = [circle1, rectangle1, triangle1]

    for shape in shapes:
        shape.area()












def main():
    print("=" * 30)
    print('STARTING THE #7 Polymorphism')
    print("=" * 30)
    print('\n' * 5)


    assignment8()



if __name__ == "__main__":
    main()