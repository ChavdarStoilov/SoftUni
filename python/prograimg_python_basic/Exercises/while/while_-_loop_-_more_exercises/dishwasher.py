count_bottles = int(input())
dishes = input()

available_preparation = 750 * count_bottles
count = 0
count_dishes = 0
count_pots = 0

while dishes != "End":
    dishess = int(dishes)
    count += 1

    if count % 3 == 0:
        count_pots += dishess
        available_preparation -= (15 * dishess)
    else:
        count_dishes += dishess
        available_preparation -= (5 * dishess)

    if available_preparation < 0:
        break

    dishes = input()

if available_preparation < 0:
    print(f"Not enough detergent, {abs(available_preparation)} ml. more necessary!")
else:
    print(f"Detergent was enough!\n"
          f"{count_dishes} dishes and {count_pots} pots were washed.\n"
          f"Leftover detergent {available_preparation} ml.")