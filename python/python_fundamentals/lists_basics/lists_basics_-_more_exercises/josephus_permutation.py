numbers_separated = input().split()
number = int(input())

executed_people = 0

result = []

idx = 0

while len(numbers_separated) > 0:
    executed_people += 1

    if executed_people % number == 0:
        result.append(int(numbers_separated.pop(idx)))
    else:
        idx += 1

    if idx >= len(numbers_separated):
        idx = 0



print(str(result).replace(" ", ""))