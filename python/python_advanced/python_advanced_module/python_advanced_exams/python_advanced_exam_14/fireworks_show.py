from collections import deque

firework_effect = deque([x for x in input().split(', ')])
explosive_power = [x for x in input().split(', ')]

fireworks = {
    'Palm': 0,
    'Willow': 0,
    'Crossette': 0

}

while firework_effect and explosive_power:

    firework = int(firework_effect[0])
    power = int(explosive_power[-1])

    if firework <= 0:
        firework_effect.popleft()
        continue

    if power <= 0:
        explosive_power.pop()
        continue

    explosive = firework + power

    if explosive % 3 == 0 and explosive % 5 != 0:
        fireworks['Palm'] += 1
        firework_effect.popleft()
        explosive_power.pop()

    elif explosive % 3 != 0 and explosive % 5 == 0:
        fireworks['Willow'] += 1
        firework_effect.popleft()
        explosive_power.pop()

    elif explosive % 3 == 0 and explosive % 5 == 0:
        fireworks['Crossette'] += 1
        firework_effect.popleft()
        explosive_power.pop()

    else:
        firework_effect[0] = firework - 1
        firework_effect.rotate(-1)

if fireworks['Palm'] >= 3 and fireworks['Willow'] >= 3 and fireworks['Crossette'] >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effect:
    print(f'Firework Effects left: {", ".join(firework_effect)}')

if explosive_power:
    print(f'Explosive Power left: {", ".join(explosive_power)}')


for fire, counter in fireworks.items():
    print(f'{fire} Fireworks: {counter}')

