courses = {}
course = ""
while True:
    students = input()
    if ":" not in students:
        course = students
        break

    student = students.split(":")
    if student[2] not in courses:
        courses[student[2]] = []
        courses[student[2]].append(f"{student[0]}:{student[1]}")
    else:
        courses[student[2]].append(f"{student[0]}:{student[1]}")


test_two = course.replace("_", " ")

test = courses.get(test_two)

for i in test:
    print(str(i).replace(":", " - "))
