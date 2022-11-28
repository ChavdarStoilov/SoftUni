some_number = int(input())

for first_num in range(some_number):
    for second_num in range(some_number):
        for third_num in range(some_number):
            print(f"{chr(97 + first_num)}{chr(97 + second_num)}{chr(97 + third_num)}")