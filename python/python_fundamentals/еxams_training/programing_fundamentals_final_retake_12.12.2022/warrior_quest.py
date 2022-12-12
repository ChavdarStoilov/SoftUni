def upper_func(some_string):
    return some_string.upper()


def lower_func(some_string):
    return some_string.lower()


def dispel(some_string, idx, letter):

    some_string = list(some_string)

    some_string[idx] = letter

    return "".join(some_string)


def change(some_string, sub_one, sub_two):

    some_string = some_string.replace(sub_one, sub_two)

    return some_string


def remove(some_string, sub):

    some_string = some_string.replace(sub, "")

    return some_string



deciphered = input()

while True:

    command = input().split()

    if " ".join(command[:2]) == 'For Azeroth':
        break

    if command[0] == 'GladiatorStance':
        deciphered = upper_func(deciphered)
        print(deciphered)
    elif command[0] == 'DefensiveStance':
        deciphered = lower_func(deciphered)
        print(deciphered)

    elif command[0] == 'Dispel':
        idx = int(command[1])
        letter = command[2]

        if 0 <= idx < len(deciphered):
            deciphered = dispel(deciphered, idx, letter)
            print('Success!')
        else:
            print('Dispel too weak.')


    elif " ".join(command[:2]) == 'Target Change':

        if command[2] in deciphered:
            deciphered = change(deciphered, command[2], command[3])

        print(deciphered)


    elif " ".join(command[:2]) == 'Target Remove':

        if command[2] in deciphered:
            deciphered = remove(deciphered, command[2])
            print(deciphered)

    else:
        print('Command doesn\'t exist!')
