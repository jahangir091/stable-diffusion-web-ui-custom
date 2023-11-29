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
    
    model_info = 'model_info'
    global_pos_prompt_key = 'global_pos_prompt'
    global_neg_prompt_key = 'global_neg_prompt'
        
    model_id_key = 'model_id'
    sampeller_method = 'sampeller_method'
    step = 'step'
    cfg = 'cfg'
    prompt = 'prompt'
    negative_prompt = 'negative_prompt'
    denoising_strength = 'denoising_strength'

    global_positive_prompt = ""
    global_negative_prompt = ""

    if global_pos_prompt_key in json_data:
        global global_positive_prompt
        global_positive_prompt = json_data[global_pos_prompt_key]
    else:
        print("Error: can't get global postive prompt")

    if global_neg_prompt_key in json_data:
        global global_negative_prompt
        global_negative_prompt = json_data[global_neg_prompt_key]
    else:
        print("Error: can't get global negative prompt")

    if not model_info in json_data:
        print("Error: can't extract model info from json")
        return None
    
    model_info_dict = json_data[model_info]
    if not isinstance(model_info_dict, list):
        print("Error: model info must be a list")
        return None
    
    print(global_positive_prompt)
    print(global_negative_prompt)
    print("siam")
        
    # Iterate over each item in the data list
    for item in model_info_dict:
        # Check that the item is a dictionary
        if isinstance(item, dict):
            # Check that all required key is in the dictionary
            if model_id_key in item and item[model_id_key] == model_id:
                if sampeller_method in item and step in item and cfg in item and prompt in item and negative_prompt in item and denoising_strength in item:
                    return TextToImageJsonModel(model_id = model_id, 
                                                sampeller_method = item[sampeller_method], 
                                                step = item[step], 
                                                cfg = item[cfg], 
                                                prompt = item[prompt],
                                                negative_prompt = item[negative_prompt],
                                                denoising_strength = item[denoising_strength],
                                                global_positive=global_positive_prompt,
                                                global_negative=global_negative_prompt)
    print("Error: model not found")     
    return None