rows, cols = [int(x) for x in input().split()]


matrix = []
char = 97
for row in range(rows):
    the_row = []
    start_word = chr(char) * 3

    temp_char = char
    for col in range(cols):

        the_word = start_word[0] + chr(temp_char) + start_word[-1]
        the_row.append(the_word)
        temp_char += 1

    char += 1
    matrix.append(the_row)

for m in matrix:
    print(' '.join(m))