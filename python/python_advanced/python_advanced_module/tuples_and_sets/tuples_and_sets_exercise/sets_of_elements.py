first_part, second_part = input().split()

range_of_numbers = int(first_part) + int(second_part)

first_set = set()
second_set = set()

for part in range(1, range_of_numbers + 1):

    number = int(input())

    if part <= int(first_part):
        first_set.add(number)
    else:
        second_set.add(number)


for num in first_set.intersection(second_set):

    print(num)