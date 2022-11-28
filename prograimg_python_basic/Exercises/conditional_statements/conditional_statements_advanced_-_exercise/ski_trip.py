days = int(input()) -1
type_room = str(input())
rating = str(input())


price = 0
discount = 0


if days < 10:
    if type_room == "apartment":
        discount = 0.30
        price =25.00
    elif type_room == "president apartment":
        discount = 0.10
        price = 35.00
    else:
        discount = 0
        price = 18.00

elif 10 < days < 15:
    if type_room == "apartment":
        discount = 0.35
        price = 25.00
    elif type_room == "president apartment":
        discount = 0.15
        price = 35.00
    else:
        discount = 0
        price = 18.00

else:
    if type_room == "apartment":
        discount = 0.50
        price = 25.00
    elif type_room == "president apartment":
        discount = 0.20
        price = 35.00
    else:
        discount = 0
        price = 18.00

sum = (days * price) - ((days * price) * discount)

if rating == "positive":
    endsum = (sum + (sum * 0.25))
else:
    endsum = (sum - (sum * 0.10))

print("{:.2f}".format(endsum))