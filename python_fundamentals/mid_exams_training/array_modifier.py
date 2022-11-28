def modifier(indexes):

    the_command = input()

    while the_command != "end":
        command = the_command.split()

        if command[0] == "swap":
            indexes[int(command[1])], indexes[int(command[2])] = indexes[int(command[2])], indexes[int(command[1])]
        elif command[0] == "multiply":
            indexes[int(command[1])] = indexes[int(command[1])] * indexes[int(command[2])]
        elif command[0] == "decrease":
            for number in range(len(indexes)):
                indexes[number] -= 1
        the_command = input()


    return ", ".join(str(idx) for idx in indexes)

index_list = input().split()
index_int_list = list(map(int, index_list))
print(modifier(index_int_list))
