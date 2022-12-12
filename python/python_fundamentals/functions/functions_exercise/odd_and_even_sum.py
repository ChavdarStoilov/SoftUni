def sum(the_number):
    result_of_odd = 0
    result_of_even = 0

    for number in the_number:
        integer_number = int(number)

        if integer_number % 2 == 0:
            result_of_even += integer_number
        elif integer_number % 2 != 0:
            result_of_odd += integer_number


    return f"Odd sum = {result_of_odd}, Even sum = {result_of_even}"

some_number = input()
print(sum(some_number))