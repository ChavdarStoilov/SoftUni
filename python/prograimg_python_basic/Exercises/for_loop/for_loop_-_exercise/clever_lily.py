years_old = int(input())
price_of_laundry = float(input())
price_of_toy = int(input())

sum_of_birthday = 0
brother_taken_money = 0
sold_toys = 0

for years in range(1, years_old + 1):
    if years % 2 == 0:
        sum_of_birthday += (10 * years) // 2
        brother_taken_money += 1
    else:
        sold_toys += 1


sum = (sum_of_birthday + (sold_toys * price_of_toy) - brother_taken_money)

if sum >= price_of_laundry:
    left = sum - price_of_laundry
    print(f"Yes! {left:.2f}")

else:
    need_more = price_of_laundry - sum
    print(f"No! {need_more:.2f}")