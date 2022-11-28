command = input()

judge = {}
courses = {}

while command != "exam finished":

    exam = command.split("-")

    if exam[1] == "banned":
        judge.pop(exam[0])
        break

    if exam[1] not in courses and exam[1]:
        courses[exam[1]] = 0
    courses[exam[1]] += 1


    if exam[0] not in judge:
        judge[exam[0]] = int(exam[2])
    else:
        the_point = int(judge[exam[0]])
        if the_point < int(exam[2]):
            judge[exam[0]] = int(exam[2])


    command = input()


print("Results:")
for name, point in judge.items():
    print(f"{name} | {point}")

print("Submissions:")
for course, count in courses.items():
    print(f"{course} - {count}")
