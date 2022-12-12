import re

def number_matching(text):

    pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

    groups = re.finditer(pattern, text)

    numbers = []

    for number in groups:
        numbers.append(number.group())


    return " ".join(numbers)


some_text = input()
print(number_matching(some_text))