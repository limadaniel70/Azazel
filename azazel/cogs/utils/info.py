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
from discord import Embed, Member, User
from discord.ext.commands import Bot, Cog, Context, command

from azazel.utils.embeds import server_info, user_info


class Info(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command(name="serverinfo")
    async def server_info(self, ctx: Context[Bot]) -> None:
        if ctx.guild is None:
            return
        await ctx.send(embed=server_info(ctx.guild))

    @command(name="userinfo")
    async def user_info(self, ctx: Context[Bot]) -> None:
        pass


async def setup(bot: Bot) -> None:
    await bot.add_cog(Info(bot))
