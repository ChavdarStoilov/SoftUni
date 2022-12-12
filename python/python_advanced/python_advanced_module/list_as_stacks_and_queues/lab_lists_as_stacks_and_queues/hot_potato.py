from collections import deque

def potato(kids, toss):

    while kids:
        kids.rotate(-toss)
        if len(kids) == 1:
            print(f'Last is {kids.pop()}')
        else:
            print(f'Removed {kids.pop()}')

kids = deque(input().split())
toss = int(input())

potato(kids, toss)