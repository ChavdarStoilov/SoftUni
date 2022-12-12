import math

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
price_gift = float(input())

price_magnolias = 3.25
price_hyacinths = 4
price_roses = 3.50
price_cactus = 8

sum =((price_magnolias * magnolias) + (price_hyacinths * hyacinths) + (price_roses * roses) + (price_cactus * cactus))
profit = sum - (sum * 0.05)

if profit >= price_gift:
    left_money = math.floor(profit - price_gift)
    print(f"She is left with {left_money} leva.")
else:
    need_more = math.ceil(price_gift - profit)
    print(f"She will have to borrow {need_more} leva.")
