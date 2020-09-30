import functools
from typing import Callable, List, Optional


def corner_case_decorator(func):
    @functools.wraps(func)
    def wrapper(self, i, j, *args, **kwargs):
        if j == 0 or j >= i:
            return 1
        return func(self, i, j, *args, **kwargs)
    return wrapper


def lazy_wrapper(value):
    return lambda: value


class TriangleBuilder:
    CACHE = {}

    def save(self, i: int, j: int, value: int):
        self.CACHE[(i, j)] = lazy_wrapper(value)
        return value

    @corner_case_decorator
    def get(self, i: int, j: int, default: Callable[[], Optional[int]] = lazy_wrapper(None)):
        key = (i, j)
        return self.CACHE.get(key, default)()

    @corner_case_decorator
    def create(self, i: int, j: int):
        upper_left = self.get_or_create(i=i-1, j=j-1)
        upper_center = self.get_or_create(i=i-1, j=j)
        return self.save(i=i, j=j, value=upper_left+upper_center)

    def get_or_create(self, i: int, j: int):
        return self.get(i, j, default=lambda: self.create(i=i, j=j))

    def get_row(self, index: int) -> List[str]:
        return [
            str(self.get_or_create(i=index, j=j))
            for j in range(index + 1)
        ]
