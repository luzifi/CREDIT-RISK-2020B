import fire

from fintools.settings import get_logger
from fintools.utils import timeit, method_caching

from .utils import TriangleBuilder

logger = get_logger(name=__name__)


class Main:
    builder = TriangleBuilder()

    @method_caching
    def get_element(self, i: int, j: int):
        return 1 if (j == 0 or j >= i) else \
            self.get_element(i=i-1, j=j-1) + self.get_element(i=i-1, j=j)

    def _default_implementation(self, level: int, index: int = 0):
        if index < level:
            row = [
                str(self.get_element(i=index, j=j))
                for j in range(index + 1)
            ]
            print(" ".join(row))
            self._default_implementation(level=level, index=index+1)

    def _oop_implementation(self, level: int, index: int = 0):
        if index < level:
            row = self.builder.get_row(index=index)
            print(" ".join(row))
            self._oop_implementation(level=level, index=index+1)

    @timeit(logger=logger)
    def pascal_triangle(self, level: int, implementation: str = "default", start: int = 0):
        if implementation.lower().startswith("oop"):
            return self._oop_implementation(level=level, index=start)
        return self._default_implementation(level=level, index=start)


if __name__ == "__main__":
    fire.Fire(Main)
