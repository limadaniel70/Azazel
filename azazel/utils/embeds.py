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
import datetime
from discord import Embed, Guild, Member, User

from azazel.utils.constants import Colors


def message(title: str, msg: str, author: Member | User) -> Embed:
    emb = Embed(title=title, description=msg, color=Colors.AZAZEL_RED.value)
    emb.set_author(name=author.name, icon_url=author.avatar)
    return emb


def welcome_message(guild_name: str, message: str, member_name: str) -> Embed:
    emb = Embed(
        title=f"Welcome to {guild_name}, {member_name}",
        description=message,
        color=Colors.AZAZEL_RED.value,
    )
    return emb


def server_info(guild: Guild) -> Embed:
    emb = Embed(
        title="SERVER INFO",
        color=Colors.AZAZEL_RED.value,
        timestamp=datetime.datetime.now(),
    )
    emb.add_field(name="Server Name", value=f"```{guild.name}```")
    emb.add_field(name="Server Owner ID", value=f"```{guild.owner_id}```")
    bots = sum(1 for member in guild.members if member.bot)
    emb.add_field(
        name=f"Server Members [{guild.member_count}]",
        value=f"```Members: {guild.member_count - bots if guild.member_count else 0} | Bots: {bots}```",
        inline=False,
    )
    emb.add_field(name="Server ID", value=f"```{guild.id}```")
    emb.add_field(
        name="Server Boosts",
        value=f"```{guild.premium_subscription_count} (Level: {guild.premium_tier})```",
    )
    emb.add_field(
        name=f"Server Roles [{len(guild.roles)}] (first 15 roles)",
        value=f"```{", ".join([role.name for role in guild.roles[:15]])}```",
        inline=False,
    )
    emb.add_field(
        name="Server creation date (DD/MM/YYYY)",
        value=f"```{guild.created_at.date():%d/%m/%Y} ({(datetime.date.today() - guild.created_at.date()).days} days)```",
        inline=False,
    )
    emb.set_thumbnail(url=guild.icon)
    return emb


def user_info() -> Embed:
    emb = Embed()
    return emb
