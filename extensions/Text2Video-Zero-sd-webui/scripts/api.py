import time
import string
import random

import torch

from fastapi import FastAPI, Body

from modules.api.models import *
import gradio as gr



from model import Model



def text2video_zero(prompt, t0=44, t1=47, video_length=8, fps=4, output_directory="output/videos/", video_format='.mp4', model_name=None):
    model = Model(device="cuda", dtype=torch.float16)
    params = {
        "t0": t0,
        "t1": t1,
        "motion_field_strength_x": 12,
        "motion_field_strength_y": 12,
        "video_length": video_length
    }
    rand_string = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=10))
    out_path, fps = output_directory + rand_string + video_format, fps
    if not model_name:
        model.process_text2video(prompt, fps=fps, path=out_path, **params)
    else:
        model.process_text2video(prompt, model_name=model_name, fps=fps, path=out_path, **params)
    return out_path


def text2video_api(_: gr.Blocks, app: FastAPI):
    @app.post("/sdapi/ai/v1/txt2video")
    async def text2video(
        prompt: str = Body("", title='prompt'),
        t0: int = Body(44, title='t0 value'),
        t1: int = Body(47, title='t1 value'),
        video_length: int = Body(8, title='video length'),
        fps: int = Body(4, title='video fps'),
        model_name: str = Body("", title='model name'),
    ):
        start_time = time.time()
        output_directory = "output/videos/"
        video_path = text2video_zero(prompt, t0=t0, t1=t1, video_length=video_length, fps=fps, output_directory=output_directory, model_name=model_name)
        end_time = time.time()
        server_process_time = end_time - start_time
        return {"server_process_time": server_process_time, "video_url": "file=" + output_directory + video_path}

try:
    import modules.script_callbacks as script_callbacks

    script_callbacks.on_app_started(text2video_api)
except:
    pass
