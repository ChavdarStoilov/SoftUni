from collections import deque

bees = deque(input().split())
nectar = input().split()
symbol = deque(input().split())

load = 0

while nectar and bees:

    if 0 < int(bees[0]) <= int(nectar[-1]) > 0:

        collect = 0
        temp_symbol = symbol.popleft()

        if temp_symbol == '+':
            collect = abs(int(bees.popleft()) + int(nectar.pop()))
        elif temp_symbol == '-':
            collect = abs(int(bees.popleft()) - int(nectar.pop()))
        elif temp_symbol == '*':
            collect = abs(int(bees.popleft()) * int(nectar.pop()))
        elif temp_symbol == '/':
            collect = abs(int(bees.popleft()) / int(nectar.pop()))

        load += collect
    else:
        nectar.pop()


print(f'Total honey made: {load}')

if bees:
    print(f"Bees left: {', '.join(bees)}")
elif nectar:
    print(f"Nectar left: {', '.join(nectar)}")