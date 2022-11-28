rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = float('-inf')
root_row, root_col = 0, 0

for row in range(rows - 2):
    for col in range(cols - 2):
        temp_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
                   matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
                   matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

        if temp_sum > max_sum:
            max_sum = temp_sum
            root_row, root_col = row, col

print(f'Sum = {max_sum}')
print(f'{matrix[root_row][root_col]} {matrix[root_row][root_col + 1]} {matrix[root_row][root_col + 2]}\n'
      f'{matrix[root_row + 1][root_col]} {matrix[root_row + 1][root_col + 1]} {matrix[root_row + 1][root_col + 2]}\n'
      f'{matrix[root_row + 2][root_col]} {matrix[root_row + 2][root_col + 1]} {matrix[root_row + 2][root_col + 2]}')