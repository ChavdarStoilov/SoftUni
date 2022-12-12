def parentheses(string):

    stack = []

    for idx in range(len(string)):
        char = string[idx]

        if char == '(':
            stack.append(idx)

        elif char == ')':
            start = stack.pop()
            print(string[start:idx + 1])


some_text = input()
parentheses(some_text)