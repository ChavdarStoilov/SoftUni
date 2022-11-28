from collections import deque

chocolates = input().split(', ')
milks = deque(input().split(', '))

shakes = 0

while shakes < 5 and chocolates and milks:
    flag = False
    if chocolates[-1] <= '0':
        chocolates.pop()
        flag =True

    if milks[0] <= '0':
        milks.popleft()
        flag = True

    if flag:
        continue

    if chocolates[-1] == milks[0]:
        shakes += 1
        chocolates.pop()
        milks.popleft()
    else:
        milks.rotate(-1)
        chocolates[-1] = str(int(chocolates[-1]) - 5)



if shakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolates:
    print(f'Chocolate: {", ".join(chocolates)}')
else:
    print('Chocolate: empty')

if milks:
    print(f'Milk: {", ".join(milks)}')
else:
    print('Milk: empty')