import re

count_of_string = int(input())

for _ in range(count_of_string):
    string = input()

    if "Ivan is Here" in string:
        print("Ivan is Here")
        continue

    pattern = r"((?<=!)[A-Z][a-z]{1,})(\!\:)([\[])(\w{8,})[\]]"

    finder = re.findall(pattern, string)

    if len(finder) > 0:
        for text in finder:
            the_text = text[3]

            result = " ".join([str(ord(num)) for num in text[3]])

            print(f"{text[0]}: {result}")

    else:
        print("The message is invalid")
