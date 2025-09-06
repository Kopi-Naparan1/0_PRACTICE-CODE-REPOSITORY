### 2D Areas

def area_rectangle(length, base):
    return length * base


def area_square(sides):
    return sides ** 2


def area_triangle(base, height):
    return 1 / 2 * base * height


def area_trapezoid(base1, base2, height):
    return 1 / 2 * (base1 * base2) * height


def area_circle(radius):
    pi = 3.141592653589793238462643
    return pi * radius ** 2


### 3D Volumes

def volume_cube(sides):
    return sides ** 3


def volume_cylinder(radius, height):
    pi = 3.141592653589793238462643
    return pi * radius ** 2 * height


def volume_cone(radius, height):
    pi = 3.141592653589793238462643
    return 1 / 3 * pi * radius ** 2 * height


def volume_sphere(radius):
    pi = 3.141592653589793238462643
    return 4 / 3 * pi * radius ** 3
