first_number = int(input())
second_number = int(input())


for number in range(first_number, second_number +1):
    number_to_string = str(number)
    even = 0
    odd = 0
    for index, digit in enumerate(number_to_string):
        if index % 2 == 0:
            odd += int(digit)

        else:
            even += int(digit)

    if even == odd:
        print(number, end=" ")
