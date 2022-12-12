from math import pi

figure = str(input())

if figure == "square":
    square = float(input())
    size_square = square * square
    print("{:.3f}".format(size_square))
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    size_rectangle = a * b
    print("{:.3f}".format(size_rectangle))
elif figure == "circle":
    radius = float(input())
    size_circle = pi * (radius * radius)
    print("{:.3f}".format(size_circle))
elif figure == "triangle":
    a = float(input())
    b = float(input())
    size_triangle = a * b / 2
    print("{:.3f}".format(size_triangle))