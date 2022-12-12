def print_rhombus(rows, size_n):
    print(' ' * (size_n - rows), end='')
    for _ in range(rows):
        print('* ', end='')
    print()


n = int(input())

for row in range(1, n):
    print_rhombus(row, n)

for row_two in range(n, -1, -1):
    print_rhombus(row_two, n)
