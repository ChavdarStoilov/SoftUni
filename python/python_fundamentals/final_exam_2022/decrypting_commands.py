some_string = input()

command = input()

while command != "Finish":
    action = command.split()

    if action[0] == "Replace":
        new_string = some_string.replace(action[1], action[2])
        some_string = new_string
        print(some_string)

    elif action[0] == "Cut":
        if 0 <= int(action[1]) < len(some_string) > int(action[2]) >= 0:
            start = int(action[1])
            end = start + int(action[2])

            some_string = "".join([some_string[idx] for idx in range(len(some_string)) if start > idx or idx >= end])
            print(some_string)
        else:
            print("Invalid indices!")

    elif action[0] == "Make":
        if action[1] == "Upper":
            some_string = some_string.upper()

        elif action[1] == "Lower":
            some_string = some_string.lower()
        print(some_string)

    elif action[0] == "Check":
        substring = action[1]
        if substring in some_string:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")

    elif action[0] == "Sum":
        sum = 0
        start = int(action[1])
        end = int(action[2])
        if 0 <= int(action[1]) < len(some_string) > int(action[2]) >= 0:
            for idx in range(start, end + 1):
                sum += ord(some_string[idx])

            print(sum)
        else:
            print("Invalid indices!")

    command = input()

