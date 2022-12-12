rows, columns = [int(x) for x in input().split(', ')]

matrix = []


for _ in range(rows):
    matrix.append([int(x) for x in input().split()])


for idx_colum in range(columns):
    sum_columns = 0

    for idx_row in range(rows):
        sum_columns += matrix[idx_row][idx_colum]

    print(sum_columns)