money = float(input())
years = int(input())

sum = 0

for year in range(1800, years + 1):
    if year % 2 == 0:
        sum += 12000
    else:
        current_years = ((year - 1800) + 18) * 50
        sum += 12000 + current_years


if money >= sum:
    left = money - sum
    print(f"Yes! He will live a carefree life and will have {left:.2f} dollars left.")
else:
    need_more = sum - money
    print(f"He will need {need_more:.2f} dollars to survive.")