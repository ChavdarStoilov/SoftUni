SIZE = 7

players = {player: [501, 0] for player in input().split(', ')}
board = [input().split() for _ in range(7)]

throws = 0
player = ''

while True:
    targets = input().replace('(', '').replace(')', '').split(', ')

    target_row, target_col = int(targets[0]), int(targets[1])

    first_number = int(board[target_row][0])
    second_number = int(board[target_row][-1])
    third_number = int(board[0][target_col])
    four_number = int(board[-1][target_col])

    the_sum = first_number + second_number + third_number + four_number

    throws += 1

    if throws % 2 == 0:
        player = list(players.keys())[1]
    elif throws % 2 != 0:
        player = list(players.keys())[0]

    players[player][1] += 1

    if SIZE - 1 < target_row or target_row < 0 or SIZE - 1 < target_col or target_col < 0:
        continue

    elif board[target_row][target_col].isdigit():
        players[player][0] -= int(board[target_row][target_col])

    elif board[target_row][target_col] == 'D':
        players[player][0] -= (the_sum * 2)

    elif board[target_row][target_col] == 'T':
        players[player][0] -= (the_sum * 3)

    elif board[target_row][target_col] == 'B':
        print(f'{player} won the game with {throws} throws!')
        break

    if players[player][0] <= 0:
        print(f'{player} won the game with {players[player][1]} throws!')
        break
