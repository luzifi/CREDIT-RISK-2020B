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


def method_caching(func):
    simple_cache = {}

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        hashable_key = frozenset(args).union(frozenset(kwargs.items()))
        key = hash(hashable_key)
        if key in simple_cache:
            return simple_cache[key]
        simple_cache[key] = func(self, *args, **kwargs)
        return wrapper(self, *args, **kwargs)
    return wrapper
