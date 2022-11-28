number_of_lines = int(input())

list_for_positive_numbers = []
list_for_negative_numbers = []

count_positives = 0
sum_of_negative_numbers = 0

for lines in range(number_of_lines):
    some_number = int(input())

    if some_number >= 0:
        list_for_positive_numbers.append(some_number)
        count_positives += 1
    else:
        sum_of_negative_numbers += some_number
        list_for_negative_numbers.append(some_number)


print(f"{list_for_positive_numbers}\n"
      f"{list_for_negative_numbers}")


print(f"Count of positives: {count_positives}\n"
      f"Sum of negatives: {sum_of_negative_numbers}")