import math

def center_func(line_one_x_one, line_one_y_one, line_one_x_two, line_one_y_two,
                line_two_x_one, line_two_y_one, line_two_x_two, line_two_y_two):

    first_line = math.floor(line_one_x_one), math.floor(line_one_y_one)
    second_line = math.floor(line_one_x_two), math.floor(line_one_y_two)
    third_line = math.floor(line_two_x_one), math.floor(line_two_y_one)
    fourth_line = math.floor(line_two_x_two), math.floor(line_two_y_two)

    first_result = abs(line_one_x_one + line_one_y_one + line_one_x_two + line_one_y_two)
    second_result = abs(line_two_x_one + line_two_y_one + line_two_x_two + line_two_y_two)

    if first_result >= second_result:
        if abs(line_one_x_one + line_one_y_one) <= abs(line_one_x_two + line_one_y_two):
            return f"{first_line}{second_line}"
        return f"{second_line}{first_line}"

    if first_result < second_result:
        if abs(line_two_x_one + line_two_y_one) <= abs(line_two_x_two + line_two_y_two):
            return f"{third_line}{fourth_line}"
        return f"{fourth_line}{third_line}"


first_line_first_x = float(input())
first_line_first_y = float(input())
first_line_second_x = float(input())
first_line_second_y = float(input())
second_line_first_x = float(input())
second_line_first_y = float(input())
second_line_second_x = float(input())
second_line_second_y = float(input())

print(center_func(first_line_first_x, first_line_first_y, first_line_second_x, first_line_second_y,
                  second_line_first_x, second_line_first_y, second_line_second_x, second_line_second_y))
