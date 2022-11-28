import time
from functools import wraps


def exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args)
        end_time = time.time()

        taken_time = end_time - start_time
        return taken_time
    return wrapper



@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())


