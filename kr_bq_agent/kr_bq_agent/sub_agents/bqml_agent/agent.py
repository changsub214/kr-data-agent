# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from google.adk.agents import Agent
from dotenv import load_dotenv
from google.adk.tools.bigquery import BigQueryCredentialsConfig
from google.adk.tools.bigquery import BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig
from google.adk.tools.bigquery.config import WriteMode
from .prompts import return_description, return_prompt
import google.auth


current_path = os.path.dirname(__file__)
dotenv_path = os.path.join(os.path.dirname(current_path), '.env')
load_dotenv(dotenv_path)


tool_config = BigQueryToolConfig(write_mode=WriteMode.ALLOWED)

#credential
application_default_credentials, _ = google.auth.default()
credentials_config = BigQueryCredentialsConfig(
    credentials=application_default_credentials
)

bigquery_toolset = BigQueryToolset(
    credentials_config=credentials_config,
    bigquery_tool_config=tool_config,
    tool_filter=["execute_sql"],
)

root_agent = Agent(
    name="BQML_Agent",
    model=os.getenv("MODEL"),
    description=return_description(),
    instruction=return_prompt(),
    tools=[bigquery_toolset],
)