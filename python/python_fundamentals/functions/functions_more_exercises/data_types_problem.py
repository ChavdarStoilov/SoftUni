def data_types(command, command_two):
    if command == "int":
        return int(command_two) * 2
    elif command == "real":
        return f"{float(command_two) * 1.5:.2f}"
    elif command == "string":
        return f"${command_two}$"


first_command = input()
second_command = input()

print(data_types(first_command, second_command))

