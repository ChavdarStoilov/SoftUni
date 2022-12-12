count_plant = int(input())

the_plants = {}

for _ in range(count_plant):
    plant, rarity = input().split("<->")
    if plant not in the_plants:
        the_plants[plant] = {"rarity": 0, "rate": []}
    the_plants[plant]["rarity"] += int(rarity)

command = input()

while command != "Exhibition":
    action = command.split(": ")
    plant_rate= action[1].split(" - ")
    plants = plant_rate[0]

    if plants not in the_plants.keys():
        print("error")
    elif action[0] == "Rate":
        the_plants[plant_rate[0]]["rate"].append(float(plant_rate[1]))
    elif action[0] == "Update":
        the_plants[plant_rate[0]]["rarity"] = int(plant_rate[1])
    elif action[0] == "Reset":
        the_plants[plant_rate[0]]["rate"] = [0]
    command = input()

print("Plants for the exhibition:")
for the_plant in the_plants.items():
    the_rarity = the_plant[1]["rarity"]
    the_rate = sum(the_plant[1]["rate"]) / len(the_plant[1]["rate"])
    print(f"- {the_plant[0]}; Rarity: {the_rarity}; Rating: {the_rate:.2f}")
