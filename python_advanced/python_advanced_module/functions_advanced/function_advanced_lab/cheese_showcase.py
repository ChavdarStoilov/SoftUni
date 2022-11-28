def sorting_cheeses(**kwargs):
    sorted_cheese = sorted(kwargs.items(), key = lambda x: (-len(x[1]), x[0]))

    result = []

    for name, quan in sorted_cheese:
        result.append(name)
        quanty_list = sorted(quan, reverse = True)
        result += quanty_list

    return '\n'.join([str(x) for x in result])

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
