number_of_the_lines = int(input())

opened_bracket = 0
closed_bracket = 0
previous_bracket = ""

for lines in range(number_of_the_lines):
    some_string = str(input())

    if some_string == "(":
        opened_bracket += 1
        if some_string == previous_bracket:
            break
        previous_bracket = "("
    elif some_string == ")":
        closed_bracket += 1
        if some_string == previous_bracket:
            break
        previous_bracket = ")"


if opened_bracket == closed_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")

