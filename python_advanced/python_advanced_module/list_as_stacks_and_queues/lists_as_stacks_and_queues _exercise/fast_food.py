from collections import deque

def restaurant(quantity, count_of_order):

    while count_of_order:
        if count_of_order[0] <= quantity:
            quantity -= count_of_order.popleft()

        elif count_of_order[0] > quantity:
            return f'Orders left: {" ".join([str(count_of_order.popleft()) for _ in range(len(count_of_order))])}'

    return 'Orders complete'


quantity_of_the_food = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

print(restaurant(quantity_of_the_food, orders))

