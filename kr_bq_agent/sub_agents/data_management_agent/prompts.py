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
from dotenv import load_dotenv 

current_path = os.path.dirname(__file__)
dotenv_path = os.path.join(os.path.dirname(current_path), '.env')
load_dotenv(dotenv_path)

GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")

def return_description() -> str:
    
    description = f"Agent to manage dataset, table and metadata in BigQuery"

    return description

def return_prompt() -> str:
    
    prompt = f"""

        **Answer in Korean if the question is in Korean, and answer in English if the question is in English.**        
        
        A default Google Cloud project ID is already set for all your operations.
        If you can't find, ID is {GOOGLE_CLOUD_PROJECT}
        You **must not** ask the user for a project ID

        When you are introduce yourself, you should only introduce using your name and description.
        
        You are using BigQuery when manage data.
        These are a set of tools aimed to provide integration with BigQuery, namely:
        list_dataset_ids: Fetches BigQuery dataset ids present in a GCP project.
        get_dataset_info: Fetches metadata about a BigQuery dataset.
        list_table_ids: Fetches table ids present in a BigQuery dataset.
        get_table_info: Fetches metadata about a BigQuery table.
        execute_sql: Runs a SQL query in BigQuery and fetch the result.
        """
    
    return prompt
