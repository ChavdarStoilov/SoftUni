def operate(operator, *args):

    def add(numbers):
        result = 0
        for num in args:
            result += num
        return result

    def subtract(numbers):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    def divide(numbers):
        result = args[0]
        for num in args[1:]:
            result /= num
        return result

    def multiply(numbers):
        result = 1
        for num in args:
            result *= num

        return result

    if operator == '+':
        return add(args)

    elif operator == '*':
        return multiply(args)

    elif operator == '/':
        return divide(args)

    elif operator == '-':
        return subtract(args)


print(operate("+", 2, 2))
print(operate("*", 2, 2))
print(operate("-", 4, 2))
print(operate("/", 4, 2))