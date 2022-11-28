first_num_of_char = int(input())
second_num_of_char = int(input())

for chars in range(first_num_of_char, second_num_of_char +1):
    print(chr(chars), end= " ")