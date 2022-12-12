rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]


while True:
    command = input()

    if command == 'END':
        break

    the_command = command.split()

    if 'swap' not in the_command or len(the_command) != 5:
        print('Invalid input!')
        continue

    action, row1, col1, row2, col2 = command.split()
    row1 = int(row1)
    col1 = int(col1)
    row2 = int(row2)
    col2 = int(col2)

    if row1 >= rows or row1 < 0 or row2 >= rows or row2 < 0 or col1 >= cols or col1 < 0 or col2 >= cols or col2 < 0:
        print('Invalid input!')
        continue


    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for end_matrix in matrix:
        print(' '.join(map(str, end_matrix)))
