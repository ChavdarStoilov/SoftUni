number_of_char = int(input())

sum_of_char = 0

while number_of_char != 0:
    char = str(input())
    sum_of_char += ord(char)
    number_of_char -= 1

print(f"The sum equals: {sum_of_char}")