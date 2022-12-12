from collections import deque
count_of_students = int(input())

student_records = {}

for _ in range(count_of_students):

    name, grade = input().split()

    if name not in student_records.keys():
        student_records[name] = []

    student_records[name].append(float(grade))


for names, grades in student_records.items():
    the_grades = ' '.join([f'{x:.2f}' for x in grades])
    avg = sum(grades) / len(grades)

    print(f'{names} -> {the_grades} (avg: {avg:.2f})')