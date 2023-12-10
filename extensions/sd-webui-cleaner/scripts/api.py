from fastapi import FastAPI, Body

from modules.api.models import *
from modules.api import api
import gradio as gr

from scripts import lama
from modules.shared import opts,OptionInfo
from datetime import datetime, timezone

import time


def cleanup_api(_: gr.Blocks, app: FastAPI):

    @app.post("/sdwebui/ai/cleanup")
    def clean_up(
        input_image: str = Body("", title='cleanup input image'),
        mask: str = Body("", title='clean up mask')
    ):

        _image = api.decode_base64_to_image(input_image)
        _mask = api.decode_base64_to_image(mask)

        start_time = time.time()
        utc_time = datetime.now(timezone.utc)
        _output = lama.clean_object(_image, _mask)
        output_img = api.encode_pil_to_base64(_output[0]).decode("utf-8")
        
        if len(_output) > 0:
            return {"server_process_time": time.time()-start_time, "image": output_img, "server_hit_time": utc_time}
        else:
            return {"code": -1, "message": "Image generation failed"}


try:
    import modules.script_callbacks as script_callbacks

    script_callbacks.on_app_started(cleanup_api)
except:
    pass
