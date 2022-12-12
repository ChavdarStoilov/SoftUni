from collections import deque


def convertor_time_to_seconds(time):
    hours, minutes, seconds = [int(t) for t in time.split(':')]

    return hours * 60 * 60 + minutes * 60 + seconds


def convertor_second_to_time(second):
    hour = second // (60 * 60)
    second %= (60 * 60)
    minutes = second // 60
    second %= 60

    return f'{hour:02d}:{minutes:02d}:{second:02d}'

robots = input().split(';')
start_time = input()

the_time = convertor_time_to_seconds(start_time)

items = deque()
robots_needed_time = {}
busy_until = {}


for robot in robots:
    name, time = robot.split('-')

    robots_needed_time[name] = int(time)
    busy_until[name] = -1

command = input()

while command != 'End':

    items.append(command)

    command = input()


while items:
    the_time = the_time +1 % (24 * 60 * 60)

    for bot, times in busy_until.items():

        if the_time >= times:
            busy_until[bot] = the_time + robots_needed_time[bot]
            print(f'{bot} - {items.popleft()} [{convertor_second_to_time(the_time)}]')
            break

    else:
        items.rotate(-1)