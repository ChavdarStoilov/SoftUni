from functools import wraps


def logged(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        name_of_func = func.__name__

        output = f'you called {name_of_func}{args}\nit returned {result}'

        return output

    return wrapper

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
