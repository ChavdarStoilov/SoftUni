from collections import deque

eggs = deque([int(egge) for egge in input().split(', ')])
piece_of_paper = [int(piece) for piece in input().split(', ')]

boxes = 0

while eggs and piece_of_paper:

    if eggs[0] <= 0:
        eggs.popleft()

    elif eggs[0] == 13:
        eggs.popleft()
        piece_of_paper[0], piece_of_paper[-1] = piece_of_paper[-1], piece_of_paper[0]

    else:
        if eggs[0] + piece_of_paper[-1] <= 50:
            boxes += 1
            eggs.popleft()
            piece_of_paper.pop()
        else:
            eggs.popleft()
            piece_of_paper.pop()


if boxes > 0:
    print(f'Great! You filled {boxes} boxes.')

else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(egge) for egge in eggs])}")
if piece_of_paper:
    print(f"Pieces of paper left: {', '.join([str(pieces) for pieces in piece_of_paper])}")