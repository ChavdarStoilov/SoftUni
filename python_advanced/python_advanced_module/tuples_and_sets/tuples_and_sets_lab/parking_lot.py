number_of_cars = int(input())

parking = set()

for _ in range(number_of_cars):

    action, plate = input().split(', ')
    if action == 'IN':
        parking.add(plate)
    elif action == "OUT":
        parking.remove(plate)

if parking:
    print('\n'.join(parking))
else:
    print('Parking Lot is Empty')