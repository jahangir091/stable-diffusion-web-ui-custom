import contextlib

import gradio as gr
from modules import scripts
# from modules.ui_components import FormRow, FormColumn, FormGroup, ToolButton
import json
import os
import random
stylespath = "sdxl_styles.json"

from modules.api.models import TextToImageStyleInfo


def get_json_content(file_path):
    try:
        with open(file_path, 'rt', encoding="utf-8") as file:
            json_data = json.load(file)
            return json_data
    except Exception as e:
        print(f"A Problem occurred: {str(e)}")


def read_sdxl_styles(json_data):
    # Check that data is a list
    if not isinstance(json_data, list):
        print("Error: input data must be a list")
        return None

    names = []

    # Iterate over each item in the data list
    for item in json_data:
        # Check that the item is a dictionary
        if isinstance(item, dict):
            # Check that 'name' is a key in the dictionary
            if 'name' in item:
                # Append the value of 'name' to the names list
                names.append(item['name'])
    names.sort()
    return names

def getStylesInfo():
    global stylespath
    json_path = os.path.join(scripts.basedir(), 'sdxl_styles.json')
    stylespath = json_path
    json_data = get_json_content(json_path)

    styles = []
    
    if not isinstance(json_data, list):
        print("Error: input data must be a list")
        return styles
    
    isPremium = 'isPremium'
    isActive = 'isActive'
    priority = 'priority'
    id = 'id'
    style_name = 'name'
    display_name = 'display_name'
    thumbnail_url = 'thumbnail_url'

    # Iterate over each item in the data list
    for item in json_data:
        # Check that the item is a dictionary
        if isinstance(item, dict):
            # Check that 'name' is a key in the dictionary
            if display_name in item and style_name in item and priority in item and id in item and isPremium in item and isActive in item and thumbnail_url in item:
                # Append to the list
                if item[isActive] == True:
                    styleInfo = TextToImageStyleInfo(id=item[id],
                                                name=item[display_name],
                                                style=item[style_name],
                                                isPremium=item[isPremium],
                                                priority=item[priority],
                                                thumbnail_url=item[thumbnail_url])
                    styles.append(styleInfo)
    return styles

def getStyles():
    global stylespath
    json_path = os.path.join(scripts.basedir(), 'sdxl_styles.json')
    stylespath = json_path
    json_data = get_json_content(json_path)
    styles = read_sdxl_styles(json_data)
    return styles


def createPositive(style, positive):
    json_data = get_json_content(stylespath)
    try:
        # Check if json_data is a list
        if not isinstance(json_data, list):
            raise ValueError(
                "Invalid JSON data. Expected a list of templates.")

        for template in json_data:
            # Check if template contains 'name' and 'prompt' fields
            if 'name' not in template or 'prompt' not in template:
                raise ValueError(
                    "Invalid template. Missing 'name' or 'prompt' field.")

            # Replace {prompt} in the matching template
            if template['name'] == style:
                positive = template['prompt'].replace(
                    '{prompt}', positive)

                return positive

        # If function hasn't returned yet, no matching template was found
        raise ValueError(f"No template found with name '{style}'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def createNegative(style, negative):
    json_data = get_json_content(stylespath)
    try:
        # Check if json_data is a list
        if not isinstance(json_data, list):
            raise ValueError(
                "Invalid JSON data. Expected a list of templates.")

        for template in json_data:
            # Check if template contains 'name' and 'prompt' fields
            if 'name' not in template or 'prompt' not in template:
                raise ValueError(
                    "Invalid template. Missing 'name' or 'prompt' field.")

            # Replace {prompt} in the matching template
            if template['name'] == style:
                json_negative_prompt = template.get('negative_prompt', "")
                if negative:
                    negative = f"{json_negative_prompt}, {negative}" if json_negative_prompt else negative
                else:
                    negative = json_negative_prompt

                return negative

        # If function hasn't returned yet, no matching template was found
        raise ValueError(f"No template found with name '{style}'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


