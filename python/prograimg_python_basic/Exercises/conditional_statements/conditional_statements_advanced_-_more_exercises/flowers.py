chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = str(input())
work_or_holiday = str(input())

sum = 0

if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50
    sum = (chrysanthemums * chrysanthemums_price) + (roses_price * roses) + (tulips_price * tulips)

else:
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15
    sum = (chrysanthemums * chrysanthemums_price) + (roses_price * roses) + (tulips_price * tulips)

if work_or_holiday == "Y":
    sum += (sum * 0.15)
else:
    sum += 0

if season == "Spring" and tulips > 7:
    sum -= (sum * 0.05)
if season == "Winter" and roses >= 10:
    sum -= (sum * 0.10)
if (roses + chrysanthemums + tulips) > 20:
    sum -= (sum * 0.20)

end_sum = sum + 2
print(f"{end_sum:.2f}")
