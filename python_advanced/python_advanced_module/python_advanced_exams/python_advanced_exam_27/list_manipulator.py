def list_manipulator(numbers, case, action, *args):
    list_num = list(args)

    if case == 'add':
        if action == 'beginning':
            while list_num:
                numbers.insert(0, list_num.pop())

        elif action == 'end':
            for num in list_num:
                numbers.append(num)

    elif case == 'remove':
        if action == 'beginning':
            if len(list_num) == 0:
                numbers.pop(0)
            else:
                for _ in range(list_num[0]):
                    numbers.pop(0)

        elif action == 'end':
            if len(list_num) == 0:
                numbers.pop()
            else:
                for _ in range(list_num[0]):
                    numbers.pop()

    return numbers

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

