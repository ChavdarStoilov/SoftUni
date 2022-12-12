fruit = str(input())
day_of_week = str(input())
count = float(input())

price = 0

if fruit == "banana":
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
        price = 2.50
        print("{:.2f}".format(price * count))
    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        price = 2.70
        print("{:.2f}".format(price * count))
    else:
        print("error")

elif fruit == "apple":
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
        price = 1.20
        print("{:.2f}".format(price * count))
    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        price = 1.25
        print("{:.2f}".format(price * count))
    else:
        print("error")

elif fruit == "orange":
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
        price = 0.85
        print("{:.2f}".format(price * count))
    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        price = 0.90
        print("{:.2f}".format(price * count))
    else:
        print("error")

elif fruit == "grapefruit":
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
        price = 1.45
        print("{:.2f}".format(price * count))
    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        price = 1.60
        print("{:.2f}".format(price * count))
    else:
        print("error")

elif fruit == "kiwi":
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
        price = 2.70
        print("{:.2f}".format(price * count))
    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        price = 3.00
        print("{:.2f}".format(price * count))
    else:
        print("error")

elif fruit == "pineapple":
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
        price = 5.50
        print("{:.2f}".format(price * count))
    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        price = 5.60
        print("{:.2f}".format(price * count))
    else:
        print("error")

elif fruit == "grapes":
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
        price = 3.85
        print("{:.2f}".format(price * count))
    elif day_of_week == "Saturday" or day_of_week == "Sunday":
        price = 4.20
        print("{:.2f}".format(price * count))
    else:
        print("error")
else:
    print("error")