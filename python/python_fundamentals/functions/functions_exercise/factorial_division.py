def factorial_division(first_number, second_number):
    result = 1

    for number in range(first_number, second_number, -1):
        result *= number

    return f"{result:.2f}"


some_number_one = int(input())
some_number_two = int(input())

print(factorial_division(some_number_one, some_number_two))