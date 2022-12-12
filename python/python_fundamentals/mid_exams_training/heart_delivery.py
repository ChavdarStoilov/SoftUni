def delivery_func(the_houses):
    command = input()
    current_index = 0
    counter_houses = 0

    while command != "Love!":
        jump_length = command.split()
        current_index += int(jump_length[1])
        if jump_length[0] == "Jump":
            if the_houses[current_index] == 0:
                print(f"Place {current_index} already had Valentine's day.")
                continue

            if int(jump_length[1]) > len(the_houses):
                new_index = abs(current_index - len(the_houses) -1)
                the_houses[new_index] -= 2
                counter_houses += 1
                if the_houses[new_index] == 0:
                    print(f"Place {new_index} has Valentine's day.")
            else:
                the_houses[current_index] -= 2
                counter_houses += 1
                # if the_houses[current_index] == 0:
                #     print(f"Place {current_index} has Valentine's day.")

        command = input()

    print(f"Cupid's last position was {current_index}.")

    if sum(the_houses) == 0:
        return "Mission was successful."
    else:
        return f"Cupid has failed {len(the_houses) - counter_houses} places."

houses = input().split("@")
house = list(map(int, houses))

print(delivery_func(house))