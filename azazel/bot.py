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

import logging
import os

import discord
import dotenv
from discord.ext import commands

dotenv.load_dotenv()

token = os.getenv("DISCORD_API_KEY")
if token == None:
    raise Exception("Null token.")

handler = logging.FileHandler(filename="azazel.log", encoding="utf-8", mode="w")
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

enviroment = os.getenv("ENVIROMENT")
if enviroment == "DEVELOPMENT":
    level = 10  # DEBUG
else:
    level = 20  # INFO

intents = discord.Intents().default()

bot = commands.Bot(command_prefix="zl", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged as {bot.user}")


bot.run(token=token)
