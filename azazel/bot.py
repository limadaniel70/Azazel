import logging
import discord
from discord.ext import commands
import dotenv
import os

dotenv.load_dotenv()

token = os.getenv("DISCORD_API_KEY")
if token == None:
    raise Exception("Null token.")

handler = logging.FileHandler(filename="azazel.log", encoding="utf-8", mode="w")
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

enviroment = os.getenv("ENVIROMENT")
if enviroment == "DEVELOPMENT":
    level = 10 # DEBUG
else:
    level = 20 # INFO

intents = discord.Intents().default()

bot = commands.Bot(command_prefix="zl", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged as {bot.user}")

bot.run(token=token)