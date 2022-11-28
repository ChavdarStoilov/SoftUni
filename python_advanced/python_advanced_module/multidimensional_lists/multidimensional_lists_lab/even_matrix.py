matrix_size = int(input())

matrix = [[int(x) for x in input().split(', ') if int(x) % 2 == 0] for _ in range(matrix_size)]

print(matrix)
