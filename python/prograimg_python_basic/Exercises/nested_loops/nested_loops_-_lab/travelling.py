place = input()

while place != "End":
    needed_money = float(input())
    collected_money = 0
    while needed_money > collected_money:
        saving_money = float(input())
        collected_money += saving_money
    print(f"Going to {place}!")

    place = input()