width = int(input())
length = int(input())
height = int(input())

room = width * length * height
box = input()
sum_of_boxes = 0

while box != "Done":
    boxs = int(box)
    sum_of_boxes += boxs

    if room < sum_of_boxes:
        break


    box = input()

if room < sum_of_boxes:
    need_more = sum_of_boxes - room
    print(f"No more free space! You need {need_more} Cubic meters more.")
else:
    left = room - sum_of_boxes
    print(f"{left} Cubic meters left.")