count_of_trainers = int(input())
points = float(input())
season = str(input())
place = str(input())

money_for_winner = 0

if place == "Bulgaria":
    money = count_of_trainers * points
    if season == "summer":
        money_for_winner = money - (money * 0.05)
    else:
        money_for_winner = money - (money * 0.08)
else:
    money = count_of_trainers * points
    test = money + (money * 0.50)
    if season == "summer":
        money_for_winner = test - (test * 0.10)
    else:
        money_for_winner = test - (test * 0.15)

sos_money = money_for_winner * 0.75
money_for_trainer =( (money_for_winner - sos_money) / count_of_trainers)


print(f"Charity - {sos_money:.2f}\n"
      f"Money per dancer - {money_for_trainer:.2f}")