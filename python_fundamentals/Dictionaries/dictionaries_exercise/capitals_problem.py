country = input().split(", ")
city = input().split(", ")

capitals = {}

for the_country, the_city in zip(country, city):
    capitals[the_country] = the_city


for item, value in capitals.items():
    print(f"{item} -> {value}")
