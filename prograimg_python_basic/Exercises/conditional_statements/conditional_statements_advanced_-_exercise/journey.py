budget = float(input())
session = str(input())

country = ""
spent = 0
place = ""

if budget <= 100:
    country = "Bulgaria"
    if session == "summer":
        spent = 0.30
        place = "Camp"
    elif session == "winter":
        spent = 0.70
        place = "Hotel"

elif budget <= 1000:
    country = "Balkans"
    if session == "summer":
        spent = 0.40
        place = "Camp"
    elif session == "winter":
        spent = 0.80
        place = "Hotel"

else:
    country = "Europe"
    spent = 0.90
    place = "Hotel"

spent_money = budget * spent

print(f"Somewhere in {country}")
print(f"{place} - {spent_money:.2f}")
