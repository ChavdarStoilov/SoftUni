kilometers = int(input())
part_of_the_day = str(input())


if 20 <= kilometers < 100:
    price_bus = 0.09 * kilometers
    print("{:.2f}".format(price_bus))

elif kilometers >= 100:
    price_train = 0.06 * kilometers
    print("{:.2f}".format(price_train))

else:
    taxi_start_price = 0.70
    taxi_tariff = 0
    if part_of_the_day == "day":
        taxi_tariff = 0.79
    else:
        taxi_tariff = 0.90
    price_taxi = 0.70 + (taxi_tariff * kilometers)
    print("{:.2f}".format(price_taxi))
