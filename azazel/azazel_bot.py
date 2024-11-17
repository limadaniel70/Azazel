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
from discord.ext.commands import Bot, CommandError, Context

from azazel.utils.constants import NullToken

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


class AzazelBot(Bot):
    def __init__(self) -> None:
        super().__init__("!!", intents=discord.Intents.all())
        logger.info("Starting AzazelBot")

    async def on_ready(self) -> None:
        logger.info("Logged in")

    async def on_command_error(self, ctx: Context, exception: CommandError) -> None:  # type: ignore
        await ctx.send(f"Error: {exception}")
        return await super().on_command_error(ctx, exception)

    async def setup_hook(self) -> None:
        for cog_type in Path("./azazel/cogs").iterdir():
            for cog in cog_type.iterdir():
                if cog.suffix == ".py":
                    try:
                        # Cog example: PosixPath("azazel/cogs/utils/ping.py")
                        # cog.parts -> ["azazel", "cogs", "utils", "ping.py"]
                        # cog.parts[1:-1] -> ["cogs", "utils"]
                        # '.'join(cog.parts[1:-1]) + f".{cog.stem}"-> "cogs.utils.ping"
                        await self.load_extension(
                            ".".join(cog.parts[1:-1]) + f".{cog.stem}"
                        )
                        logger.info(
                            "Cog loaded successfully: %s", ".".join(cog.parts[1:])
                        )
                    except FileNotFoundError:
                        logger.error("couldn't find %s", ".".join(cog.parts[1:]))
                    except Exception as e:
                        logger.error(
                            "Cog failed: %s\nError: %s", ".".join(cog.parts[1:]), e
                        )


if __name__ == "__main__":
    client = AzazelBot()
    client.run(TOKEN, log_handler=None)
