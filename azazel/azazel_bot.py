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
from pathlib import Path

import discord
import dotenv
from discord.ext import commands

from azazel.utils.exceptions import NullToken

dotenv.load_dotenv()

TOKEN = os.getenv("DISCORD_API_KEY")
if TOKEN is None:
    raise NullToken("The token cannot be empty!")

logger = logging.getLogger("discord")
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
handler = logging.StreamHandler()

environment = os.getenv("ENVIRONMENT")
if environment == "DEVELOPMENT":
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)


handler.setFormatter(formatter)
logger.addHandler(handler)


class AzazelBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__("!!", intents=discord.Intents.all())
        logger.info("Starting AzazelBot")

    async def on_ready(self) -> None:
        logger.info("Logged in")

    async def setup_hook(self) -> None:
        for cog in Path("./azazel/cogs").iterdir():
            if Path(cog).suffix == ".py":
                try:
                    # example cog: PosixPath("cogs/ping.py")
                    # str(cog.parts[-1][:-3]) -> "ping"
                    await self.load_extension(f"cogs.{str(cog.parts[-1][:-3])}")
                    logger.info("Cog loaded successfully: %s", str(cog.parts[-1]))
                except FileNotFoundError:
                    logger.error("couldn't find %s", str(cog))
                except Exception as e:
                    logger.error("Cog failed: %s\nError: %s", str(cog), e)


if __name__ == "__main__":
    client = AzazelBot()
    client.run(TOKEN, log_handler=None)
