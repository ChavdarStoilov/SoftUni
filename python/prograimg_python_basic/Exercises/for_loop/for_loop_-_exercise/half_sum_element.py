count_of_numbers = int(input())

sum = 0
max_number = 0

for number in range(count_of_numbers):
    numbers = int(input())
    if max_number < numbers:
        max_number = numbers
    sum += numbers

if max_number == abs(sum - max_number):
    print("Yes")
    print(f"Sum = {max_number}")


else:

    left = abs((sum - max_number) - max_number)
    print("No")
    print(f"Diff = {left}")
