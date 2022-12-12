change = float(input())

money = change * 100
count_of_coin = 0

while money > 0:
    if money >= 200:
        money -= 200
        count_of_coin += 1

    elif money >= 100:
        money -= 100
        count_of_coin += 1

    elif money >= 50:
        money -= 50
        count_of_coin += 1

    elif money >= 20:
        money -= 20
        count_of_coin += 1

    elif money >= 10:
        money -= 10
        count_of_coin += 1

    elif money >= 5:
        money -= 5
        count_of_coin +=1

    elif money >= 2:
        money -= 2
        count_of_coin += 1

    elif money >= 1:
        money -= 1
        count_of_coin += 1

    else:
        break

print(count_of_coin)