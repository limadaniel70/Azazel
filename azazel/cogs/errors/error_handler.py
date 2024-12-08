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
from discord.ext.commands import Bot, Cog, Context, CommandError
from discord.ext.commands import (
    MemberNotFound,
    MissingPermissions,
    MissingRequiredArgument,
)


logger = logging.getLogger("discord")


class ErrorHandler(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_command_error(self, ctx: Context[Bot], error: CommandError) -> None:
        if isinstance(error, MemberNotFound):
            await ctx.send(f"Could not find member '{error.argument}'.")
        elif isinstance(error, MissingPermissions):
            await ctx.send(
                f"You don't have the required permissions to use this command.\n"
                f"Missing Permissions: {', '.join(error.missing_permissions)}."
            )
        elif isinstance(error, MissingRequiredArgument):
            await ctx.send(f"'{error.param.name}' is a required argument.")
        else:
            logger.error("Unhandled error: %s", error)
            await ctx.send("An unexpected error ocurred. Please try again later.")

    # @Cog.listener()
    # async def on_error(self) -> None:
    #    pass


async def setup(bot: Bot) -> None:
    await bot.add_cog(ErrorHandler(bot))
