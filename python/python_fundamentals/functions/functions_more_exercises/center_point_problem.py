import math
def center_func(x_one, y_one, x_two, y_two):

    first_coordinate = math.floor(float(x_one)), math.floor(float(y_one))
    second_coordinate = math.floor(float(x_two)), math.floor(float(y_two))

    first_result = abs(float(x_one)) + abs(float(y_one))
    second_result = abs(float(x_two)) + abs(float(y_two))


    if first_result <= second_result:
        return first_coordinate
    elif first_result > second_result:
        return second_coordinate




coordinate_x_one = input()
coordinate_y_one = input()
coordinate_x_second = input()
coordinate_y_second = input()

print(center_func(coordinate_x_one, coordinate_y_one, coordinate_x_second, coordinate_y_second))