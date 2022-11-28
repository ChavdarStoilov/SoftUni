from math import floor

def player_position(board):
    for rows in range(len(board)):
        for cols in range(len(board)):
            if board[rows][cols] == 'P':
                row, col = (rows, cols)
                return row, col


def moving(row, col, board, coins, already_get_coin):
    wall = False

    if board[row][col] == 'X':
        wall = True
        return board, row, col, coins, wall
    else:
        if [row, col] not in already_get_coin:
            if board[row][col].isdigit():
                coins += int(board[row][col])

    return board, row, col, coins, wall


size_of_board = int(input())

board = [input().split() for _ in range(size_of_board)]

coins = 0
already_get_coin = []

player_row, player_col = player_position(board)

already_get_coin.append([player_row, player_col])

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    if coins >= 100:
        break

    move = input()
    new_player_row = player_row + moves[move][0]
    new_player_col = player_col + moves[move][1]

    if 0 > new_player_row or new_player_row >= size_of_board:
        if size_of_board <= new_player_row:
            new_player_row = 0
        else:
            new_player_row = size_of_board - 1

    if 0 > new_player_col or new_player_col >= size_of_board:
        if size_of_board <= new_player_col:
            new_player_col = 0
        else:
            new_player_col = size_of_board - 1

    board, player_row, player_col, coins, wall = moving(new_player_row, new_player_col, board, coins, already_get_coin)
    already_get_coin.append([player_row, player_col])

    if wall:
        coins -= coins * 0.50
        break


if coins < 100:
    print(f'Game over! You\'ve collected {floor(coins)} coins.\nYour path:')
else:
    print(f'You won! You\'ve collected {coins} coins.\nYour path:')

for path in already_get_coin:
    print(path)