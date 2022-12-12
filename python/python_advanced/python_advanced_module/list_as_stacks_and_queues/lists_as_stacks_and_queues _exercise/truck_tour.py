from collections import deque

pumps = int(input())

circle_road = deque()


for _ in range(pumps):

    pumps_items = list(map(int, input().split()))
    circle_road.append(pumps_items)


for tried in range(pumps):
    failed = False
    tank = 0

    for fuel, distance in circle_road:
        tank += fuel

        if distance > tank:
            circle_road.popleft()
            failed = True
            break
        else:
            tank -= distance


    if not failed:
        print(tried)
        break