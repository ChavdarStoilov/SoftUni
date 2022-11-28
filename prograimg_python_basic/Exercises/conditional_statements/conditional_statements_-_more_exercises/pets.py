import math

days = int(input())
food = int(input())
food_for_dog_in_kilograms_per_day = float(input())
food_for_cat_in_kilograms_per_day = float(input())
food_for_turtle_in_grams_per_day = float(input()) / 1000


need_food = (food_for_dog_in_kilograms_per_day + food_for_cat_in_kilograms_per_day + food_for_turtle_in_grams_per_day) * days

if food >= need_food:
    left_food_kilograms = math.floor(food - need_food)
    print(f"{left_food_kilograms} kilos of food left.")

else:
    need_more_food = math.ceil(need_food - food)
    print(f"{need_more_food} more kilos of food are needed.")
