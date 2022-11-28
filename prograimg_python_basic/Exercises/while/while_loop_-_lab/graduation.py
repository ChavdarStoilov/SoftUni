import sys

name_of_student = input()

clas = 1
sum_of_rating = 0
failed = 0

while clas <= 12:
    rat = float(input())
    if rat >= 4:
        sum_of_rating += rat
        clas += 1
        continue
    else:
        failed += 1
        if failed>= 2:
            break



if clas >= 12:
    avr = sum_of_rating / 12
    print(f"{name_of_student} graduated. Average grade: {avr:.2f}")

else:
    print(f"{name_of_student} has been excluded at {clas} grade")