some_date = input().split()
command = input().split()

left_side = []
right_side = []

while command[0] != "end":
    manipulation = command

    if manipulation[0] == "exchange":
        the_exchange = int(manipulation[1])
        if the_exchange > len(some_date):
            print("Invalid index")
        elif the_exchange < 0:
            print("Invalid index")
        else:
            left_side = some_date[:the_exchange +1]
            right_side = some_date[the_exchange +1:]
            some_date = right_side + left_side

    elif manipulation[0] == "max" and manipulation[1] == "even":
        max_even = [max(num) for num in some_date if int(num) % 2 == 0]
        if len(max_even) == 0:
            print("No matches")
        else:
            print(some_date.index(max(max_even)))

    elif manipulation[0] == "max" and manipulation[1] == "odd":
        max_odd = [max(num) for num in some_date if int(num) % 2 != 0]
        print(max_odd)
        if len(max_odd) == 0:
            print("No matches")
        else:
            print(some_date.index(max(max_odd)))

    elif manipulation[0] == "min" and manipulation[1] == "even":
        min_even = [min(num) for num in some_date if int(num) % 2 == 0]
        if len(min_even) == 0:
            print("No matches")
        else:
            print(some_date.index(min(min_even)))

    elif manipulation[0] == "min" and manipulation[1] == "odd":
        min_odd = [min(num) for num in some_date if int(num) % 2 != 0]
        if len(min_odd) == 0:
            print("No matches")
        else:
            print(some_date.index(min(min_odd)))

    elif manipulation[0] == "first" and manipulation[2] == "odd":
        first_odd = []
        count = int(manipulation[1])

        for numb in some_date:
            if int(numb) % 2 != 0:
                first_odd.append(int(numb))

        if count > len(some_date):
            print("Invalid count")
        else:
            print(first_odd[:count])

    elif manipulation[0] == "first" and manipulation[2] == "even":
        first_even = []
        count = int(manipulation[1])

        for numb in some_date:
            if int(numb) % 2 == 0:
                first_even.append(int(numb))

        if count > len(some_date):
            print("Invalid count")
        else:
            print(first_even[:count])

    elif manipulation[0] == "last" and manipulation[2] == "even":
        last_even = []
        count = int(manipulation[1])
        for numb in some_date:
            if int(numb) % 2 == 0:
                last_even.append(int(numb))

        if count > len(some_date):
            print("Invalid count")
        else:
            print(last_even[:count])

    elif manipulation[0] == "last" and manipulation[2] == "odd":
        last_odd = []
        count = int(manipulation[1])

        for numb in some_date:
            if int(numb) % 2 != 0:
                last_odd.append(int(numb))

        if count > len(some_date):
            print("Invalid count")
        else:
            print(last_odd[:count])

    command = input().split()


print(list(map(int, some_date)))