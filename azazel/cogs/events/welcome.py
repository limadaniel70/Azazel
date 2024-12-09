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
from discord.ext.commands import Bot, Cog

from azazel.utils.embeds import welcome_message


class Welcome(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member: Member) -> None:
        pass

    async def __dm_welcome_message(
        self, member: Member | User, message: str | Embed | None = None
    ) -> None:
        if message is None:
            return
        elif isinstance(message, Embed):
            await member.send(embed=message)
        else:
            await member.send(message)


async def setup(bot: Bot) -> None:
    await bot.add_cog(Welcome(bot))
