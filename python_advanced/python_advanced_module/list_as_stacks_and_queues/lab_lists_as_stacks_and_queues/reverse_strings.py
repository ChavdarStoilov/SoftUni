def reverse(string):

    stack = list(string)

    result = "".join([stack.pop() for _ in range (len(stack))])

    print(result)

some_string = input()
reverse(some_string)
