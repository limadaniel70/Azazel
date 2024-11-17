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
from discord.ext.commands import Bot, Cog, Context, command, has_permissions
from discord import app_commands, Interaction, TextChannel


class MessageMod(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    @has_permissions(manage_messages=True)
    async def purge(self, ctx: Context[Bot], count: int = 2) -> None:
        await ctx.channel.purge(limit=count)  # type: ignore

    @app_commands.command(name="purge")
    @app_commands.default_permissions(manage_messages=True)
    @app_commands.checks.has_permissions(manage_messages=True)
    async def purge_slash(self, inter: Interaction, count: int = 2) -> None:
        await inter.channel.purge(limit=count)  # type: ignore

    @command()
    @has_permissions(manage_messages=True)
    async def send_message(
        self, ctx: Context[Bot], msg: str, title: str, target: TextChannel
    ) -> None:
        pass

async def setup(bot: Bot) -> None:
    await bot.add_cog(MessageMod(bot))
