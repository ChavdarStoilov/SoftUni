def wagons(waiters, spaces):

    for wagon in range(len(spaces)):
        if waiters > 3:
            waiting = abs(4 - int(spaces[wagon]))
            waiters -= waiting
            spaces[wagon] += waiting
        else:
            spaces[wagon] += waiters
            waiters = 0

    if waiters > 0:
        print(f"There isn't enough space! {waiters} people in a queue!")

    elif sum(spaces) != len(spaces) * 4:
        print("The lift has empty spots!")

    end_result = [str(str_num) for str_num in spaces]
    return " ".join(end_result)


people_waiting = int(input())
wagons_spaces = list(map(int, input().split()))

print(wagons(people_waiting, wagons_spaces))