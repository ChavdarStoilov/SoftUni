loses_game = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())


helmets_broken = loses_game // 2
sword_broken = loses_game // 3
shield_broken = loses_game // 6
armor_broken = shield_broken // 2

expenses = helmets_broken * helmet_price + \
    sword_broken * sword_price + \
    shield_broken * shield_price + \
    armor_broken * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
