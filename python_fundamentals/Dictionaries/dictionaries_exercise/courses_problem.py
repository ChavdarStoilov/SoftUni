command = input()

courses = {}

while command != "end":
    course, student = command.split(" : ")

    if course not in courses:
        courses[course] = []
    courses[course].append(student)

    command = input()


for the_course, names in courses.items():
    print(f"{the_course}: {len(names)}")
    for name in names:
        print(f"-- {name}")
