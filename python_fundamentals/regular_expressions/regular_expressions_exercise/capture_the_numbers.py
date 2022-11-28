import re

number = []

def find_only_numbers(text):

    pattern = r"(?P<test>\d+)"

    finder = re.finditer(pattern, text)

    for num in finder:
        number.append(num.group())



some_text = input()

while True:

    if some_text == "":
        break

    find_only_numbers(some_text)
    some_text = input()

print(" ".join(number))