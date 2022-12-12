numbers_dictionary = {}

while True:
    line = input()

    if line == 'Search':
        break

    number_as_string = line

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')
        continue



while True:
    line = input()

    if line == "Remove":
        break

    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print('Number does not exist in dictionary')
        continue

while True:
    line = input()

    if line == 'End':
        break

    searched = line

    try:
        del numbers_dictionary[searched]
    except KeyError:
        print('Number does not exist in dictionary')
        continue

print(numbers_dictionary)
