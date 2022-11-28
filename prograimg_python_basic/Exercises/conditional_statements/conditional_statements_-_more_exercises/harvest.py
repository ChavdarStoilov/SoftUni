import math

square_meter_grapes = int(input())
grapes_for_one_square_meter = float(input())
needed_liters_for_wine = int(input())
count_worker = int(input())

grapes = square_meter_grapes * grapes_for_one_square_meter
take_grapes_for_wine = grapes * 0.40

liter_wine = take_grapes_for_wine / 2.5

if liter_wine < needed_liters_for_wine:
    more_liter_wine = math.floor(needed_liters_for_wine - liter_wine)
    print(f"It will be a tough winter! More {more_liter_wine} liters wine needed.")
else:
    left_liter_wine = liter_wine - needed_liters_for_wine
    liter_wine_per_worker = left_liter_wine / count_worker
    print(f"Good harvest this year! Total wine: {math.ceil(liter_wine)} liters.")
    print(f"{math.ceil(left_liter_wine)} liters left -> {math.ceil(liter_wine_per_worker)} liters per person.")
