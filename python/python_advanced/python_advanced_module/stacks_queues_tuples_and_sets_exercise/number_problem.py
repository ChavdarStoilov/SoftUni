first_sequences = input().split()
second_sequences = input().split()

numbs_of_commands = int(input())

first_set = {int(num) for num in first_sequences}
second_set = {int(num) for num in second_sequences}


for _ in range(numbs_of_commands):

    numers = []
    command = input().split()

    for i in command:
        if len(i) < 3:
            numers.append(int(i))

    if command[0] == 'Add':
        if command[1] == 'First':
            for num in numers:
                first_set.add(int(num))
        else:
            for num in numers:
                second_set.add(int(num))

    elif command[0] == 'Remove':
        if command[1] == "First":
            for num in numers:
                if num in first_set:
                    first_set.remove(int(num))
        else:
            for num in numers:
                if num in second_set:
                    second_set.remove(int(num))

    elif command[0] == 'Check':
        checker = second_set.issubset(first_set)
        print(checker)


print(', '.join(str(end) for end in sorted(first_set)))
print(', '.join(str(end) for end in sorted(second_set)))