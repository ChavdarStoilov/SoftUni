rows, cols = [int(x) for x in input().split()]
some_word = input()

idx = 0

for row in range(rows):
    matrix = [None] * cols

    if row % 2 == 0:
        for col in range(0, cols, 1):
            matrix[col] = some_word[idx % len(some_word)]
            idx += 1

    else:
        for col in range(cols - 1, -1, -1):
            matrix[col] = some_word[idx % len(some_word)]
            idx += 1


    print(''.join(matrix))