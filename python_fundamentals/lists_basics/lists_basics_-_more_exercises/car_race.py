the_race = input().split()

first_car_time = 0
second_car_time = 0

finish = len(the_race) // 2
left_car = the_race[:finish]
right_car = the_race[finish + 1::]
right_car.reverse()

for first_car in left_car:
    if int(first_car) == 0:
        first_car_time *= 0.80
    else:
        first_car_time += int(first_car)

for second_car in right_car:
    if int(second_car) == 0:
        second_car_time *= 0.80
    else:
        second_car_time += int(second_car)


if first_car_time < second_car_time:
    print(f"The winner is left with total time: {first_car_time:.1f}")
elif first_car_time > second_car_time:
    print(f"The winner is right with total time: {second_car_time:.1f}")