number_of_lines = int(input())

even_set = set()
odd_set = set()


for row in range(1, number_of_lines + 1):

    names = input()
    sum_of_char_ascii = 0

    for char in names:
        sum_of_char_ascii += int(ord(char))


    end_sum = sum_of_char_ascii // row

    if end_sum % 2 == 0:
        even_set.add(end_sum)
    else:
        odd_set.add(end_sum)


if sum(odd_set) == sum(even_set):
    print(', '.join(str(x) for x in odd_set.union(even_set)))
elif sum(odd_set) > sum(even_set):
    print(', '.join(str(x) for x in odd_set.difference(even_set)))
else:
    print(', '.join(str(x) for x in odd_set.symmetric_difference(even_set)))

