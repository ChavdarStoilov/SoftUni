price = float(input())
statists = int(input())
price2 = float(input())
discount = 0
decor = price * 0.10

if statists > 150:
    discount = price2 * 0.10
    price2 = (price2 - discount) * statists

else:
    price2 = (price2 * statists)

end_sum = decor + price2

if end_sum > price:
    money = end_sum - price
    print("Not enough money!")
    print("Wingard needs " + "{:.2f}".format(money) + " leva more.")

elif end_sum <= price:
    money = price - end_sum
    print("Action!")
    print("Wingard starts filming with " + "{:.2f}".format(money) + " leva left.")
