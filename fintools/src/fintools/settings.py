import logging
import string
import os
from logging.config import dictConfig
from typing import Dict, Optional

# General


# Logging configuration

CROD_DEFAULT_LOGLEVEL = os.environ.get(
    "CROD_DEFAULT_LOGLEVEL",
    default="WARN"
)

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
    },
    "handlers": {
        "default": {
            "level": CROD_DEFAULT_LOGLEVEL,
            "formatter": "standard",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "": {
            "handlers": [
                "default"
            ],
            "level": CROD_DEFAULT_LOGLEVEL,
            "propagate": True
        }
    }
}


def get_logger(name: str, logging_config_dictionary: Optional[Dict] = None):
    if logging_config_dictionary is None:
        logging_config_dictionary = logging_config
    dictConfig(logging_config_dictionary)
    return logging.getLogger(name)
