def creating(board, row, col, value):

    if board[row][col] == '.':
        board[row][col] = value

    return board

def updating(board, row, col, value):

    if board[row][col].isdigit() or board[row][col].isalpha():
        if value == 'h' and board[row][col] == '12':
            board[row][col] = 'h'
        board[row][col] = value

    return board

def deleting(board, row, col):

    if board[row][col].isalpha() or board[row][col].isdigit():
        board[row][col] = '.'

    return board

def reading(board, row, col):

    if board[row][col].isdigit() or board[row][col].isalpha():
        print(board[row][col])


SIZE = 6

board = [input().split() for _ in range(SIZE)]

first_posi = input()
move_row, move_col = int(first_posi[1]), int(first_posi[4])

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:

    command = input().split(', ')
    action = command[0]

    if action == 'Stop':
        break

    move_row, move_col = moves[command[1]][0] + move_row, moves[command[1]][1] + move_col

    if action == 'Create':
        board = creating(board, move_row, move_col, str(command[2]))

    elif action == 'Update':
        board = updating(board, move_row, move_col, str(command[2]))

    elif action == 'Delete':
        board = deleting(board, move_row, move_col)

    elif action == 'Read':
        reading(board, move_row, move_col)


for matrix in board:
    print(' '.join(matrix))