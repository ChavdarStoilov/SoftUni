from functools import wraps


def type_check(some_type):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            get_result = args[0]

            if type(get_result) == some_type:
                return func(*args, **kwargs)

            return 'Bad Type'

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
