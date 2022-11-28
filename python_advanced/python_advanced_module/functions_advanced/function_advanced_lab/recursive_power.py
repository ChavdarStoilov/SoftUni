def recursive_power(num_one, num_two):
    result = 1

    if num_two == 0:
        return result

    result = num_one * recursive_power(num_one, num_two - 1)

    return result

print(recursive_power(2, 10))