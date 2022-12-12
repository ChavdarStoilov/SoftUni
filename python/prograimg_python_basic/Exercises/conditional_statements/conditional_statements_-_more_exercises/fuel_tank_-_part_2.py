type_fuel = str(input())
count_fuel = float(input())
club_card = str(input())


fuel_price = 0
discount = 0
end_sum = 0

if type_fuel == "Gasoline":
    fuel_price = 2.22

elif type_fuel == "Diesel":
    fuel_price = 2.33

elif type_fuel == "Gas":
    fuel_price = 0.93

if club_card == "Yes":
    if type_fuel == "Gasoline":
        discount = 0.18
    elif type_fuel == "Diesel":
        discount = 0.12
    else:
        discount = 0.08
elif club_card == "No":
    discount = 0

if 20 <= count_fuel <= 25:
    filled_fuel = (fuel_price - discount) * count_fuel
    discount_plus = filled_fuel * 0.08
    end_sum = filled_fuel - discount_plus

elif count_fuel > 25:
    filled_fuel = (fuel_price - discount) * count_fuel
    discount_plus = filled_fuel * 0.10
    end_sum = filled_fuel - discount_plus
else:
    end_sum = (fuel_price - discount) * count_fuel


print(f"{end_sum:.2f} lv.")
