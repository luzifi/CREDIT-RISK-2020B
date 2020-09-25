import functools
import time


def timeit(logger):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            out = func(*args, **kwargs)
            logger.warning("Execution time %s" % (time.time() - start))
            return out
        return wrapper
    return decorator
