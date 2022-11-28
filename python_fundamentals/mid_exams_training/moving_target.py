def move_target(target):
    command = input()

    while command != "End":
        shoot = command.split()
        if shoot[0] == "Shoot":
            if 0 <= int(shoot[1]) < len(target):
                target[int(shoot[1])] -= int(shoot[2])
                if target[int(shoot[1])] <= 0:
                    target.pop(int(shoot[1]))

        elif shoot[0] == "Add":
            if 0 <= int(shoot[1]) < len(target):
                target.insert(int(shoot[1]), int(shoot[2]))
            else:
                print("Invalid placement!")

        elif shoot[0] == "Strike":
            if int(shoot[1]) - int(shoot[2]) >= 0 and (int(shoot[1])) + int(shoot[2]) < len(target):
                end_radius = int(shoot[1]) + int(shoot[2])
                start_radius = int(shoot[1]) - int(shoot[2])
                for num in range(end_radius, start_radius - 1, -1):
                    target.pop(int(num))
            else:
                print("Strike missed!")

        command = input()

    end_result = list(map(str, target))
    return f"|".join(end_result)


sequence_of_targets = input().split()
integers_sequence_of_targets = list(map(int, sequence_of_targets))

print(move_target(integers_sequence_of_targets))
