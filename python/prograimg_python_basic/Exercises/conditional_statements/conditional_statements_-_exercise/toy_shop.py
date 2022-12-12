puzzle = 2.60
speak = 3
bear = 4.10
minion = 8.20
truck = 2

excursion = float(input())
num_puzzle = int(input())
num_speak = int(input())
num_bear = int(input())
num_minion = int(input())
num_truck = int(input())
discount = 0

num = num_bear + num_truck + num_speak + num_minion + num_puzzle
price_before = (num_bear * bear) + (num_truck * truck) + (num_speak * speak) + (num_minion * minion) + (num_puzzle * puzzle)

if num >= 50:
    discount = price_before * 0.25

price = price_before - discount
rent = price * 0.10

win = price - rent

if win >= excursion:
    left_sum = win - excursion
    print("Yes! " + "{:.2f}".format(left_sum) + " lv left.")
else:
    left_sum = excursion - win
    print("Not enough money! " + "{:.2f}".format(left_sum) + " lv needed.")