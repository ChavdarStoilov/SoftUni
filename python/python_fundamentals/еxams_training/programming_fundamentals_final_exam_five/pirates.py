def events(cities, command):
    the_cities = cities

    while command != "End":
        action = command.split("=>")
        event = action[0]
        town = action[1]

        if event == "Plunder":
            the_cities[town]["population"] -= int(action[2])
            the_cities[town]["golds"] -= int(action[3])
            print(f"{town} plundered! {int(action[3])} gold stolen, {int(action[2])} citizens killed.")
            if the_cities[town]["population"] == 0 or the_cities[town]["golds"] == 0:
                print(f"{town} has been wiped off the map!")
                the_cities.pop(town)

        elif event == "Prosper":
            if int(action[2]) < 0:
                print("Gold added cannot be a negative number!")
                command = input()
                continue

            the_cities[town]["golds"] += int(action[2])
            print(f"{int(action[2])} gold added to the city treasury. {town} now has {the_cities[town]['golds']} gold.")

        command = input()

    if len(the_cities) == 0:

        print("Ahoy, Captain! All targets have been plundered and destroyed")

    else:

        print(f"Ahoy, Captain! There are {len(the_cities)} wealthy settlements to go to:")
        for all_city in the_cities.items():
            city = all_city[0]
            people = all_city[1]["population"]
            gold = all_city[1]["golds"]

            print(f"{city} -> Population: {people} citizens, Gold: {gold} kg")

def cities(city):

    the_cities = {}

    while city != "Sail":

        action = city.split("||")
        the_city = action[0]
        the_population = int(action[1])
        the_gold = int(action[2])

        if action[0] not in the_cities.keys():
            the_cities[the_city] = {"population": the_population, "golds": the_gold}
        else:
            the_cities[the_city]["population"] += the_population
            the_cities[the_city]["golds"] += the_gold

        city = input()

    event = input()
    events(the_cities, event)

first_command = input()
cities(first_command)