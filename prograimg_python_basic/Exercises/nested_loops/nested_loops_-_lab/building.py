number_floor = int(input())
number_rooms = int(input())

type_of_floor = ""

for floor in range(number_floor, 0 , -1):
    for room in range(number_rooms):
        if floor == number_floor:
            type_of_floor = "L"
        elif floor % 2 != 0:
            type_of_floor = "A"
        else:
            type_of_floor = "O"

        print(f"{type_of_floor}{floor}{room}", end=" ")
    print()