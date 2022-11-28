from collections import deque

male = [int(m) for m in input().split()]
female = deque([int(f) for f in input().split()])


matches = 0

while female and male:

    first_female = female[0]
    last_male = male[-1]

    if first_female <= 0:
        female.popleft()
        continue


    if last_male <= 0:
        male.pop()
        continue


    if first_female % 25 == 0:
        female.popleft()
        if not female:
            break

        female.popleft()
        continue

    if last_male % 25 == 0:
        male.pop()
        if not male:
            break
        male.pop()
        continue

    if first_female == last_male:
        female.popleft()
        male.pop()
        matches += 1
    else:
        female.popleft()
        male[-1] -= 2


print(f'Matches: {matches}')

if male:
    male.reverse()
    print(f"Males left: {', '.join([str(m) for m in male])}")
else:
    print('Males left: none')

if female:
    print(f"Females left: {', '.join([str(f) for f in female])}")
else:
    print('Females left: none')