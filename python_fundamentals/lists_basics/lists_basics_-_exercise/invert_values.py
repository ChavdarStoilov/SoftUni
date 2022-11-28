some_numbers = input()

inverted_numbers = []
added_number_in_list = some_numbers.split(" ")


for number in added_number_in_list:
    invert = int(number) * -1
    inverted_numbers.append(invert)


print(inverted_numbers)