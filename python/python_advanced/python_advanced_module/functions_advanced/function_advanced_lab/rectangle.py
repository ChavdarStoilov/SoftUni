def rectangle(*args):

    def area(num_one, num_two):
        return num_one * num_two

    def perimeter(num_one, num_two):
        return num_one * 2 + num_two * 2


    num_one, num_two = args

    if isinstance(num_one, int) and isinstance(num_two, int):

        return f'Rectangle area: {area(num_one, num_two)}\nRectangle perimeter: {perimeter(num_one, num_two)}'

    return "Enter valid values!"

# print(rectangle(2, 10))
print(rectangle('2', 10))