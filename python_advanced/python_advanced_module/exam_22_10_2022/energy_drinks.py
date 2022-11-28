from collections import deque

coffeines = [int(c) for c in input().split(', ')]
drinks = deque([int(d) for d in input().split(', ')])


total_coffeine = 0

while coffeines and drinks:

    if 0 >= total_coffeine > 300:
        break

    coffeine = coffeines[-1]
    drink = drinks[0]

    sum_of_drink_coffeine = drink * coffeine

    if sum_of_drink_coffeine <= 300 - total_coffeine:
        coffeines.pop()
        drinks.popleft()
        total_coffeine += sum_of_drink_coffeine


    else:
        coffeines.pop()
        drinks.append(drinks.popleft())
        if total_coffeine > 0:
            total_coffeine -= 30


if drinks:
    print(f'Drinks left: {", ".join([str(d) for d in drinks])}')

else:
    print('At least Stamat wasn\'t exceeding the maximum caffeine.')

print(f'Stamat is going to sleep with {total_coffeine} mg caffeine.')