# def sum_numbers(first_number, second_number):
#     result = first_number + second_number
#
#     print(subtract(result, third_number))
#
# def subtract(result, third_number):
#     return result - third_number
#
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
#
# sum_numbers(first_number, second_number)



def sum_numbers(the_first_number, the_second_number):
    return the_first_number + the_second_number


def subtract(sum, the_third_number):
    return sum - the_third_number


def add_and_subtract(first, second, third):
    the_result_of_first_and_second = sum_numbers(first, second)
    result = subtract(the_result_of_first_and_second, third)

    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
