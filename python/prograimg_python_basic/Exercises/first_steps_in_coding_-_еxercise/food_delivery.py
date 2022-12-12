delivery = 2.50
dessert_percentage = 20 / 100

chicken_menu = int(input()) * 10.35
fish_menu = int(input()) * 12.40
vegan_menu = int(input()) * 8.15

order = (chicken_menu + fish_menu + vegan_menu) * dessert_percentage
dessert = order

end_sum = chicken_menu + fish_menu + vegan_menu + dessert + delivery
print(end_sum)