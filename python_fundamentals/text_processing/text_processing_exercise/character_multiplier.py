first_string, second_string = input().split()

total_sum = 0

if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total_sum += int(ord(second_string[index])) * int(ord(first_string[index]))
    for char in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[char])

elif len(second_string) > len(first_string):
    for index in range(len(first_string)):
        total_sum += int(ord(second_string[index])) * int(ord(first_string[index]))
    for char in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[char])
else:
    for index in range(len(second_string)):
        total_sum += int(ord(second_string[index])) * int(ord(first_string[index]))


print(total_sum)