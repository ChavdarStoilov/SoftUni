season = str(input())
kilometers_per_months = float(input())

price_per_kilometers = 0

if kilometers_per_months <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_kilometers = 0.75
    elif season == "Summer":
        price_per_kilometers = 0.90
    else:
        price_per_kilometers = 1.05

elif 5000 < kilometers_per_months <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_kilometers = 0.95
    elif season == "Summer":
        price_per_kilometers = 1.10
    else:
        price_per_kilometers = 1.25

else:
    price_per_kilometers = 1.45


sum = (price_per_kilometers * kilometers_per_months) * 4
end_sum = sum - (sum * 0.10)
print(f"{end_sum:.2f}")