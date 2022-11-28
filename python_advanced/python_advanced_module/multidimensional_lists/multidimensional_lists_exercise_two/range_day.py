def moving(the_map, the_shooter, side, steps):

    move_to = ()

    if side == 'up':
        move_to = (the_shooter[0] - steps, the_shooter[1])

    elif side == 'down':
        move_to = (the_shooter[0] + steps, the_shooter[1])

    elif side == 'left':
        move_to = (the_shooter[0], the_shooter[1] - steps)

    elif side == 'right':
        move_to = (the_shooter[0], the_shooter[1] + steps)


    if 0 <= move_to[0] < len(the_map) and 0 <= move_to[1] < len(the_map) and the_map[move_to[0]][move_to[1]] == '.':
        the_map[the_shooter[0]][the_shooter[1]] = '.'
        the_map[move_to[0]][move_to[1]] = 'A'
    else:
        move_to = (the_shooter[0], the_shooter[1])


    return the_map, move_to

def shooting(the_shooter, the_map, count_target, side, killed):

    if side == 'down':
        for target in range(the_shooter[0] + 1, len(the_map)):
            if the_map[target][the_shooter[1]] == 'x':
                killed.append([target, the_shooter[1]])
                the_map[target][the_shooter[1]] = '.'
                count_target -= 1
                break

    elif side == 'up':
        for target in range(the_shooter[0] - 1, -1, -1):
            if the_map[target][the_shooter[1]] == 'x':
                killed.append([target, the_shooter[1]])
                the_map[target][the_shooter[1]] = '.'
                count_target -= 1
                break

    elif side == 'left':
        for target in range(the_shooter[0] - 1, -1, -1):
            if the_map[the_shooter[0]][target] == 'x':
                killed.append([the_shooter[0], target])
                the_map[the_shooter[0]][target] = '.'
                count_target -= 1
                break

    elif side == 'right':
        for target in range(the_shooter[1] + 1, len(the_map)):
            if the_map[the_shooter[0]][target] == 'x':
                killed.append([the_shooter[0], target])
                the_map[the_shooter[0]][target] = '.'
                count_target -= 1
                break

    return matrix, count_target, killed

def shooter_position(place):
    targets = [target.count('x') for target in place if 'x' in target]

    for row in range(len(place)):
        for col in range(len(place)):
            if place[row][col] == "A":
                return (row, col), sum(targets)

SIZE = 5

matrix = [input().split() for _ in range(SIZE)]
count_commands = int(input())

shooter, all_target = shooter_position(matrix)
killed_target = []


while all_target > 0:


    command = input().split()

    if command[0] == 'move':
        matrix, shooter = moving(matrix, shooter, command[1], int(command[2]))


    elif command[0] == 'shoot':
        matrix, all_target, killed_target = shooting(shooter, matrix, all_target, command[1], killed_target)

    count_commands -= 1

    if count_commands == 0 and all_target > 0:
        break

if all_target == 0:
    print(f'Training completed! All {len(killed_target)} targets hit.')

else:
    print(f'Training not completed! {all_target} targets left.')

for kills in killed_target:
    print(kills)