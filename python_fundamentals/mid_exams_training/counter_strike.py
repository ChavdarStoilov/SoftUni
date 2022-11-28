def kill_enemy(energy):
    command = input()
    count_wins = 0
    while command != "End of battle":
        distance = int(command)

        if distance <= energy:
            energy -= distance
            count_wins += 1

            if count_wins % 3 == 0:
                energy += count_wins

        else:
            return f"Not enough energy! Game ends with {count_wins} won battles and {energy} energy"

        command = input()


    return f"Won battles: {count_wins}. Energy left: {energy}"


start_energy = int(input())

print(kill_enemy(start_energy))