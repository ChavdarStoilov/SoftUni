number_wagons = int(input())
command = input().split()

wagons = [0 for wagon in range(number_wagons)]

while command[0] != "End":

    commands = command

    if commands[0] == "add":
        wagons[-1] += int(commands[1])

    elif commands[0] == "insert":
        wagons[int(commands[1])] += int(commands[2])

    elif commands[0] == "leave":
        wagons[int(commands[1])] -= int(commands[2])


    command = input().split()


print(wagons)