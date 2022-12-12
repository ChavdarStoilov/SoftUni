text = input().split()

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

left_side = []
right_side = []

colors = []

for idx in range(len(text)):

    if len(text) / 2 > idx:
        left_side.append(text[idx])
    else:
        right_side.append(text[idx])



while left_side:

    if left_side[0] + right_side[-1] in main_colors:
        colors.append(left_side[0] + right_side[-1])
        left_side.remove(left_side[0])
        left_side.remove(left_side[-1])
    else:
        left_side[0] = left_side[0][:len(left_side[0])-1]
        right_side[-1] = right_side[-1][:len(right_side[-1])-1]
        left_side[0], left_side[1], left_side[2] = left_side[1], left_side[2], left_side[0]
        right_side[0], right_side[1], right_side[-1] = right_side[-1], right_side[0], right_side[1]

