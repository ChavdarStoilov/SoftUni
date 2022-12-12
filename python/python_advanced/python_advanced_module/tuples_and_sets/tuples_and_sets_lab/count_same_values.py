some_values = input().split()

not_duplicate = []

for number in some_values:
    if number not in not_duplicate:
        not_duplicate.append(number)

for counter in not_duplicate:
    float_number = float(counter)

    print(f'{float_number:.1f} - {some_values.count(counter)} times')