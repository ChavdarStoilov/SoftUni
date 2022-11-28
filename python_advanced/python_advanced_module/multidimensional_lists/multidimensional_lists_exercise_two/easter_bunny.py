size_matrix = int(input())

matrix = [input().split() for _ in range(size_matrix)]

bunny_pos = ()

for row in range(size_matrix):
    for col in range(size_matrix):
        if matrix[row][col] == 'B':
            bunny_pos = (row, col)

up_max = [0, 'up', []]
down_max = [0, 'down', []]
left_max = [0, 'left', []]
right_max = [0, 'right', []]

while True:


    for up in range(bunny_pos[0] -1, -1, -1):
        if matrix[up][bunny_pos[1]] == 'X':
            break
        else:
            up_max[0] += int(matrix[up][bunny_pos[1]])
            up_max[2].append([up, bunny_pos[1]])

    for down in range(bunny_pos[0] + 1, len(matrix)):
        if matrix[down][bunny_pos[1]] == 'X':
            break
        else:
            down_max[0] += int(matrix[down][bunny_pos[1]])
            down_max[2].append([down, bunny_pos[1]])


    for left in range(bunny_pos[1] -1, -1, -1):
        if matrix[bunny_pos[0]][left] == 'X':
            break
        else:
            left_max[0] += int(matrix[bunny_pos[0]][left])
            left_max[2].append([bunny_pos[0], left])


    for right in range(bunny_pos[1] + 1, len(matrix)):
        if matrix[bunny_pos[0]][right] == 'X':
            break
        else:
            right_max[0] += int(matrix[bunny_pos[0]][right])
            right_max[2].append([bunny_pos[0], right])

    break


if up_max[0] > down_max[0] and up_max[0] > right_max[0] and up_max[0] > left_max[0]:
    print(f'{up_max[1]}')
    for pos in up_max[2]:
        print(pos)
    print(up_max[0])


elif down_max[0] > up_max[0] and down_max[0] > right_max[0] and down_max[0] > left_max[0]:
    print(f'{down_max[1]}')
    for pos in down_max[2]:
        print(pos)
    print(down_max[0])


elif right_max[0] > up_max[0] and right_max[0] > down_max[0] and right_max[0] > left_max[0]:
    print(f'{right_max[1]}')
    for pos in right_max[2]:
        print(pos)
    print(right_max[0])


elif left_max[0] > up_max[0] and left_max[0] > right_max[0] and left_max[0] > down_max[0]:
    print(f'{left_max[1]}')
    for pos in left_max[2]:
        print(pos)

    print(left_max[0])


