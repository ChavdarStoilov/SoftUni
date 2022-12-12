season = str(input())
type_group = str(input())
count_people = int(input())
count_night = int(input())

price = 0
discount = 0
sport = ""

if season == "Winter":
    if type_group == "boys":
        price = 9.60
        sport = "Judo"

    elif type_group == "girls":
        price = 9.60
        sport = "Gymnastics"

    else:
        price = 10
        sport = "Ski"


elif season == "Spring":
    if type_group == "boys":
        price = 7.20
        sport = "Tennis"

    elif type_group == "girls":
        price = 7.20
        sport = "Athletics"

    else:
        price = 9.50
        sport = "Cycling"

else:

    if type_group == "boys":
        price = 15
        sport = "Football"

    elif type_group == "girls":
        price = 15
        sport = "Volleyball"

    else:
        price = 20
        sport = "Swimming"

if 50 <= count_people:
    discount = 0.50

elif 20 <= count_people < 50:
    discount = 0.15

elif 10 <= count_people < 20:
    discount = 0.05

else:
    discount = 0


sum_for_night = count_people * price * count_night
end_sum = sum_for_night - (sum_for_night * discount)

print(f"{sport} {end_sum:.2f} lv.")