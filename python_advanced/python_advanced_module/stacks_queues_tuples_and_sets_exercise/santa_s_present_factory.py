from collections import deque

materials = input().split()
magic_level = deque(input().split())

crafted_toys = {'Doll': {'count': 0, 'magic_needed': 150},
                'Wooden train': {'count': 0, 'magic_needed': 250},
                'Teddy bear': {'count': 0, 'magic_needed': 300},
                'Bicycle': {'count': 0, 'magic_needed': 400}
                }


while magic_level and materials:

    flag = False

    if materials[-1] == "0":
        materials.pop()
        flag = True

    if magic_level[0] == "0":
        magic_level.popleft()
        flag = True

    if flag:
        continue

    the_total_level = int(magic_level[0]) * int(materials[-1])

    if the_total_level == crafted_toys['Doll']['magic_needed']:
        crafted_toys['Doll']['count'] += 1
        magic_level.popleft()
        materials.pop()

    elif the_total_level == crafted_toys['Wooden train']['magic_needed']:
        crafted_toys['Wooden train']['count'] += 1
        magic_level.popleft()
        materials.pop()

    elif the_total_level == crafted_toys['Teddy bear']['magic_needed']:
        crafted_toys['Teddy bear']['count'] += 1
        magic_level.popleft()
        materials.pop()

    elif the_total_level == crafted_toys['Bicycle']['magic_needed']:
        crafted_toys['Bicycle']['count'] += 1
        magic_level.popleft()
        materials.pop()

    else:
        if the_total_level < 0:
            new_material = str(int(materials.pop()) + int(magic_level.popleft()))
            materials.append(new_material)


        elif the_total_level > 0:
            materials[-1] = str(int(materials[-1]) + 15)
            magic_level.popleft()



if crafted_toys['Doll']['count'] > 0 and crafted_toys['Wooden train']['count'] > 1 or \
        crafted_toys['Bicycle']['count'] > 0 and crafted_toys['Teddy bear']['count'] > 1:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

materials.reverse()

if materials:
    print(f'Materials left: {", ".join(materials)}')
elif magic_level:
    print(f'Magic left: {", ".join(magic_level)}')

for toys in sorted(crafted_toys):
    if crafted_toys[toys]['count'] > 0:
        print(f'{toys}: {crafted_toys[toys]["count"]}')
