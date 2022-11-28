width = int(input())
length = int(input())
part = input()

left = width * length
count_parts = 0

while part != "STOP":
    parts = int(part)
    left -= parts

    if left < 0:
        count_parts = abs(left)
        break


    count_parts += 1
    part = input()



if parts > left:
    print(f"No more cake left! You need {count_parts} pieces more.")
else:
    print(f"{left} pieces are left.")
