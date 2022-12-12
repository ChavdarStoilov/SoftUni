the_level_of_fire = input().split("#")
amount_of_water = int(input())

effort = 0
total_fire = 0

fire_finished = []

for word in the_level_of_fire:
    current_value = "".join(word)
    fire = current_value.split("=")

    type_of_fire = fire[0]
    fire_level = int(fire[1])

    if amount_of_water < fire_level:
        continue

    if type_of_fire == "High ":
        if 81 <= fire_level <= 125:
            amount_of_water -= fire_level
            effort += fire_level * 0.25
            total_fire += fire_level
            fire_finished.append(fire_level)
    elif type_of_fire == "Medium ":
        if 51 <= fire_level <= 80:
            amount_of_water -= fire_level
            effort += fire_level * 0.25
            total_fire += fire_level
            fire_finished.append(fire_level)
    elif type_of_fire == "Low ":
        if 1 <= fire_level <= 50:
            amount_of_water -= fire_level
            effort += fire_level * 0.25
            total_fire += fire_level
            fire_finished.append(fire_level)


print("Cells:")

for index in fire_finished:
    print(f" - {index}")


print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")