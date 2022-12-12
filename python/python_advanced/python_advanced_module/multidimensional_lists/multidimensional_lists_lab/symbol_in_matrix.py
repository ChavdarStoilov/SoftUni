size_of_matrix = int(input())

matrix = []

for _ in range(size_of_matrix):
    row = input()
    matrix.append(row)



symbol = input()
founded = False
for idx_row in range(size_of_matrix):
    for idx_colum in range(len(matrix[idx_row])):
        if symbol == matrix[idx_row][idx_colum]:
            print(f'({idx_row}, {idx_colum})')
            founded = True
            break

    if founded:
        break


if not founded:
    print(f'{symbol} does not occur in the matrix')