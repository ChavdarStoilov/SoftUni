names_gifts = input().split()
command = input().split()

final_list = []

while " ".join(command) != "No Money":
    if command[0] == "OutOfStock":
        for index in range(len(names_gifts)):
            if command[1] == names_gifts[index]:
                names_gifts.pop(index)
                names_gifts.insert(index, None)
    elif command[0] == "Required":
        if len(names_gifts) > int(command[2]) >= 0:
            names_gifts.pop(int(command[2]))
            names_gifts.insert(int(command[2]), command[1])
    elif command[0] == "JustInCase":
        names_gifts.pop(-1)
        names_gifts.append(command[1])

    command = input().split()


for none_values in range(len(names_gifts)):
    if None in names_gifts:
        names_gifts.remove(None)

print(" ".join(names_gifts))