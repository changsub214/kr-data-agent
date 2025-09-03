# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pandas as pd
import altair as alt
import vl_convert as vlc
import io, os
import traceback

from dotenv import load_dotenv 
from typing import List, Optional
from datetime import datetime
from google.cloud import storage


current_path = os.path.dirname(__file__)
dotenv_path = os.path.join(os.path.dirname(current_path), '.env')
load_dotenv(dotenv_path)

GOOGLE_CLOUD_BUCKET = os.getenv("GOOGLE_CLOUD_BUCKET")

def configure_korean_font(chart):
    """
    Applies NanumGothic font settings to all parts of an Altair chart.
    """
    
    return chart.configure_title(
        font='NanumGothic'
    ).configure_axis(
        labelFont='NanumGothic',
        titleFont='NanumGothic'
    ).configure_legend(
        labelFont='NanumGothic',
        titleFont='NanumGothic'
    )

#gcs
def save_chart_to_gcs(chart, title):
    """
    Saves a chart object to a bucket and returns the path.
    You want to know path, refer to return value. 
    """
    
    storage_client = storage.Client()

    try:
        bucket = storage_client.get_bucket(GOOGLE_CLOUD_BUCKET)
    except Exception:
        print(f"Bucket: {GOOGLE_CLOUD_BUCKET} not found. now try making bucket..")
        bucket = storage_client.create_bucket(GOOGLE_CLOUD_BUCKET)
    

    timestamp = datetime.now().strftime("%Y%m%d")
    title = "".join(c for c in title if c.isalnum() or c in (' ', '_')).rstrip()
    filename = f"{timestamp}_{title}.png"
    chart_json = chart.to_json()
    png_bytes = vlc.vegalite_to_png(vl_spec=chart_json)
    
    blob = bucket.blob(filename)
    blob.upload_from_string(png_bytes, content_type='image/png')
    gcs_uri = f"gs://{GOOGLE_CLOUD_BUCKET}/{filename}"
    #print(gcs_uri)

        
    return f"{gcs_uri}"

#local
def save_chart(chart, title):
    """
    Saves a chart object to a file and returns the path.
    """
    
    script_dir = os.path.dirname(__file__)
    output_dir = os.path.join(script_dir, 'img')
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d")
    title = "".join(c for c in title if c.isalnum() or c in (' ', '_')).rstrip()
    filename = f"{timestamp}_{title}.png"
    file_path = os.path.join(output_dir, filename)
    
    chart_json = chart.to_json()
    png_bytes = vlc.vegalite_to_png(vl_spec=chart_json)
    
    with open(file_path, "wb") as f:
        f.write(png_bytes)
        
    return f"{file_path}"


def create_bar_chart(
    df_json: str, x_column: str, y_columns: List[str], title: str
) -> str:
    """
    Creates a BAR CHART from a pandas DataFrame and saves it as an image.

    Args:
        df_json (str): A JSON string representing a pandas DataFrame.
        x_column (str): The column name for the categorical x-axis.
        y_columns (List[str]): A list with the column name for the numerical y-axis.
        title (str): The title of the chart.

    Returns:
        str: A confirmation message with the saved chart's file path, or an error message.
    """

    try:
        df = pd.read_json(io.StringIO(df_json))
        
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X(x_column, type="nominal", sort=None),
            y=alt.Y(y_columns[0], type="quantitative"),
            tooltip=df.columns.tolist()
        ).properties(title=title)
        
        chart = configure_korean_font(chart)
        #return save_chart(chart, title) 
        return save_chart_to_gcs(chart, title)

    except Exception as e:
        error_details = traceback.format_exc()
        return f"Error creating bar chart: {error_details}"


def create_line_chart(
    df_json: str, x_column: str, y_columns: List[str], title: str
) -> str:
    """
    Creates a LINE CHART to show trends and saves it as an image.

    Args:
        df_json (str): A JSON string representing a pandas DataFrame.
        x_column (str): The column name for the x-axis (often time or an ordered category).
        y_columns (List[str]): A list with the column name for the numerical y-axis.
        title (str): The title of the chart.

    Returns:
        str: A confirmation message with the saved chart's file path, or an error message.
    """
    
    try:
        df = pd.read_json(io.StringIO(df_json))

        chart = alt.Chart(df).mark_line().encode(
            x=alt.X(x_column, type="nominal", sort=None),
            y=alt.Y(y_columns[0], type="quantitative"),
            tooltip=df.columns.tolist()
        ).properties(title=title)
        
        chart = configure_korean_font(chart)
        #return save_chart(chart, title)
        return save_chart_to_gcs(chart, title)

    except Exception as e:
        error_details = traceback.format_exc()
        return f"Error creating line chart: {error_details}"


def create_scatter_plot(
    df_json: str, x_column: str, y_column: str, title: str, color_column: Optional[str] = None
) -> str:
    """
    Creates a SCATTER PLOT to show the relationship between two variables and saves it as an image.

    Args:
        df_json (str): A JSON string representing a pandas DataFrame.
        x_column (str): The column name for the numerical x-axis.
        y_column (str): The column name for the numerical y-axis.
        title (str): The title of the chart.
        color_column (str, optional): A column name to color the points by. Defaults to None.

    Returns:
        str: A confirmation message with the saved chart's file path, or an error message.
    """

    try:
        df = pd.read_json(io.StringIO(df_json))

        encoding = {
            'x': alt.X(x_column, type='quantitative'),
            'y': alt.Y(y_column, type='quantitative'),
            'tooltip': df.columns.tolist()
        }
        if color_column and color_column in df.columns:
            encoding['color'] = alt.Color(color_column, type='nominal')

        chart = alt.Chart(df).mark_point().encode(**encoding).properties(title=title)
        
        chart = configure_korean_font(chart)
        #return save_chart(chart, title)
        return save_chart_to_gcs(chart, title)

    except Exception as e:
        error_details = traceback.format_exc()
        return f"Error creating scatter plot: {error_details}"


def create_histogram(
    df_json: str, column: str, title: str
) -> str:
    """
    Creates a HISTOGRAM to show the distribution of a single variable and saves it as an image.

    Args:
        df_json (str): A JSON string representing a pandas DataFrame.
        column (str): The numerical column whose distribution is to be plotted.
        title (str): The title of the chart.

    Returns:
        str: A confirmation message with the saved chart's file path, or an error message.
    """
    
    try:
        df = pd.read_json(io.StringIO(df_json))

        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X(column, bin=True, title=f'{column} distribution'),
            y=alt.Y('count()', title='Count')
        ).properties(title=title)
        
        chart = configure_korean_font(chart)
        #return save_chart(chart, title)
        return save_chart_to_gcs(chart, title)

    except Exception as e:
        error_details = traceback.format_exc()
        return f"Error creating scatter plot: {error_details}"