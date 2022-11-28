from collections import deque

vowels = deque(input().split())
consonants = input().split()

finder = {
    "rose": ['r', 'o', 's', 'e'],
    "tulip": ['t', 'u', 'l', 'i', 'p'],
    "lotus": ['l', 'o', 't', 'u', 's'],
    "daffodil": ['d', 'a', 'f', 'f', 'o', 'd', 'i', 'l']

}

while vowels and consonants:

    vowel = vowels.popleft()
    consonant = consonants.pop()

    if vowel in finder['rose']:
        finder['rose'].remove(vowel)
    if consonant in finder['rose']:
        finder['rose'].remove(consonant)

    if len(finder['rose']) == 0:
        break

    if vowel in finder['tulip']:
        finder['tulip'].remove(vowel)
    if consonant in finder['tulip']:
        finder['tulip'].remove(consonant)

    if len(finder['tulip']) == 0:
        break

    if vowel in finder['lotus']:
        finder['lotus'].remove(vowel)
    if consonant in finder['lotus']:
        finder['lotus'].remove(consonant)

    if len(finder['lotus']) == 0:
        break

    if vowel in finder['daffodil']:
        finder['daffodil'].remove(vowel)
    if consonant in finder['daffodil']:
        finder['daffodil'].remove(consonant)

    if len(finder['daffodil']) == 0:
        break

if len(finder['rose']) == 0:
    print('Word found: rose')

elif len(finder['tulip']) == 0:
    print('Word found: tulip')

elif len(finder['lotus']) == 0:
    print('Word found: lotus')

elif len(finder['daffodil']) == 0:
    print('Word found: daffodil')

else:
    print('Cannot find any word!')

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')
