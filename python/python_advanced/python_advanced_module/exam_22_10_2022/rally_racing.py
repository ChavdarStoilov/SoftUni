def tunnels(maps):
    tunnel = []

    for row in range(len(maps)):
        for col in range(len(maps)):
            if maps[row][col] == 'T':
                tunnel.append([row, col])

    return tunnel

SIZE = int(input())

race_num = str(input())

trace = [input().split() for _ in range(SIZE)]

kilometer = 0

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

tunnel = tunnels(trace)
car_row, car_col = [0, 0]

while True:

    move = input()

    if move == 'End':
        print(f'Racing car {race_num} DNF.')
        break

    car_row, car_col = car_row + moves[move][0], car_col + moves[move][1]

    if trace[car_row][car_col] == 'T':

        kilometer += 30
        trace[car_row][car_col] = '.'

        car_row, car_col = [tun for tun in tunnel if tun[0] != car_row][0]
        trace[car_row][car_col] = '.'

    elif trace[car_row][car_col] == 'F':
        kilometer += 10
        print(f'Racing car {race_num} finished the stage!')

        break
    else:
        kilometer += 10


trace[car_row][car_col] = 'C'
print(f'Distance covered {kilometer} km.')

for the_trace in trace:
    print(''.join(the_trace))
