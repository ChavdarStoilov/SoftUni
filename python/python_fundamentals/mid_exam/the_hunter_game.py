def adventure(days, players, energy, water, food):

    total_water = days * players * water
    total_foot = days * players * food

    for day in range(1, days + 1):

        energy_loss = float(input())
        energy -= energy_loss

        if energy <= 0:
            break

        if day % 2 == 0:
            energy += energy * 0.05
            total_water -= total_water * 0.30

        if day % 3 == 0:
            total_foot -= total_foot / players
            energy += energy * 0.10


    if energy > 0:
        return f"You are ready for the quest. You will be left with - {energy:.2f} energy!"
    else:
        return f"You will run out of energy. You will be left with {total_foot:.2f} food and {total_water:.2f} water."

count_days = int(input())
count_of_player = int(input())
group_energy = float(input())
water_per_person = float(input())
food_per_person = float(input())


print(adventure(count_days, count_of_player, group_energy, water_per_person, food_per_person))
