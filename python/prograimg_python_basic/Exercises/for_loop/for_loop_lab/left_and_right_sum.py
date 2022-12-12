number = int(input())

sum_number1 = 0
sum_number2 = 0

for numbers in range(2 * number):
    number1 = int(input())
    if numbers < number:
        sum_number1 += number1
    else:
        sum_number2 += number1

if sum_number1 == sum_number2:
    print(f"Yes, sum = {sum_number1}")
else:
    diff = abs(sum_number1 - sum_number2)
    print(f"No, diff = {diff}")