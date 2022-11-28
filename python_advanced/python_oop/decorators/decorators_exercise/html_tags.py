from functools import wraps


def tags(type_tag):

    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            result = [func(*args)]
            result.insert(0, f'<{type_tag}>')
            result.append(f'</{type_tag}>')

            return ''.join(result)

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
