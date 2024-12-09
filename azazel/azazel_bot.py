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
from pathlib import Path

import discord
from discord.ext.commands import Bot

logger = logging.getLogger("discord")


class AzazelBot(Bot):
    def __init__(self) -> None:
        super().__init__("!!", intents=discord.Intents.all())
        logger.info("Starting AzazelBot")

    async def on_ready(self) -> None:
        logger.info("Logged in as %s", self.user)
        logger.debug("Servers [%d]:", len(self.guilds))
        for i, guild in enumerate(self.guilds):
            logger.debug("[%d] - %s : (ID: %d)", i, guild.name, guild.id)

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
                        logger.info("Cog loaded successfully: %s", cog)

                    except FileNotFoundError:
                        logger.error("couldn't find %s", cog)
                    except Exception as e:
                        logger.error("Cog failed: %s -> %s", cog, e)
