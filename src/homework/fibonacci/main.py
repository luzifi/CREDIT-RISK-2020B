from typing import List

from fintools.settings import get_logger

logger = get_logger(name=__name__)


class Main:

    def __init__(self):
        logger.info("Main object initialized.")

    def element(self, i: int) -> int:
        return i if (i<2) else \
            self.element(i=i - 1) + self.element(i=i - 2)

    def sequence(self, j: int) -> List[int]:
        list=[self.element(j)]

