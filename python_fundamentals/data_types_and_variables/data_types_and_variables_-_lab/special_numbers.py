some_num = int(input())

for special in range(1, some_num +1):
    sum_of_digits = 0
    digits = special
    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{special} -> True")
    else:
        print(f"{special} -> False")