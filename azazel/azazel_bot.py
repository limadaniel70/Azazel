#    Copyright 2024 Daniel Lima
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import asyncio
import logging
import os
# import pathlib

import discord
import dotenv
from discord.ext import commands

from azazel.utils.exceptions import NullToken

dotenv.load_dotenv()

token = os.getenv("DISCORD_API_KEY")
if token is None:
    raise NullToken("The token cannot be empty!")

enviroment = os.getenv("ENVIROMENT")
if enviroment == "DEVELOPMENT":
    level = 10  # DEBUG
else:
    level = 20  # INFO

file_handler = logging.FileHandler(filename="azazel.log", encoding="utf-8", mode="a")
logging.basicConfig(
    handlers=[file_handler], format="%(asctime)s %(levelname)s %(message)s", level=level
)
logger = logging.getLogger(__name__)

intents = discord.Intents().all()

bot = commands.Bot(command_prefix="zl", intents=intents)


@bot.event
async def on_ready() -> None:
    logger.info("Bot ready as %s", bot.user)


# async def load() -> None:
#     """
#     Loads the commands.
#     """
#     for file in pathlib.Path("azazel/commands").iterdir():
#         if file.suffix == ".py":
#             await bot.load_extension(f"commands.{file.name[:-3]}")


async def main() -> None:
    # await load()
    await bot.start(str(token))

asyncio.run(main())
