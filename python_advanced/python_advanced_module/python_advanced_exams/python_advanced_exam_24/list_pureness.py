from collections import deque

def best_list_pureness(*args):
    list_pureness = deque(args[0])
    number_of_rotation = args[1]

    best_pureness = 0
    count_rotations = 0

    for number_rotation in range(number_of_rotation + 1):

        current_pureness = 0

        for numb in list_pureness:
            current_pureness += numb * list_pureness.index(numb)

        if current_pureness > best_pureness:
            best_pureness = current_pureness
            count_rotations = number_rotation

        list_pureness.rotate()

    return f"Best pureness {best_pureness} after {count_rotations} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
