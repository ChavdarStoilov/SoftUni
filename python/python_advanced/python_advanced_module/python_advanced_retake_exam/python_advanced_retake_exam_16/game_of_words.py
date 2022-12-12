def player_position(board):

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 'P':
                return row, col


def move_to(row, col, string, board):

    if board[row][col].isalnum():
        string += board[row][col]
        board[row][col] = 'P'

    return string, row, col, board


some_string = str(input())
SIZE = int(input())

board = [[x for x in input()] for _ in range(SIZE)]

player_row, player_col = player_position(board)


moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

count_moves = int(input())

for _ in range(count_moves):

    move = str(input())

    new_row, new_col = moves[move][0] + player_row, moves[move][1] + player_col

    if 0 > new_row or new_row >= SIZE or 0 > new_col or new_col >= SIZE:
        some_string = some_string[:-1]
    else:
        board[player_row][player_col] = '-'
        some_string, player_row, player_col, board = move_to(new_row, new_col, some_string, board)

print(some_string)
for matrix in board:
    print(f'{"".join(matrix)}')