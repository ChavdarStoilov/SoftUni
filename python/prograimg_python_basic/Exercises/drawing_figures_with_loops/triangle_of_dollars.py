number = int(input())

for row in range(0, number):
    for down in range(row + 1):
        print("$", end=" ")
    print()