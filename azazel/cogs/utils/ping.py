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
from discord import Interaction, app_commands
from discord.ext.commands import Bot, Cog, Context, command


class Ping(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    def get_latency(self) -> float:
        """
        Gets the bot latency in milliseconds

        Returns:
            float: the latency in milliseconds.
        """
        return self.bot.latency * 1000

    @command()
    async def ping(self, ctx: Context[Bot]) -> None:
        await ctx.send(f"Pong!\nLatency: {self.get_latency():.3f} ms")

    @command()
    async def echo(self, ctx: Context[Bot]) -> None:
        message = ctx.message.content.split(" ")
        await ctx.send(" ".join(message[1:]))

    @app_commands.command(name="ping", description="Get the bot's latency")
    async def ping_slash(self, inter: Interaction) -> None:
        await inter.response.send_message(
            f"Pong!\nLatency: {self.get_latency():.3f} ms"
        )

    @app_commands.command(name="echo", description="Echo a message")
    async def echo_slash(self, inter: Interaction, message: str) -> None:
        await inter.response.send_message(message)


async def setup(bot: Bot) -> None:
    await bot.add_cog(Ping(bot))
