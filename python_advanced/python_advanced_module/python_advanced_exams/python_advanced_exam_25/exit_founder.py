def game(player, move_to, winner, rest, lose):
    if move_to == 'W':
        rest = True
        print(f'{player} hits a wall and needs to rest.')
    elif move_to == 'T':
        lose = True
    elif move_to == 'E':
        winner = True

    return rest, winner, lose


def fist_player(player, board, rest):
    winner = False
    lose = False
    rest = rest
    moves = input()

    if rest:
        rest = False
        return rest, winner, the_board, lose


    row, col = int(moves[1]), int(moves[4])
    move_to = board[row][col]

    rest, winner, lose = game(player, move_to, winner, rest, lose)

    return rest, winner, the_board, lose


def second_player(player, board, rest):
    winner = False
    lose = False
    rest = rest
    moves = input()

    if rest:
        rest = False
        return rest, winner, the_board, lose

    row, col = int(moves[1]), int(moves[4])
    move_to = board[row][col]

    rest, winner, lose = game(player, move_to, winner, rest, lose)

    return rest, winner, the_board, lose


player_one, player_two = input().split(', ')

the_board = [input().split() for _ in range(6)]

rest_one = False
rest_two = False
lose_one = False
lose_two = False
player_one_win = False
player_two_win = False

while True:

    if lose_two:
        print(f'{player_two} is out of the game! The winner is {player_one}.')
        break
    elif player_two_win:
        print(f'{player_two} found the Exit and wins the game!')
        break
    else:
        rest_one, player_one_win, the_board, lose_one = fist_player(player_one, the_board, rest_one)

    if lose_one:
        print(f'{player_one} is out of the game! The winner is {player_two}.')
        break
    elif player_one_win:
        print(f'{player_one} found the Exit and wins the game!')
        break
    else:
        rest_two, player_two_win, the_board, lose_two = second_player(player_two, the_board, rest_two)