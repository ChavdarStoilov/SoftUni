size_matrix = int(input())

matrix = []

for _ in range(size_matrix):
    matrix.append([int(x) for x in input().split(', ')])

primary_diagonal = []
secondary_diagonal = []

for row in range(len(matrix)):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][size_matrix -1 -row])


print(f'Primary diagonal: {", ".join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}')