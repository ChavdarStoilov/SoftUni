from collections import deque

def dispenser(the_water, persons):

    command = input()
    while command != 'End':

        action = command.split()

        if action[0] == 'refill':
            the_water += int(action[1])

        else:
            if int(action[0]) <= the_water:
                the_water -= int(action[0])
                print(f'{persons.popleft()} got water')
            else:
                print(f'{persons.popleft()} must wait')

        command = input()

    return f'{the_water} liters left'

quality_of_water = int(input())
command = input()

que = deque()

while command != 'Start':
    que.append(command)

    command = input()

print(dispenser(quality_of_water, que))