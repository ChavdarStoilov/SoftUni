number = int(input())

count_of_combination = 0

for first_number in range(0, number + 1):
    for second_number in range(0, number + 1):
        for third_number in range(0, number + 1):
            if first_number + second_number + third_number == number:
                count_of_combination += 1


print(count_of_combination)

