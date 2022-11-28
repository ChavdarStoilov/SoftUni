from collections import deque

def eat_cookie(move, posi, nice_kids, gifts_left):
    for cord in move.values():
        row = santa[0] + cord[0]
        col = santa[1] + cord[1]

        if the_map[row][col].isalpha():
            if the_map[row][col] == 'V':
                nice_kids += 1

            the_map[row][col] = '-'
            gifts_left -= 1

        if not gifts_left:
            break

    return gifts_left, nice_kids

def santa_position(city, size):
    nice_kid = [kid.count('V') for kid in city if 'V' in kid]

    for row in range(size):
        for col in range(size):
            if city[row][col] == 'S':
                city[row][col] = '-'
                return (row, col), sum(nice_kid)

gifts = int(input())
size_map = int(input())

the_map = [input().split() for _ in range(size_map)]

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

santa, total_nice_kids = santa_position(the_map, size_map)

nice_kids_visited = 0

while True:
    if not gifts or nice_kids_visited == total_nice_kids:
        break

    command = input()

    if command == 'Christmas morning' or command == '':
        break

    santa = (santa[0] + moves[command][0], santa[1] + moves[command][1])

    if 0 <= santa[0] < size_map and 0 <= santa[1] < size_map:
        type_child = the_map[santa[0]][santa[1]]

        if type_child == 'V':
            gifts -= 1
            nice_kids_visited += 1

        elif type_child == 'C':
            gifts, nice_kids_visited = eat_cookie(moves, santa, nice_kids_visited, gifts)


        the_map[santa[0]][santa[1]] = '-'


the_map[santa[0]][santa[1]] = 'S'

if not gifts and nice_kids_visited < total_nice_kids:
    print("Santa ran out of presents!")

for i in the_map:
    print(' '.join(i))

if nice_kids_visited == total_nice_kids:
    print(f'Good job, Santa! {nice_kids_visited} happy nice kid/s.')
else:
    print(f'No presents for {total_nice_kids - nice_kids_visited} nice kid/s.')