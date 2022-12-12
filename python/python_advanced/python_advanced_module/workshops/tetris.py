import time
import random
import os

clear = lambda: os.system('cls')


def display_board():
    for i in board:
        print(f'| {" ".join(i)} |')


def figure_one(board):
    for row in range(1, len(board)):

        if '#' in board[0]:
            break

        board[row - 1][0] = ' '
        board[row - 1][1] = ' '
        board[row - 1][2] = ' '
        board[row - 1][3] = ' '

        if board[row][0] == ' ' and board[row][1] == ' ' and board[row][2] == ' ' and board[row][3] == ' ':
            board[row][0] = '#'
            board[row][1] = '#'
            board[row][2] = '#'
            board[row][3] = '#'
        elif board[row][0] == "#" and board[row][1] == "#" and board[row][2] == "#" and board[row][3] == "#":
            board[row - 1][0] = '#'
            board[row - 1][1] = '#'
            board[row - 1][2] = '#'
            board[row - 1][3] = '#'
        display_board()
        clear()

    return board


def figure_two(board):
    for row in range(1, len(board)):
        if row + 3 < len(board):
            if '#' in board[0]:
                break

            board[row - 0][0] = ' '
            board[row - 1][0] = ' '
            board[row - 2][0] = ' '
            board[row - 3][0] = ' '

            if board[row][0] == ' ' and board[row][0] == ' ' and board[row][0] == ' ' and board[row][0] == ' ':
                board[row + -1][0] = '#'
                board[row + 0][0] = '#'
                board[row + 1][0] = '#'
                board[row + 2][0] = '#'

            elif board[row][0] == "#" and board[row][0] == "#" and board[row][0] == "#" and board[row][0] == "#":
                board[row - 0][0] = '#'
                board[row - 1][0] = '#'
                board[row - 2][0] = '#'
                board[row - 3][0] = '#'

            display_board()

            clear()

    return board


board = [[' '] * 12 for _ in range(10)]

figures = [
    '####',
    '#\n#\n#\n#',
]

while '#' not in board[0]:
    figure = random.choice(figures)

    if figure == '####':
        board = figure_one(board)

    # elif figure == '#\n#\n#\n#':
    #     board = figure_two(board)
    #
    #

    display_board()
