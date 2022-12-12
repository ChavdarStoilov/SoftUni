def pig(food, hay, cover, weight):
    food_grams = food * 1000
    hay_grams = hay * 1000
    cover_grams = cover * 1000
    weight_grams = weight * 1000

    for day in range(1, 31):
        food_grams -= 300
        if day % 2 == 0:
            hay_grams -= food_grams * 0.05
        if day % 3 == 0:
            cover_grams -= weight_grams // 3

        if food_grams <= 0 or hay_grams <= 0 or cover_grams <= 0:
            return "Merry must go to the pet store!"

    food_kilograms = food_grams / 1000
    hay_kilograms = hay_grams / 1000
    cover_kilograms = cover_grams / 1000

    return f"Everything is fine! Puppy is happy! Food: {food_kilograms:.2f}, Hay: {hay_kilograms:.2f}," \
           f" Cover: {cover_kilograms:.2f}."

quantity_food_in_kilograms = float(input())
quantity_hay_in_kilograms = float(input())
quantity_cover_in_kilograms = float(input())
weight_in_kilograms = float(input())

print(pig(quantity_food_in_kilograms, quantity_hay_in_kilograms, quantity_cover_in_kilograms, weight_in_kilograms))