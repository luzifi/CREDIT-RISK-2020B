import fire

from fintools.settings import get_logger
from fintools.utils import timeit


logger = get_logger(name=__name__)

class Main:

    def get_element(self, i: int, j: int):
        return 1 if (j == 0 or j >= i) else \
            self.get_element(i=i-1, j=j-1) + self.get_element(i=i-1, j=j)
    def _naive_implementation(self, level: int, index: int = 0):
        if index < level:
            row = [
                str(self.get_element(i=index, j=j))
                for j in range(index + 1)
            ]
            print(" ".join(row))
            self._naive_implementation(level=level, index=index+1)

    @timeit(logger=logger)
    def pascal_triangle(self, level: int, start: int = 0):
        self._naive_implementation(level=level, index=start)


if __name__ == "__main__":
    fire.Fire(Main)
