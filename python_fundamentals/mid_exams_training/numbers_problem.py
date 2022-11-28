def top_five_numbers(numbers):
    average = sum(numbers) / len(numbers)
    top = []
    for greater in numbers:
        if greater > average:
            top.append(greater)

    while len(top) > 5:
        min_number = min(top)
        top.remove(min_number)

    top.sort()
    string_num = [str(num_str) for num_str in top]

    if len(top) < 1:
        return "No"
    else:
        return " ".join(string_num[::-1])

some_numbers = input().split()
integers_number = list(map(int, some_numbers))

print(top_five_numbers(integers_number))
