some_numbers = input().split(", ")

max_number = 10
max_numbers_list = []

while len(some_numbers) != 0:
    for number in some_numbers:
        if int(number) <= max_number:
            max_numbers_list.append(int(number))

    for number_for_del in max_numbers_list:
        num_str = str(number_for_del)
        some_numbers.remove(num_str)

    print(f"Group of {max_number}'s: {max_numbers_list}")
    max_numbers_list.clear()
    max_number += 10