money_for_vacation = float(input())
available_money = float(input())

days = 0
spend_days = 0

while money_for_vacation > available_money and spend_days < 5:
    type_action_with_money = str(input())
    money = float(input())
    days += 1

    if type_action_with_money == "spend":

        if available_money - money < 0:
            available_money = 0
        else:
            available_money -= money
        spend_days += 1

    else:
        available_money += money
        spend_days = 0


if spend_days == 5:
    print("You can't save the money.\n"
          f"{days}")
if available_money >= money_for_vacation:
    print(f"You saved the money for {days} days.")
