def absolute(number):
    list_of_absolute_number = []
    for absolute_number in number:
        float_number = float(absolute_number)
        list_of_absolute_number.append(abs(float_number))

    return list_of_absolute_number

some_numbers = input().split()
print(absolute(some_numbers))
