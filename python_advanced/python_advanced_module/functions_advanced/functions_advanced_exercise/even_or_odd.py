def even_odd(*args):

    result = []

    if args[-1] == 'even':
        for number in args[:-1]:
            if number % 2 == 0:
                result.append(number)
    elif args[-1] == 'odd':
        for number in args[:-1]:
            if number % 2 != 0:
                result.append(number)

    return result

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))