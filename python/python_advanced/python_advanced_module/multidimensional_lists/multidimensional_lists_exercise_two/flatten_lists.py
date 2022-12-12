first_list = input().split('|')
second_list = [li.split() for li in first_list[::-1]]

test = []

for i in second_list:
    test.extend(i)

print(' '.join(test))