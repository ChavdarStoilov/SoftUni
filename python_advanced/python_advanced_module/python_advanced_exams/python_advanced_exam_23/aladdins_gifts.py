from collections import deque

materials = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))

crafted = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0

}

while materials and magic_level:

    collected_level = materials[-1] + magic_level[0]

    if collected_level < 100:
        if collected_level % 2 == 0:
            collected_level = (materials[-1] * 2) + (magic_level[0] * 3)
        elif collected_level % 2 != 0:
            collected_level = collected_level * 2

    if collected_level > 499:
        collected_level = collected_level / 2

    if 100 <= collected_level <= 199:
        crafted['Gemstone'] += 1
    elif 200 <= collected_level <= 299:
        crafted['Porcelain Sculpture'] += 1
    elif 300 <= collected_level <= 399:
        crafted['Gold'] += 1
    elif 400 <= collected_level <= 499:
        crafted['Diamond Jewellery'] += 1

    materials.pop()
    magic_level.popleft()

if crafted['Gemstone'] > 0 and crafted['Porcelain Sculpture'] > 0 or crafted['Gold'] > 0 and crafted['Diamond Jewellery'] > 0:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials])}')
if magic_level:
    print(f'Magic left: {", ".join([str(x) for x in magic_level])}')

for material, count in crafted.items():
    if count > 0:
        print(f'{material}: {count}')
