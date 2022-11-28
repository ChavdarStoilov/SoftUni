number_of_lines = int(input())

capacity_water_of_tank = 255
filled_water_in_tank = 0

for i in range(number_of_lines):
    liters = int(input())

    if liters > capacity_water_of_tank:
        print("Insufficient capacity!")

    if filled_water_in_tank + liters <= 255:
        filled_water_in_tank += liters
    else:
        print("Insufficient capacity!")




print(f"{filled_water_in_tank}")