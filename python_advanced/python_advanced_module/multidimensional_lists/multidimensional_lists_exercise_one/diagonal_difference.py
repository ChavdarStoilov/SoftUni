size_matrix = int(input())

matrix = []

for _ in range(size_matrix):
    matrix.append([int(x) for x in input().split()])

primary_diagonal = []
secondary_diagonal = []

for row in range(len(matrix)):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][size_matrix -1 -row])


diff = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(diff)