size_matrix = int(input())

matrix = [[int(i) for i in input().split()] for _ in range(size_matrix)]

while True:
    command = input().split()

    if command[0] == "END":
        break

    action, row, col, value = command
    row = int(row)
    col = int(col)
    value = int(value)

    if 0 <= row < size_matrix and 0 <= col < size_matrix:
        if action == 'Add':
            matrix[row][col] += value

        elif action == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

for resul in matrix:
    print(' '.join(str(i) for i in resul))