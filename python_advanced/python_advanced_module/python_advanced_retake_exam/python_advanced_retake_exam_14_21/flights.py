from collections import deque

def flights(*args):
    statistic = {}

    planes = [plane for plane in args if isinstance(plane, str)]
    passengers = deque([passenger for passenger in args if isinstance(passenger, int)])

    for flight in planes:
        if flight == 'Finish':
            return statistic

        if flight not in statistic.keys():
            statistic[flight] = 0
        statistic[flight] += passengers.popleft()






print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))