number_of_students = int(input())

academy = {}

for _ in range(number_of_students):
    name_of_student = input()
    grades = float(input())


    if name_of_student not in academy:
        academy[name_of_student] = []
    academy[name_of_student].append(grades)


academy_end = {name: sum(the_grades) / len(the_grades) for name, the_grades in academy.items() if sum(the_grades) / len(the_grades) >= 4.50}

#
for name, the_grades in academy_end.items():
    print(f"{name} -> {the_grades:.2f}")