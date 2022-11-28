from collections import deque

bowls = [int(b) for b in input().split(', ')]
customers = deque(int(c) for c in input().split(', '))


while bowls and customers:

    bowl = bowls[-1]
    customer = customers[0]

    if bowl == customer:
        bowls.pop()
        customers.popleft()
    elif bowl > customer:
        bowls[-1] -= customer
        customers.popleft()
    elif bowl < customer:
        customers[0] -= bowl
        bowls.pop()

if customers:
    print('Out of ramen! You didn\'t manage to serve all customers.')
    print(f"Customers left: {', '.join([str(c) for c in customers])}")
else:
    print('Great job! You served all the customers.')
    if bowls:
        print(f"Bowls of ramen left: {', '.join([str(b) for b in bowls])}")