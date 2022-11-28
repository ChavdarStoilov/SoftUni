def rover_position(size, mars):

    for row in range(size):
        for col in range(size):
            if mars[row][col] == 'E':
                return row, col

SIZE = 6


mars = [input().split() for _ in range(SIZE)]

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

rover_row, rover_col = rover_position(SIZE, mars)

commands = input().split(', ')

deposits = {
    'Water': 0,
    'Metal': 0,
    'Concrete': 0
}

while True:

    if len(commands) == 0:
        break

    move = commands.pop(0)
    rover_row, rover_col = moves[move][0] + rover_row, moves[move][1] + rover_col

    if rover_row < 0:
        rover_row = SIZE - 1

    elif rover_row == SIZE:
        rover_row = 0

    elif rover_col < 0:
        rover_col = SIZE - 1

    elif rover_col == SIZE:
        rover_col = 0

    if mars[rover_row][rover_col] == 'W':
        deposits['Water'] += 1
        print(f'Water deposit found at ({rover_row}, {rover_col})')

    elif mars[rover_row][rover_col] == 'M':
        deposits['Metal'] += 1
        print(f'Metal deposit found at ({rover_row}, {rover_col})')

    elif mars[rover_row][rover_col] == 'C':
        deposits['Concrete'] += 1
        print(f'Concrete deposit found at ({rover_row}, {rover_col})')

    elif mars[rover_row][rover_col] == 'R':
        print(f'Rover got broken at ({rover_row}, {rover_col})')
        break


if deposits['Water'] >= 1 and deposits['Metal'] >= 1 and deposits['Concrete'] >= 1:
    print('Area suitable to start the colony.')

else:
    print('Area not suitable to start the colony.')