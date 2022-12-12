command = str(input())

needed_coffee = 0
list_of_events = ["coding", "dog", "cat", "movie"]

while command != "END":
    events = command
    lower_events = events.lower()

    if lower_events not in list_of_events:
        command = str(input())
        continue
    else:
        if events == events.upper():
            needed_coffee += 2

        else:
            needed_coffee += 1


    command = str(input())

if needed_coffee <= 5:
    print(needed_coffee)
else:
    print("You need extra sleep")
