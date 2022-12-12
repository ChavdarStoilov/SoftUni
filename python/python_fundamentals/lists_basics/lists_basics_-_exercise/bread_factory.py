working_day_events = input().split("|")

coins = 100
energy = 100
bakery_closed = True

for event in working_day_events:
    event_and_value = event.split("-")

    the_event = event_and_value[0]
    the_value = int(event_and_value[1])

    if the_event == "rest":
        temporary_energy = energy
        energy += the_value
        if energy >= 100:
            energy = 100

        gained_energy = energy -temporary_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif the_event == "order":

        if energy >= 30:
            energy -= 30
            coins += the_value
            print(f"You earned {the_value} coins.")

        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= the_value:
            coins -= the_value
            print(f"You bought {the_event}.")
        else:
            print(f"Closed! Cannot afford {the_event}.")
            bakery_closed = False
            break

if bakery_closed:
    print("Day completed!\n"
          f"Coins: {coins}\n"
          f"Energy: {energy}")

