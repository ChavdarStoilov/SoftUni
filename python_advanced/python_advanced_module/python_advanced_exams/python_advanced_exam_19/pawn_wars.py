def white_attack(player, checker, board, capture, marker):
    capture = capture

    for row, col in checker.values():
        attack_row, attack_col = player[0] + row, player[1] + col
        if 0 <= attack_col < 8 and 0 <= attack_row < 8:
            if board[attack_row][attack_col] == 'b':
                capture.append(marker[attack_row][attack_col])
                capture[0] = True
                break

    return capture

def black_attack(player, checker, board, capture, marker):
    capture = capture

    for row, col in checker.values():
        attack_row, attack_col = player[0] + row, player[1] + col
        if 0 <= attack_col < 8 and 0 <= attack_row < 8:
            if board[attack_row][attack_col] == 'w':
                capture.append(marker[attack_row][attack_col])
                capture[0] = True
                break

    return capture


def move_black_pawn(old_position, new_position, board):
    board[old_position[0]][old_position[1]] = '-'

    board[new_position[0]][new_position[1]] = 'b'

    return new_position, board


def move_white_pawn(old_position, new_position, board):
    board[old_position[0]][old_position[1]] = '-'

    board[new_position[0]][new_position[1]] = 'w'

    return new_position, board


def players(board):
    white = ()
    black = ()

    for row in range(8):
        for col in range(8):
            if board[row][col] == 'b':
                black = (row, col)
            elif board[row][col] == 'w':
                white = (row, col)

    return white, black


chessboard = [input().split() for _ in range(8)]
chessboard_markers = []

diagonal_move = {
    'down_left': (-1, -1),
    'down_right': (-1, 1),
    'up_left': (1, -1),
    'up_right': (1, 1)
}

for rows in range(8, 0, -1):
    row = []
    for col in range(97, 105):
        row.append(f'{chr(col)}{rows}')

    chessboard_markers.append(row)

white, black = players(chessboard)

white_capture = [False]
black_capture = [False]

while True:
    white_move_to = (white[0] + -1, white[1])
    black_move_to = (black[0] + 1, black[1])

    white_capture = white_attack(white, diagonal_move, chessboard, white_capture, chessboard_markers)

    if white_capture[0]:
        print(f'Game over! White win, capture on {white_capture[1]}.')
        break

    white, chessboard = move_white_pawn(white, white_move_to, chessboard)
    if white[0] == 0:
        print(f'Game over! White pawn is promoted to a queen at {chessboard_markers[white[0]][white[1]]}.')
        break

    black_capture = black_attack(black, diagonal_move, chessboard, black_capture, chessboard_markers)

    if black_capture[0]:
        print(f'Game over! Black win, capture on {black_capture[1]}.')
        break

    black, chessboard = move_black_pawn(black, black_move_to, chessboard)
    if black[0] == 7:
        print(f'Game over! Black pawn is promoted to a queen at {chessboard_markers[black[0]][black[1]]}.')
        break
