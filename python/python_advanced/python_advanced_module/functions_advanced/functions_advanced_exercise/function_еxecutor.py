def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = []

    for fun_ref, fun_params in args:
        fun_result = fun_ref(*fun_params)
        result.append(f'{fun_ref.__name__} - {fun_result}')

    return '\n'.join(result)


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
