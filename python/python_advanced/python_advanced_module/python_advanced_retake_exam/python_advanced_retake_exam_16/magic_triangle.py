def get_magic_triangle(number):
    magic_triangle = []

    for row in range(number):
        if row == 0:
            magic_triangle.append([1])

        else:
            magic_triangle.append([])

            for col in range(len(magic_triangle)):
                if col == 0:
                    magic_triangle[row].append(magic_triangle[row - 1][0])

                else:
                    combined = 0
                    combined += magic_triangle[row - 1][col - 1]

                    if len(magic_triangle) - 1 != col:
                        combined += magic_triangle[row - 1][col]

                    magic_triangle[row].append(combined)

    return magic_triangle

print(get_magic_triangle(5))