number_n = int(input())
previous_sum = int(input()) + int(input())
max_difference = 0

for i in range(number_n - 1):
    current_sum = int(input()) + int(input())

    if abs(previous_sum - current_sum) > max_difference:
        max_difference = abs(previous_sum - current_sum)

    previous_sum = current_sum

if max_difference == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_difference}")