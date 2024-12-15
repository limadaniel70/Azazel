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
import os
from dataclasses import dataclass

import dotenv

dotenv.load_dotenv()


@dataclass
class EnvConfig:
    token: str | None
    environment: str
    db_connection: str | None


env = EnvConfig(
    token=os.getenv("DISCORD_API_KEY"),
    environment=os.getenv("ENVIRONMENT", "PRODUCTION"),
    db_connection=os.getenv("DATABASE_CONNECTION_STRING"),
)
