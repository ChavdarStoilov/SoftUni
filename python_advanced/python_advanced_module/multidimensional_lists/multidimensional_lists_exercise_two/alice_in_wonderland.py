size_wonderland = int(input())

wonderland = [input().split() for _ in range(size_wonderland)]
print(wonderland)
moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

needed_tea = 10
alice_pos = ()

for row in range(len(wonderland)):
    for col in range(len(wonderland)):
        if wonderland[row][col] == 'A':
            alice_pos = (row, col)


while needed_tea > 0:

    command = input()

    row, col = moves[command][0], moves[command][1]


    wonderland[alice_pos[0]][alice_pos[1]] = '*'
    alice_pos = (alice_pos[0] + row, alice_pos[1] + col)
    if 0 <= alice_pos[0] < size_wonderland and 0 <= alice_pos[1] < size_wonderland:
        if wonderland[alice_pos[0]][alice_pos[1]].isdigit():
            needed_tea -= int(wonderland[alice_pos[0]][alice_pos[1]])
        elif wonderland[alice_pos[0]][alice_pos[1]] == 'R':
            wonderland[alice_pos[0]][alice_pos[1]] = '*'
            break
        wonderland[alice_pos[0]][alice_pos[1]] = '*'
    else:
        break


if needed_tea <= 0:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")

for board in wonderland:
    print(' '.join(board))