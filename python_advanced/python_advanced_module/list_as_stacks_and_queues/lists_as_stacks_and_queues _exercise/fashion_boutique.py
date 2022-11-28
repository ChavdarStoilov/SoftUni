def boutique(boxs, capacity):
    rackets = 1
    temp_capacity = 0

    while boxs:
        if temp_capacity + boxs[-1] <= capacity:
            temp_capacity += boxs.pop()
            if temp_capacity == capacity:
                if boxs:
                    rackets += 1
                    temp_capacity = 0

        elif temp_capacity + boxs[-1] > capacity:
            rackets += 1
            temp_capacity = 0
            temp_capacity += boxs.pop()




    return rackets

clothes = list(map(int, input().split()))
capacity_of_a_rack = int(input())

print(boutique(clothes, capacity_of_a_rack))