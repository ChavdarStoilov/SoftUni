from collections import deque
from itertools import count

from regex import R

def check_for_winner(board, row, col, disk):
    winner = False
    row = row - 1
    col = 0

    for _ in range(3):
        if board[row][col] != disk:
            break

        row -= 1
        col += 1
 
    else:
        winner = True
        return winner        


def put_disk(board, col, row, disk):

    try:
        for rows in range(row - 1, -1, -1):
            the_col = board[rows]
            if the_col[col - 1] == '_':
                the_col[col - 1] = disk
                return board
    except TypeError:
        return 'Cannot put out of board'

def result(board, col):
    
    print()
    for cols in board:
        print(f'|  {"  |  ".join("".join(cols))}  |')

    print(f'   {"     ".join([str(x) for x in range(1, col + 1)])}\n')
        

def inputs():
    finish_inputs = False

    while not finish_inputs:
        try:
            ROWS = int(input('Enter number of rows: '))
            COLS = int(input('Enter number of cols: '))
            number_of_player = int(input('Please give number of players: '))
            break
        except ValueError:
            print('Please enter valid number')
            continue

    
    return ROWS, COLS, number_of_player


board_row, board_col, players = inputs()
board = [["_"] * board_col for _ in range(board_row)]
players = deque([f'Player {str(num)}' for num in range(1, players + 1)])
type_disks = ['X', 'Q', 'V', 'S', 'O']

disks = {f'{x}': type_disks.pop() for x in players}

while True:
    player = players[0]
    disk = disks[player]


    try:
        result(board, board_col)
        number = int(input(f'\n{player} Please choose number: '))
        
    except ValueError:
        print('Please enter valid number')
        continue
    
    
    board = put_disk(board, number, board_row, disk)

    if check_for_winner(board, board_row, board_col, disk):
        print(f'The Winner is {player}')
        break
    
   

    # result(board, board_col)

    players.rotate(-1)

