import json
from fintools.settings import get_logger
from typing import Dict
from .utils import FLT

logger = get_logger(name="__main__")


class Main:

    @staticmethod
    def show(file: str) -> str:
        logger.info("Calling the show method.")

        with open(file, "r", ) as f:
            df = json.load(f)
            return df

    @staticmethod
    def flatten(file: str):
        flk = FLT.flatten_dict(fll=file)
        flk = json.dumps(flk)
        return flk
