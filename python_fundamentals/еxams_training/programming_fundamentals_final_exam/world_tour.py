some_string = input()

command = input()
while command != "Travel":
    tour = command.split(":")

    if tour[0] == "Add Stop" and 0 <= int(tour[1]) < len(some_string):
        some_string = some_string[:int(tour[1])] + tour[2] + some_string[int(tour[1]):]
    elif tour[0] == "Remove Stop" and 0 <= int(tour[1]) < len(some_string) and 0 <= int(tour[2]) < len(some_string):
        some_string = some_string[:int(tour[1])] + some_string[int(tour[2]) + 1::]
    elif tour[0] == "Switch":
        some_string = some_string.replace(tour[1], tour[2])

    print(some_string)


    command = input()

print(f"Ready for world tour! Planned stops: {some_string}")