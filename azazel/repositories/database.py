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
import aiosqlite
from aiosqlite import Connection


class DbContext:
    def __init__(self, db_name: str = "azazel.db") -> None:
        self.db_name = db_name
        self.conn: Connection | None = None

    async def __aenter__(self) -> "DbContext":
        self.conn = await aiosqlite.connect(self.db_name)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore
        if self.conn:
            await self.conn.close()
