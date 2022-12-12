matrix_size = int(input())

matrix = []

end_result = []

for idx_row in range(matrix_size):
    rows = [int(x) for x in input().split(', ')]

    matrix.append(rows)

    for num in matrix[idx_row]:
        end_result.append(num)

print(end_result)