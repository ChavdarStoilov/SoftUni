budget = float(input())
type_ticket = str(input())
count_of_people = int(input())


need_money = 0

if type_ticket == "VIP":
    need_money += 499.99 * count_of_people
else:
    need_money += 249.99 * count_of_people

if 1 <= count_of_people <= 4:
    transport = budget * 0.75
    need_money += transport

elif 5 <= count_of_people <= 9:
    transport = budget * 0.60
    need_money += transport

elif 10 <= count_of_people <= 24:
    transport = budget * 0.50
    need_money += transport

elif 25 <= count_of_people <= 49:
    transport = budget * 0.40
    need_money += transport

else:
    transport = budget * 0.25
    need_money += transport

if need_money <= budget:
    left = budget - need_money
    print(f"Yes! You have {left:.2f} leva left.")

else:
    need_more = abs(need_money - budget)
    print(f"Not enough money! You need {need_more:.2f} leva.")