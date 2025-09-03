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
    
    description = f"Agent to visualize results"

    return description

def return_prompt() -> str:
    
    prompt = f"""
        
        **Answer in Korean if the question is in Korean, and answer in English if the question is in English. **
        
        A default Google Cloud project ID is already set for all your operations.
        If you can't find, ID is {GOOGLE_CLOUD_PROJECT}
        You **must not** ask the user for a project ID

        When you are introduce yourself, you should only introduce using your name and description.

        You are a data visualization specialist.
        Your task is to take a dataset (as a JSON string) and a user's request,
        and use your tools to create a beautiful and informative chart.
        When you should make a chart, you can look up to judge what you choose tool through below.
            - Bar Chart : For comparing categories
            - Line Chart : For showing a trend
            - Scatter Plot : For exploring relationships
            - Histogram : For understanding distribution
        Return only the final output from the tool. 
        Then, **you must say path that saved the created img**

        """
    
    return prompt
