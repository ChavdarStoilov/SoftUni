rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

max_sum = float('-inf')
owner_row, owner_col = 0, 0

for row in range(rows -1):
    for cols in range(columns -1):
        temp_sum = matrix[row][cols] + matrix[row][cols + 1] + \
                   matrix[row + 1][cols] + matrix[row + 1][cols + 1]

        if temp_sum > max_sum:
            max_sum = temp_sum
            owner_row, owner_col = row, cols


print(f'{matrix[owner_row][owner_col]} {matrix[owner_row][owner_col + 1]}\n'
      f'{matrix[owner_row + 1][owner_col]} {matrix[owner_row + 1][owner_col + 1]}')
print(max_sum)
