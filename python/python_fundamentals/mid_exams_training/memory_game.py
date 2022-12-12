def memory(number):
    some_move = input()
    founded_counter = 0

    while some_move != "end":
        move = some_move.split()
        founded_counter += 1
        first_index = int(move[0])
        second_index = int(move[1])

        if 0 > first_index or first_index > len(number) - 1 or 0 > second_index or second_index > len(number) - 1 or first_index == second_index:
            middle = len(number) // 2
            number.insert(int(middle), f"-{founded_counter}a")
            number.insert(int(middle), f"-{founded_counter}a")
            print("Invalid input! Adding additional elements to the board")


        elif number[first_index] == number[second_index]:
            founded = number[first_index]
            print(f"Congrats! You have found matching elements - {number[first_index]}!")
            number.remove(founded)
            number.remove(founded)

        elif number[first_index] != number[second_index]:
            print("Try again!")

        some_move = input()

        if len(number) == 0:
            return f"You have won in {founded_counter} turns!"

    return f"Sorry you lose :(\n" \
           f"{' '.join(number)}"


some_numbers = input().split()
print(memory(some_numbers))
