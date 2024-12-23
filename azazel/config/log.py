#  Copyright 2024 Daniel Lima
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from logging.config import dictConfig

LOGGING_CONFIG = {  # type: ignore
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"}
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "file": {
            "level": "WARNING",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/azazel.log",
            "mode": "a",
            "maxBytes": 10 * 1024 * 1024,  # 10 MB
            "backupCount": 5,
            "formatter": "standard",
        },
    },
    "loggers": {
        "": {  # root
            "handlers": ["console"],
            "level": "WARNING",
        },
        "azazel": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "discord": {
            "handlers": ["console", "file"],
            "level": "WARNING",
            "propagate": False,
        },
    },
}

dictConfig(LOGGING_CONFIG)
