import sys

count_numbers = int(input())

min_num = sys.maxsize
max_num = - sys. maxsize

for numbers in range(count_numbers):
    number = int(input())
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number


print("Max number:", max_num)
print("Min number:", min_num)
