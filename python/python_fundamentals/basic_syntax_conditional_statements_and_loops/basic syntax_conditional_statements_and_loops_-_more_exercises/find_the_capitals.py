some_string = str(input())

list_of_capital_letters_indices = []

for index, char in enumerate(some_string):
    if 65 <= ord(char) <= 90:
        list_of_capital_letters_indices.append(index)

print(list_of_capital_letters_indices)