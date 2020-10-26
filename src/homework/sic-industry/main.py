import os
import json
from typing import Dict

from fintools.settings import get_logger
from fintools.utils import StringWrapper, timeit

from .settings import (
    INDUSTRY_SEARCH_DEFAULT_FILENAME,
    INDUSTRY_SEARCH_DEFAULT_THRESHOLD
)

logger = get_logger(name=__name__)
sw = StringWrapper


class Main:
    threshold = INDUSTRY_SEARCH_DEFAULT_THRESHOLD

    @timeit(logger=logger)
    def search(self, title: str, exact: bool = False, file: str = INDUSTRY_SEARCH_DEFAULT_FILENAME) -> str:
        sw.contains(self, pattern=title)
        with open(file, 'r') as f:
            content = f.read()
            se = sw.boolean_search(self, pattern=title, exact=exact,
                                   threshold=INDUSTRY_SEARCH_DEFAULT_THRESHOLD)
            return se
