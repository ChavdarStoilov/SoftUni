some_numbers = list(map(int, input().split(", ")))

get_indexes = [idx for idx in range(len(some_numbers)) if some_numbers[idx] % 2 == 0]
print(get_indexes)

