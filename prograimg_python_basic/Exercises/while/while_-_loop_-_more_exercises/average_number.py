number_for_n = int(input())

sum_of_numbers = 0
count_of_numbers = 0

for numbers in range(number_for_n):
    number = int(input())
    sum_of_numbers += number
    count_of_numbers += 1

avg_numbers = sum_of_numbers / count_of_numbers
print(f"{avg_numbers:.2f}")
