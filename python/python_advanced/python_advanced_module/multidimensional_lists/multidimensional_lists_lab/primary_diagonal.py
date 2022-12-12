matrix_size = int(input())

matrix = []
sum_diagonal = 0

for _ in range(matrix_size):

    matrix.append([int(x) for x in input().split()])


for idx_row in range(len(matrix)):
    for idx_colum in range(matrix_size):
        if idx_row == idx_colum:
            sum_diagonal += matrix[idx_row][idx_colum]


print(sum_diagonal)