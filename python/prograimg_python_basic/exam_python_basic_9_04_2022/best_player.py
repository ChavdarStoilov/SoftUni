name_of_player = str(input())

winner = ""
goals = 0

while name_of_player != "END":
    count_goals = int(input())

    if count_goals > goals:
        winner = name_of_player
        goals = count_goals

    if count_goals >= 10:
        break

    name_of_player = str(input())


print(f"{winner} is the best player!")

if goals >= 3:
    print(f"He has scored {goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals} goals.")
