def stacked(action, the_stack_query):

    if action[0] == '1':
        the_stack_query.append(action[1])

    elif action[0] == '2':
        if the_stack_query:
            the_stack_query.pop()

    elif action[0] == '3':
        if the_stack_query:
            print(max(the_stack_query))

    elif action[0] == '4':
        if the_stack_query:
            print(min(the_stack_query))



count_of_lines = int(input())
the_stack_query = []

for _ in range(count_of_lines):
    command = input().split()
    stacked(command, the_stack_query)

print(", ".join([the_stack_query.pop() for _ in range(len(the_stack_query))]))