from functools import wraps


def cache(func):
    cached = {}

    @wraps(func)
    def wrapper(num):
        result = func(num)

        if num not in cached:
            cached[num] = result

        return result

    wrapper.log = cached
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
fibonacci(4)
print(fibonacci.log)
