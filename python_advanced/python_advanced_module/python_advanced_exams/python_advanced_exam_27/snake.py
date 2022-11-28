def snake_posi(size_territory):
    for row in range(size_territory):
        for col in range(size_territory):
            if territory[row][col] == 'S':
                return row, col


def burrows_posi(size_territory):
    burrow = []

    for row in range(size_territory):
        for col in range(size_territory):
            if territory[row][col] == 'B':
                burrow.append((row, col))
    return burrow

def out_of_territory(size_territory, row, col):

    if 0 > row or row >= size_territory:
        return True

    elif 0 > col or col >= size_territory:
        return True

def moving(territory, row, col, burrow, quantity):

    if territory[row][col] == '-':
        territory[row][col] = 'S'
    elif territory[row][col] == 'B':
        for rows, cols in burrow:
            territory[row][col] = '.'
            if row != rows and col != cols:
                row, col = rows, cols
                territory[row][col] = 'S'
    elif territory[row][col] == '*':
        quantity += 1
        territory[row][col] = 'S'

    return territory, row, col, quantity

size_territory = int(input())

territory = [[str(x) for x in input()] for _ in range(size_territory)]


snake_row, snake_col = snake_posi(size_territory)
burrows = burrows_posi(size_territory)

moves = {

    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

food_quantity = 0

while food_quantity != 10:

    move = input()

    move_to_row, move_to_col = moves[f'{move}'][0] + snake_row, moves[f'{move}'][1] + snake_col
    if out_of_territory(size_territory, move_to_row, move_to_col):
        territory[snake_row][snake_col] = '.'
        break
    else:
        territory[snake_row][snake_col] = '.'
        territory, snake_row, snake_col, food_quantity = moving(territory, move_to_row, move_to_col, burrows, food_quantity)


if food_quantity == 10:
    print('You won! You fed the snake.')
else:
    print('Game over!')

print(f'Food eaten: {food_quantity}')

for t in territory:
    print(f"{''.join(t)}")

