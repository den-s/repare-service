import time
from .settings import DEBUG


def time_logger(func):
    def func_wrapper(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        if DEBUG:
            print(
                # f"{func.__qualname__} [{round(te - ts, 3)} sec] (args: {args}, kwargs: {kwargs})"
                f"{func.__qualname__} [{round(te - ts, 3)} sec]"
            )
        return result

    return func_wrapper
