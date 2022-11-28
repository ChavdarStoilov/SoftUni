start_number = int(input())
end_number = int(input())
magic_number = int(input())

count_combination = 0
number_found = False

for first_number in range(start_number, end_number + 1):
    for second_number in range(start_number, end_number + 1):
        count_combination += 1
        if first_number + second_number == magic_number:
            number_found = True
            break

    if number_found is True:
        break

if number_found is True:
    print(f"Combination N:{count_combination} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{count_combination} combinations - neither equals {magic_number}")