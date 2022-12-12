def maintenance(the_list):

    command = input()

    black_list_names = 0
    lost_name = 0

    while command != "Report":

        commands = command.split()

        if commands[0] == "Blacklist":
            if commands[1] not in the_list:
                print(f"{commands[1]} was not found.")
            else:
                index = the_list.index(commands[1])
                the_list[int(index)] = "Blacklisted"
                print(f"{commands[1]} was blacklisted.")
                black_list_names += 1

        elif commands[0] == "Error":
            if 0 <= int(commands[1]) < len(the_list) and the_list[int(commands[1])] != "Blacklisted" and the_list[int(commands[1])] != "Lost":
                print(f"{the_list[int(commands[1])]} was lost due to an error.")
                the_list[int(commands[1])] = "Lost"
                lost_name += 1

        elif commands[0] == "Change":
            if 0 <= int(commands[1]) < len(the_list):
                print(f"{the_list[int(commands[1])]} changed his username to {commands[2]}.")
                the_list[int(commands[1])] = commands[2]

        command = input()

    return f"Blacklisted names: {black_list_names}\n"\
           f"Lost names: {lost_name}\n" \
           f"{' '.join(the_list)}"

some_friend_list = input().split(", ")


print(maintenance(some_friend_list))