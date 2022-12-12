def min_max_sum(numbers):
    integer_list = []

    for number in numbers:
        integer_list.append(int(number))

    return f"The minimum number is {min(integer_list)}\n"\
           f"The maximum number is {max(integer_list)}\n"\
           f"The sum number is: {sum(integer_list)}"

some_numbers = input().split()
print(min_max_sum(some_numbers))