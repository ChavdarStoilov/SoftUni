import re

letters = input()

first_hidden = False
second_hidden = False
third_hidden = False
count_n = 0
count_c = 0
count_o = 0
count_hidden = 0

the_letter = ""
second_letter = ""

while letters != "End":
    letters = letters

    re.findall('[^A-Za-z0-9]', letters)


    if letters == "n":
        first_hidden = True
        count_n += 1
        if count_n > 1:
            count_n += 0
            the_letter += letters
        else:
            the_letter += ""
    elif letters == "o":
        second_hidden = True
        count_o += 1
        if count_o > 1:
            count_o += 0
            the_letter += letters
        else:
            the_letter += ""
    elif letters == "c":
        third_hidden = True
        count_c += 1
        if count_c > 1:
            count_c += 0
            the_letter += letters
        else:
            the_letter += ""
    elif re.findall('[^A-Za-z0-9]', letters):
        the_letter += ""
    elif count_hidden == 1:
        second_letter += letters
    elif count_hidden == 2:
        second_letter += ""
    else:
        the_letter += letters

    if first_hidden and second_hidden and third_hidden:
        count_hidden += 1
        first_hidden = False
        second_hidden = False
        third_hidden = False
        count_n = 0
        count_c = 0
        count_o = 0
    else:
        the_letter += ""

    letters = input()

if count_hidden >= 2:
    print(f"{the_letter} {second_letter}")
else:
    print(the_letter)