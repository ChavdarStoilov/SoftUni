def even_odd_filter(**kwargs):
    sorted_info = sorted(kwargs.items(), key = lambda x: (x[0], len(x[1])))

    result = {}

    for key, value in sorted_info:

        if key == 'odd':
            result[key] = [x for x in value if x % 2 != 0]
        elif key == 'even':
            result[key] = [x for x in value if x % 2 == 0]

    return result

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
