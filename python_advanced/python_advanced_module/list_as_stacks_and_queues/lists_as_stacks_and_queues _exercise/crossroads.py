from collections import deque

green_light_second = int(input())
free_window = int(input())

crashed_car = ''
crashed_bool = False

cars_queue = deque()
car = input()

while car != 'END':

    cars = car

    while cars != 'green':
        if cars != 'green':
            crashed_car = cars

        for ch in cars:
            cars_queue.append(ch)

        cars = input()


    for _ in range(green_light_second + free_window + 1):
        if cars_queue:
            cars_queue.popleft()
        else:
            break

    if len(cars_queue) != 0:
        crashed_bool = True
        break

    car = input()


if not crashed_bool:
    print('Everyone is safe.\n'
          '')
else:
    print(f'A crash happened!\n'
          f'{crashed_car} was hit at {cars_queue.popleft()}.')