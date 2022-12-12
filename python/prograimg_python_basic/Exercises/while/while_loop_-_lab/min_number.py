import sys

first_input = input()

num = sys.maxsize

while first_input != "Stop":
    number = int(first_input)

    if num > number:
        num = number

    first_input = input()

print(num)