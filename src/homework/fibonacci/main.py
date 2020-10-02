from typing import List

from fintools.settings import get_logger

logger = get_logger(name=__name__)


class Main:

    def __init__(self):
        logger.info("Main object initialized.")

    def element(self, position: int) -> int:
        pass

    def sequence(self, length: int) -> List[int]:
        pass
