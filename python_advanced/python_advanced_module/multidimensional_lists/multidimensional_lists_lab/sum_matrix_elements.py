rows, columns = [int(x) for x in input().split(', ')]

matrix = []
sum_elements = 0

for idx in range(rows):
    matrix.append([int(x) for x in input().split(', ')])



    for idx_colum in range(columns):
        sum_elements += matrix[idx][idx_colum]




print(sum_elements)
print(matrix)