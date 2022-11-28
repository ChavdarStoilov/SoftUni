some_number = str(input())

numbers = []
max_number = []

for number in some_number:
    numbers.append(number)

for index in range(len(numbers)):
    max_number.append((max(numbers)))
    numbers.remove(max(numbers))

print("".join(max_number))