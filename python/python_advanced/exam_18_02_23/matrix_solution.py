def your_posi():
    for x in range(len(playground)):
        for y in range(len(playground)):
            if playground[x][y] == "B":
                return x, y

def counter_opponents():
    opponents = 0
    for x in range(len(playground)):
        for y in range(len(playground)):
            if playground[x][y] == "P":
                opponents += 1

    return opponents

moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

touched_opponents = 0
moves_made = 0

row, colm = input().split(" ")

playground = [input().split() for _ in range(int(row))]

opponents = counter_opponents()
your_posi_x, you_posi_y = your_posi()

while True:

    move = input()

    if move == "Finish" or opponents == 0:
        break

    your_new_x, your_new_y = int(your_posi_x + moves[move][0]), int(you_posi_y + moves[move][1])

    if int(row) > your_new_x and int(colm) > your_new_y:
        if playground[your_new_x][your_new_y] != "O":

            if playground[your_new_x][your_new_y] == "P":
                touched_opponents += 1
                opponents -= 1

            playground[your_posi_x][you_posi_y] = "-"
            your_posi_x, you_posi_y = your_new_x, your_new_y
            playground[your_new_x][your_new_y] = "B"
            moves_made += 1


print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")


