number_of_cars = int(input())

the_parking = {"register": {}, "unregister": []}

for _ in range(number_of_cars):
    command = input().split()

    if command[0] == "register":
        if command[1] not in the_parking["register"].keys():
            the_parking["register"].update({command[1]: command[2]})
            print(f"{command[1]} registered {command[2]} successfully")
        else:
            license_plate_number = the_parking["register"][command[1]]
            print(f"ERROR: already registered with plate number {license_plate_number}")
    else:
        if command[1] not in the_parking["register"]:
            print(f"ERROR: user {command[1]} not found")
        else:
            print(f"{command[1]} unregistered successfully")
            the_parking["register"].pop(command[1])
            the_parking["unregister"].append(command[1])


for owner in the_parking["register"].items():
    print(f"{owner[0]} => {owner[1]}")