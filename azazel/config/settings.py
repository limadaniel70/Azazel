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
import logging
import os

import dotenv

from azazel.utils.exceptions import NullToken

dotenv.load_dotenv()


def get_discord_token() -> str:
    token = os.getenv("DISCORD_API_KEY")
    if token is None:
        raise NullToken("The token cannot be empty!")
    return token


def setup_logging() -> None:
    logger = logging.getLogger("discord")
    logger.handlers.clear()
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
    handler = logging.StreamHandler()

    if os.getenv("ENVIRONMENT") == "DEVELOPMENT":
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    handler.setFormatter(formatter)
    logger.addHandler(handler)
