type_fuel = str(input()).lower()
liter_fuel = float(input())


if type_fuel == "diesel":
    if liter_fuel >= 25:
        print(f"You have enough {type_fuel}.")

    else:
        print(f"Fill your tank with {type_fuel}!")

elif type_fuel == "gasoline":
    if liter_fuel >= 25:
        print(f"You have enough {type_fuel}.")

    else:
        print(f"Fill your tank with {type_fuel}!")


elif type_fuel == "gas":
    if liter_fuel >= 25:
        print(f"You have enough {type_fuel}.")

    else:
        print(f"Fill your tank with {type_fuel}!")

else:
    print("Invalid fuel!")