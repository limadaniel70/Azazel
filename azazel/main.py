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
import sys

from azazel.azazel_bot import AzazelBot
from azazel.config.env import env
from azazel.config.log import setup_logging
from azazel.utils.exceptions import NullToken


def main() -> None:
    """
    Azazel's entry point
    """
    setup_logging("azazel")
    setup_logging("discord")
    logger = logging.getLogger("azazel")
    try:
        if env.token:
            bot = AzazelBot()
            bot.run(env.token, log_handler=None)
        else:
            raise NullToken("The bot token is not set!")
    except KeyboardInterrupt:
        logger.info("Shutting down.")
        sys.exit(0)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
