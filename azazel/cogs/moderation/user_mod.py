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
from discord import Interaction, Member, app_commands
from discord.ext.commands import Bot, Cog, Context, command, has_permissions

from azazel.utils.exceptions import ActionNotAllowed, InvalidMember


class UserMod(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    # region Base Commands
    async def _kick(
        self, author: Member, bot: Member, target: Member, reason: str | None = None
    ) -> None:
        if bot == target:
            raise InvalidMember("I can't kick myself")

        if author == target:
            raise InvalidMember("You can't kick yourself")

        if author.top_role <= target.top_role:
            raise ActionNotAllowed("You cannot kick this member due to role hierarchy")

        if bot.top_role <= target.top_role:
            raise ActionNotAllowed("I cannot kick this member due to role hierarchy")

        await target.kick(reason=reason)

    async def _ban(
        self, author: Member, bot: Member, target: Member, reason: str | None = None
    ) -> None:
        if bot == target:
            raise InvalidMember("I can't ban myself")

        if author == target:
            raise InvalidMember("You can't ban yourself")

        if author.top_role <= target.top_role:
            raise ActionNotAllowed("You cannot ban this member due to role hierarchy")

        if bot.top_role <= target.top_role:
            raise ActionNotAllowed("I cannot ban this member due to role hierarchy")

        await target.ban(reason=reason)

    async def _unban(self) -> None:
        pass

    # endregion

    # region Commands
    @command()
    @has_permissions(ban_members=True)
    async def ban(
        self, ctx: Context[Bot], member: Member, reason: str | None = None
    ) -> None:
        try:
            await self._ban(ctx.author, ctx.guild.me, member, reason)  # type: ignore
            await ctx.send(f"{member.mention} was banned by {ctx.author.name}.")
        except InvalidMember as e:
            await ctx.send(f"This member is not valid: {e}.")
        except ActionNotAllowed as e:
            await ctx.send(f"Action not allowed: {e}.")

    @command()
    @has_permissions(ban_members=True)
    async def unban(
        self, ctx: Context[Bot], member: Member, reason: str | None = None
    ) -> None:
        pass

    @command()
    @has_permissions(kick_members=True)
    async def kick(
        self, ctx: Context[Bot], member: Member, reason: str | None = None
    ) -> None:
        try:
            await self._kick(ctx.author, ctx.guild.me, member, reason)  # type: ignore
            await ctx.send(f"{member.mention} was kicked by {ctx.author.name}.")
        except InvalidMember as e:
            await ctx.send(f"This member is not valid: {e}.")
        except ActionNotAllowed as e:
            await ctx.send(f"Action not allowed: {e}.")

    # endregion

    # region Slash Commands
    @app_commands.command(name="ban")
    @app_commands.default_permissions(ban_members=True)
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban_slash(
        self, inter: Interaction, member: Member, reason: str | None = None
    ) -> None:
        pass

    @app_commands.command(name="unban")
    @app_commands.default_permissions(ban_members=True)
    @app_commands.checks.has_permissions(ban_members=True)
    async def unban_slash(
        self, inter: Interaction, member: Member, reason: str | None = None
    ) -> None:
        pass

    @app_commands.command(name="kick")
    @app_commands.default_permissions(kick_members=True)
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick_slash(
        self, inter: Interaction, member: Member, reason: str | None = None
    ) -> None:
        try:
            await self._kick(inter.user, inter.guild.me, member, reason)  # type: ignore
            await inter.response.send_message(
                f"{member.mention} was kicked by {inter.user.name}."
            )
        except InvalidMember as e:
            await inter.response.send_message(f"This member is not valid: {e}.")
        except ActionNotAllowed as e:
            await inter.response.send_message(f"Action not allowed: {e}.")

    # endregion


async def setup(bot: Bot) -> None:
    await bot.add_cog(UserMod(bot))
