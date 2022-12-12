number_of_lines = int(input())

list_of_numbers = []
filtered_numbers = []

for lines in range(number_of_lines):
    some_number = int(input())
    list_of_numbers.append(some_number)

command = str(input())
if command == "even":
    for number in list_of_numbers:
        if number % 2 == 0:
            filtered_numbers.append(number)
elif command == "odd":
    for number in list_of_numbers:
        if number % 2 != 0:
            filtered_numbers.append(number)
elif command == "negative":
    for number in list_of_numbers:
        if number < 0:
            filtered_numbers.append(number)
elif command == "positive":
    for number in list_of_numbers:
        if number >= 0:
            filtered_numbers.append(number)


print(filtered_numbers)