budget = int(input())
session = str(input())
count_fisher = int(input())

price = 0
discount = 0
discount_plus = 1
sum = 0

if count_fisher <= 6:
    discount = 0.10
    if session == "Spring":
        price = 3000
        if count_fisher % 2 ==0:
            discount_plus = 0.05

    elif session == "Summer":
        price = 4200
        if count_fisher % 2 ==0:
            discount_plus = 0.05

    elif session == "Autumn":
        price = 4200

    elif session == "Winter":
        price = 2600
        if count_fisher % 2 ==0:
            discount_plus = 0.05


elif 7 <= count_fisher <= 11:
    discount = 0.15
    if session == "Spring":
        price = 3000
        if count_fisher % 2 ==0:
            discount_plus = 0.05

    elif session == "Summer":
        price = 4200
        if count_fisher % 2 ==0:
            discount_plus = 0.05

    elif session == "Autumn":
        price = 4200

    elif session == "Winter":
        price = 2600
        if count_fisher % 2 ==0:
            discount_plus = 0.05

elif count_fisher >= 12:
    discount = 0.25
    if session == "Spring":
        price = 3000
        if count_fisher % 2 ==0:
            discount_plus = 0.05

    elif session == "Summer":
        price = 4200
        if count_fisher % 2 ==0:
            discount_plus = 0.05

    elif session == "Autumn":
        price = 4200

    elif session == "Winter":
        price = 2600
        if count_fisher % 2 ==0:
            discount_plus = 0.05

if discount_plus == 1:
    sum = price - (price * discount)

else:
    dis = price - (price * discount)
    sum = dis - (dis * discount_plus)

if budget >= sum:
    left = budget - sum
    print("Yes! You have " + "{:.2f}".format(left) + " leva left.")

elif budget < sum:
    need_more = sum - budget
    print("Not enough money! You need " + "{:.2f}".format(need_more) + " leva.")