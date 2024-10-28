#     Copyright 2024 Daniel Lima
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
import os
from math import expm1
from pathlib import Path

import discord
import dotenv
from discord.ext import commands

from azazel.utils.exceptions import NullToken

dotenv.load_dotenv()

TOKEN = os.getenv("DISCORD_API_KEY")
if TOKEN is None:
    raise NullToken("The token cannot be empty!")


class AzazelBot(commands.Bot):
    def __init__(self):
        super().__init__("!!", intents=discord.Intents.all())

    async def setup_hook(self) -> None:
        for cog in Path("./azazel/cogs").iterdir():
            if Path(cog).suffix == ".py":
                try:
                    await self.load_extension(f"cogs.{str(cog)}")
                    print(f"Cog loaded successfully: {str(cog)}")
                except Exception as e:
                    print(f"[*] Cog failed: {str(cog)}\nError: {e}")


if __name__ == "__main__":
    client = AzazelBot()
    client.run(TOKEN)
