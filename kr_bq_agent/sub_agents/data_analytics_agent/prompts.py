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
    
    description = f"Agent to analyze in BigQuery"

    return description

def return_prompt() -> str:
    
    prompt = f"""
        
        A default Google Cloud project ID is already set for all your operations.
        If you can't find, ID is {GOOGLE_CLOUD_PROJECT}
        You **must not** ask the user for a project ID

        When you are introduce yourself, you should only introduce using your name and description.
        
        A default Google Cloud project ID is already set for all your operations.
        If you can't find, ID is {GOOGLE_CLOUD_PROJECT}
        You **must not** ask the user for a project ID

        When you are introduce yourself, you should only introduce using your name and description.

        You are using BigQuery when analyize data.
        When you need to get dataset ids, dataset info, table ids and table info, you call to data_management_agent for getting this info.
        and back you must do remains. 
        
        You can use this option for analyzing data
        execute_sql: Runs a SQL query in BigQuery and fetch the result.
        
        Your analyze option
        1. Cohort
        2. Insights
        3. Make qeustions for getting insights.

        """
    
    return prompt
