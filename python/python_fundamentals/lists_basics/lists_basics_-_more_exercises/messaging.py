some_number_code = input().split()
some_string_code = input()


list_of_string = []
message = ""
sum_number = 0

for string in some_string_code:
    list_of_string.append(string)

for number in some_number_code:
    for sum in number:
        sum_number += int(sum)

    if sum_number > len(list_of_string):
        new_index = sum_number -len(list_of_string)
        message += list_of_string[new_index]
        list_of_string.pop(new_index)
        sum_number = 0

    else:
        message += list_of_string[sum_number]
        list_of_string.pop(sum_number)
        sum_number = 0

print(message)