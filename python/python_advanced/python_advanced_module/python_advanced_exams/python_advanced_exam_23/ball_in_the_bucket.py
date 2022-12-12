SIZE = 6

board = [input().split() for _ in range(SIZE)]

hit_bucket = []

points = 0

for _ in range(3):

    row, col = 0, 0
    place = [x for x in input() if x.isdigit()]

    if len(place) == 2:
        row, col = int(place[0]), int(place[1])
    elif len(place) == 4:
        row, col = int(place[0]+place[1]), int(place[2]+ place[3])

    if (row, col) not in hit_bucket:

        if 0 <= row < SIZE and 0 <= col < SIZE:
            if board[row][col] == 'B':
                hit_bucket.append((row, col))
                for rows in range(SIZE):
                    if board[rows][col].isdigit():
                        points += int(board[rows][col])

if points < 100:
    needed = 100 - points
    print(f'Sorry! You need {needed} points more to win a prize.')
elif 100 <= points <= 199:
    print(f'Good job! You scored {points} points, and you\'ve won Football.')
elif 200 <= points <= 299:
    print(f'Good job! You scored {points} points, and you\'ve won Teddy Bear.')
elif 300 >= points:
    print(f'Good job! You scored {points} points, and you\'ve won Lego Construction Set.')
