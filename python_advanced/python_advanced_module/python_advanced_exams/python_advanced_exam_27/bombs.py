from collections import deque


def check_filled(materials):
    if materials['Datura Bombs']['counter'] >= 3 and materials['Cherry Bombs']['counter'] >= 3 and \
            materials['Smoke Decoy Bombs']['counter'] >= 3:
        return True


def mixing(effect, casing, materials):
    bomb_effect = effect[0]
    bomb_casing = casing[-1]
    mixed_bombs = bomb_effect + bomb_casing

    if materials['Datura Bombs']['sum'] == mixed_bombs:
        materials['Datura Bombs']['counter'] += 1
        effect.popleft()
        casing.pop()

    elif materials['Cherry Bombs']['sum'] == mixed_bombs:
        materials['Cherry Bombs']['counter'] += 1
        effect.popleft()
        casing.pop()

    elif materials['Smoke Decoy Bombs']['sum'] == mixed_bombs:
        materials['Smoke Decoy Bombs']['counter'] += 1
        effect.popleft()
        casing.pop()

    else:
        casing[-1] -= 5

    return effect, casing, materials


bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casings = [int(x) for x in input().split(', ')]

materials = {
    'Datura Bombs': {'sum': 40, 'counter': 0},
    'Cherry Bombs': {'sum': 60, 'counter': 0},
    'Smoke Decoy Bombs': {'sum': 120, 'counter': 0}
}

while bomb_effects and bomb_casings:

    if check_filled(materials):
        break

    bomb_effects, bomb_casings, materials = mixing(bomb_effects, bomb_casings, materials)



if check_filled(materials):
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print('You don\'t have enough materials to fill the bomb pouch.')


if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print('Bomb Effects: empty')

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print('Bomb Casings: empty')


ordered = sorted(materials.items(), key=lambda x: x[0])

for material, counter in ordered:

    print(f'{material}: {counter["counter"]}')

