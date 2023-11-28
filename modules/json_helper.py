import json
import os
from modules import scripts
from modules.api.models import TextToImageJsonModel

def get_json_content(file_path):
    try:
        with open(file_path, 'rt', encoding="utf-8") as file:
            json_data = json.load(file)
            return json_data
    except Exception as e:
        print(f"A Problem occurred: {str(e)}")
    return []

def get_text2img_data(model_id: str):
    json_path = os.path.join(scripts.basedir(), 'text2img.json')
    json_data = get_json_content(json_path)
    if not isinstance(json_data, list):
        print("Error: input data must be a list")
        return None
        
    model_id_key = 'model_id'
    sampeller_method = 'sampeller_method'
    step = 'step'
    cfg = 'cfg'
    prompt = 'prompt'
    negative_prompt = 'negative_prompt'
        
    # Iterate over each item in the data list
    for item in json_data:
        # Check that the item is a dictionary
        if isinstance(item, dict):
            # Check that all required key is in the dictionary
            if model_id_key in item and item[model_id_key] == model_id:
                if sampeller_method in item and step in item and cfg in item and prompt in item and negative_prompt in item:
                    return TextToImageJsonModel(model_id = model_id, 
                                                sampeller_method = item[sampeller_method], 
                                                step = item[step], 
                                                cfg = item[cfg], 
                                                prompt = item[prompt],
                                                negative_prompt = item[negative_prompt])
    print("Error: model not found")     
    return None