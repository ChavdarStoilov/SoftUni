budget = float(input())
season = str(input())

place_for_sleep = ""
place = ""
price = 0

if budget <= 1000:
    place_for_sleep = "Camp"
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.65
    else:
        place = "Morocco"
        price = budget * 0.45

elif 1000 < budget <= 3000:
    place_for_sleep = "Hut"
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.80
    else:
        place = "Morocco"
        price = budget * 0.60
else:
    place_for_sleep = "Hotel"
    price = budget * 0.90
    if season == "Summer":
        place = "Alaska"
    else:
        place = "Morocco"

print(f"{place} - {place_for_sleep} - {price:.2f}")