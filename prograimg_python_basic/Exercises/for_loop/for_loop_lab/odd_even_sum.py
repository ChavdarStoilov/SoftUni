count_of_numbers = int(input())

numbers1 = 0
numbers2 = 0

for position in range(count_of_numbers):
    numbers = int(input())
    if position % 2 == 0:
        numbers2 += numbers
    else:
        numbers1 += numbers


if numbers1 == numbers2:
    print("Yes")
    print(f"Sum = {numbers1}")
else:
    left = abs(numbers1 - numbers2)
    print("No")
    print(f"Diff = {left}")