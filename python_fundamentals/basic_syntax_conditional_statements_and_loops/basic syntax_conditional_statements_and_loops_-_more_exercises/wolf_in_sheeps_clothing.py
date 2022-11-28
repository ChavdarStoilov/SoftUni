animals = input().split(", ")
animals.reverse()

for animal in range(len(animals)):
    if animals[0] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif animals[animal] == "wolf":
        count_sheep = animals.count("sheep")
        print(f"Oi! Sheep number {animal}! You are about to be eaten by a wolf!")

