count_of_students = int(input())

sum_of_assessments = 0
failed = 0
between_three = 0
between_four = 0
top_students = 0

for assessments in range(0, count_of_students):
    assessment = float(input())
    sum_of_assessments += assessment

    if 2.00 <= assessment <= 2.99:
        failed += 1
    elif 3.00 <= assessment <= 3.99:
        between_three += 1
    elif 4.00 <= assessment <= 4.99:
        between_four += 1
    else:
        top_students += 1


percentage_top = (top_students / count_of_students) * 100
percentage_between_three = (between_three / count_of_students) * 100
percentage_between_four = (between_four / count_of_students) * 100
percentage_fail = (failed / count_of_students) * 100
avg = sum_of_assessments / count_of_students

print(f"Top students: {percentage_top:.2f}%\n"
      f"Between 4.00 and 4.99: {percentage_between_four:.2f}%\n"
      f"Between 3.00 and 3.99: {percentage_between_three:.2f}%\n"
      f"Fail: {percentage_fail:.2f}%\n"
      f"Average: {avg:.2f}")



