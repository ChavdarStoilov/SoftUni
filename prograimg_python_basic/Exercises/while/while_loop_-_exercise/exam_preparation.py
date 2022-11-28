count_of_negative_grades = int(input())

count_grades = 0
poor_grades = 0
sum_grades = 0
last_exercise = ""
has_failed = True

while count_of_negative_grades > poor_grades:
    name_of_exercise = str(input())

    if name_of_exercise == "Enough":
        has_failed = False
        break


    grades = int(input())
    if grades <= 4:
        poor_grades += 1

    count_grades += 1
    sum_grades += grades
    last_exercise = name_of_exercise

if has_failed:
    print(f"You need a break, {poor_grades} poor grades.")
else:
    avg = sum_grades / count_grades
    print(f"Average score: {avg:.2f} \n"
          f"Number of problems: {count_grades} \n"
          f"Last problem: {last_exercise}")