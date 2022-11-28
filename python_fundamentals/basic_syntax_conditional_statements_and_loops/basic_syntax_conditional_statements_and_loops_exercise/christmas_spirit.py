quantity_of_decorations = int(input())
left_days_until_christmas = int(input())

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

needed_budget = 0
total_spirit = 0

for day in range(1, left_days_until_christmas + 1):

    if day % 11 == 0:
        quantity_of_decorations += 2

    if day % 2 == 0:
        needed_budget += ornament_set * quantity_of_decorations
        total_spirit += 5

    if day % 3 == 0:
        needed_budget += tree_skirt * quantity_of_decorations
        needed_budget += tree_garland * quantity_of_decorations
        total_spirit += 13 # 3 points from tree skirt and 10 points from tree garland

    if day % 5 == 0:
        needed_budget += tree_lights * quantity_of_decorations
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30


    if day % 10 == 0:
        total_spirit -= 20
        needed_budget += tree_skirt
        needed_budget += tree_garland
        needed_budget += tree_lights
        if left_days_until_christmas == day:
            total_spirit -= 30

print(f"Total cost: {needed_budget}")
print(f"Total spirit: {total_spirit}")





