def check_attack(killers, max_kills, the_board, moves):

    for i in moves:
        print(the_board[i[0]][i[1]])


size_of_board = int(input())

board = [input().split() for _ in range(size_of_board)]

moves =[
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1)
]


max_attacker = 0
count_killer = 0

for row in range(size_of_board):
    for col in range(size_of_board):
        for hors in board[row][col]:
            if hors == 'K':
                count_killer, max_attacker, board, moves = check_attack(count_killer, max_attacker, board, moves)