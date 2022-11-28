from collections import deque


def checker(row, col, captured_list, captured):
    if captured:
        captured_list.append([row, col])

    return captured_list


def diagonally(row, col, board, captured_list):
    captured = False

    for left_down in range(len(board)):

        if 0 <= row + 1 < len(board) and 0 <= col - 1 < len(board):

            if board[row + 1][col - 1] == 'Q':
                break
            elif board[row + 1][col - 1] == 'K':
                captured = True
                captured_list = checker(row, col, captured_list, captured)
                break
        else:
            break

    for left_up in range(len(board)):

        if 0 <= row - 1 < len(board) and 0 <= col - 1 < len(board):

            if board[row - 1][col - 1] == 'Q':
                break
            elif board[row - 1][col - 1] == 'K':
                captured = True
                captured_list = checker(row, col, captured_list, captured)
                break
        else:
            break

    for right_up in range(len(board)):
        if 0 <= row - 1 < len(board) and 0 <= col + 1 < len(board):

            if board[row - 1][col + 1] == 'Q':
                break
            elif board[row - 1][col + 1] == 'K':
                captured = True
                captured_list = checker(row, col, captured_list, captured)
                break
        else:
            break

    for right_down in range(len(board)):

        if 0 <= row + 1 < len(board) and 0 <= col + 1 < len(board):

            if board[row + 1][col + 1] == 'Q':
                break
            elif board[row + 1][col + 1] == 'K':
                captured = True
                captured_list = checker(row, col, captured_list, captured)
                break
        else:
            break


    return captured_list


def horizontally(row, col, board, captured_list):
    captured = False

    for left in range(col - 1, -1, - 1):
        if board[row][left] == 'Q':
            break
        elif board[row][left] == 'K':
            captured = True
            captured_list = checker(row, col, captured_list, captured)
            break

    for right in range(col + 1, len(board)):
        if board[row][right] == 'Q':
            break
        elif board[row][right] == 'K':
            captured = True
            captured_list = checker(row, col, captured_list, captured)
            break

    return captured_list


def vertically(row, col, board, captured_list):
    captured = False

    for up in range(row - 1, -1, - 1):
        if board[up][col] == 'Q':
            break
        elif board[up][col] == 'K':
            captured = True
            captured_list = checker(row, col, captured_list, captured)
            break

    for down in range(row + 1, len(board)):
        if board[down][col] == 'Q':
            break
        elif board[down][col] == 'K':
            captured = True
            captured_list = checker(row, col, captured_list, captured)
            break

    return captured_list


def queens_position(board):
    queens = []

    for row_queen in range(len(board)):
        for col_queen in range(len(board)):
            if board[row_queen][col_queen] == 'Q':
                queens.append((row_queen, col_queen))

    return queens


def king_position(board):
    for row_king in range(len(board)):
        for col_king in range(len(board)):
            if board[row_king][col_king] == 'K':
                return row_king, col_king


chess_board_size = 8

board = [input().split() for _ in range(chess_board_size)]
print(len(board))
king_row, king_col = king_position(board)
print(king_row, king_col)
queens = deque(queens_position(board))
print(queens)
queen_captured_king = []

while queens:


    queen_row, queen_col = queens.popleft()

    queen_captured_king = diagonally(queen_row, queen_col, board, queen_captured_king)

    queen_captured_king = vertically(queen_row, queen_col, board, queen_captured_king)

    queen_captured_king = horizontally(queen_row, queen_col, board, queen_captured_king)



if len(queen_captured_king) == 0:
    print('The king is safe!')
else:
    for counter_queens in queen_captured_king:
        print(counter_queens)