from functools import wraps


def even_parameters(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        count_of_numbers = len(args)

        is_even = True if len([n for n in args if not isinstance(n, str) and n % 2 == 0]) == count_of_numbers else False

        if is_even:
            return func(*args)

        return 'Please use only even numbers!'

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))


