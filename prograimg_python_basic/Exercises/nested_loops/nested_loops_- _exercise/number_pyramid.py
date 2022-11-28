some_number = int(input())

current_number = 1
is_current_bigger_then_some_number = False

for first_number in range(1, some_number + 1):
    for second_number in range(1, first_number + 1):
        if current_number > some_number:
            is_current_bigger_then_some_number = True
            break

        print(str(current_number) + " ", end = "")
        current_number +=1

    if is_current_bigger_then_some_number:
        break

    print()