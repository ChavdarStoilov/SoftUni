password = input()
command = input()

while command != "Done":
    action = command.split()

    if action[0] == "TakeOdd":
        password = "".join([password[idx] for idx in range(len(password)) if idx % 2 != 0])
        print(password)


    elif action[0] == "Cut":
        start = int(action[1])
        finish = start + int(action[2])

        password = "".join([password[idx] for idx in range(len(password)) if start > idx or idx >= finish])
        print(password)

    elif action[0] == "Substitute":
        old = action[1]
        new = action[2]

        if old in password:
            password = password.replace(old, new)
            print(password)

        else:
            print("Nothing to replace!")


    command = input()

print(f"Your password is: {password}")