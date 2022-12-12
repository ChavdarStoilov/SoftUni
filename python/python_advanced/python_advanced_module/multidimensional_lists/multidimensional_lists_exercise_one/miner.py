from collections import deque

def check_finder(the_field, position, route, coals, coal):

    found = field[position[0]][position[1]]

    if found == 'c':
        coals += 1
        coal -= 1
    elif found == 'e':
        route = True

    return the_field, position, route, coals, coal

def locate_field(position, coals):


    for row in range(len(field)):
        for col in range(len(field)):
            place = field[row][col]

            if place == 'c':
                coals += 1
            elif place == 's':
                position = (row, col)

    return position, coals


size_of_field = int(input())
moves = deque(input().split())
field = [input().split() for _ in range(size_of_field)]

moves_on_field = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

count_coal = 0
all_coals = 0
end_route = False
miner_position = ()

miner_position, all_coals = locate_field(miner_position, all_coals)

while True:

    if end_route:
        print(f'Game over! {miner_position}')
        break

    if all_coals == 0:
        print(f'You collected all coal! {miner_position}')
        break

    if moves:
        move = moves.popleft()


        if move == 'up' and 0 <= miner_position[0] + moves_on_field['up'][0] < size_of_field and \
                0 <= miner_position[1] + moves_on_field['up'][1] < size_of_field:

            field[miner_position[0]][miner_position[1]] = '*'
            miner_position = (miner_position[0] + moves_on_field['up'][0],
                              miner_position[1] + moves_on_field['up'][1])

            field, miner_position, end_route, count_coal, all_coals = check_finder(field, miner_position,
                                                                                   end_route, count_coal, all_coals)


        elif move == 'down' and 0 <= miner_position[0] + moves_on_field['down'][0] < size_of_field and \
                0 <= miner_position[1] + moves_on_field['down'][1] < size_of_field:

            field[miner_position[0]][miner_position[1]] = '*'
            miner_position = (miner_position[0] + moves_on_field['down'][0],
                              miner_position[1] + moves_on_field['down'][1])

            field, miner_position, end_route, count_coal, all_coals = check_finder(field, miner_position,
                                                                                   end_route, count_coal, all_coals)


        elif move == 'right' and 0 <= miner_position[0] + moves_on_field['right'][0] < size_of_field and \
                0 <= miner_position[1] + moves_on_field['right'][1] < size_of_field:

            field[miner_position[0]][miner_position[1]] = '*'

            miner_position = (miner_position[0] + moves_on_field['right'][0],
                              miner_position[1] + moves_on_field['right'][1])

            field, miner_position, end_route, count_coal, all_coals = check_finder(field, miner_position,
                                                                                   end_route, count_coal, all_coals)


        elif move == 'left' and 0 <= miner_position[0] + moves_on_field['left'][0] < size_of_field and \
                0 <= miner_position[1] + moves_on_field['left'][1] < size_of_field:

            field[miner_position[0]][miner_position[1]] = '*'
            miner_position = (miner_position[0] + moves_on_field['left'][0],
                              miner_position[1] + moves_on_field['left'][1])

            field, miner_position, end_route, count_coal, all_coals = check_finder(field, miner_position,
                                                                                   end_route, count_coal, all_coals)


        field[miner_position[0]][miner_position[1]] = 's'


    else:
        print(f'{all_coals} pieces of coal left. {miner_position}')
        break
