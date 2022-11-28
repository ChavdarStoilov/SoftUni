some_raw_key = input()

command = input()

while command != "Generate":

    action = command.split(">>>")

    if action[0] == "Contains":
        if action[1] in some_raw_key:
            print(f"{some_raw_key} contains {action[1]}")
        else:
            print("Substring not found!")

    elif action[0] == "Flip":
        new_string = ""
        left_side = some_raw_key[:int(action[2])]
        middle_side = some_raw_key[int(action[2]):int(action[3])]
        right_side = some_raw_key[int(action[3]):]

        if action[1] == "Upper":
            some_raw_key = left_side + middle_side.upper() + right_side

        elif action[1] == "Lower":
            some_raw_key = left_side + middle_side.lower() + right_side

        print(some_raw_key)

    elif action[0] == "Slice":

        left_side = some_raw_key[:int(action[1])]
        right_side = some_raw_key[int(action[2]):]
        some_raw_key = left_side + right_side

        print(some_raw_key)

    command = input()

print(f"Your activation key is: {some_raw_key}")