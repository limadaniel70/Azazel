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
from enum import Enum


class Colors(Enum):
    AZAZEL_RED = 0xFF013D
    EMERALD_GREEN = 0x01FF9F
    PURE_WHITE = 0xFFFFFF
    CRIMSON = 0xB00029
    GOLD = 0xFFC401


# Exceptions
class NullToken(Exception):
    """
    Exception raised when the bot token is empty.

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)
