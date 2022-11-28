def rounding(numbers):
    list_of_rounding_number = []
    for round_number in numbers:
        list_of_rounding_number.append(round(float(round_number)))

    return list_of_rounding_number

some_number = input().split()
print(rounding(some_number))