from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from fastapi import File, UploadFile

from typing import List
import gradio as gr

import facefusion.globals
from facefusion.utilities import is_image, is_video
from facefusion.uis.components.output import predict, start

import os


def facefusion_api(_: gr.Blocks, app: FastAPI):
    @app.post('/facefusion/image')
    async def facefusion_image(
        source_image: str,
        target_file: str
    ):
        if is_image(source_image):
            facefusion.globals.source_path = source_image
        else:
            facefusion.globals.source_path = None
            raise HTTPException(status_code=404, detail="Source Image not found")
            
        if is_image(target_file) or is_video(target_file):
            facefusion.globals.target_path = target_file
        else:
            facefusion.globals.target_path = None
            raise HTTPException(status_code=404, detail="Target not found")

        
        return start("/home/siam/output")

        # predict("/home/siam/output")
        
        # if is_image(facefusion.globals.output_path):
        #     return {
        #         "image": api.encode_pil_to_base64(outImg).decode("utf-8")
        #     }
        #     return FileResponse(facefusion.globals.output_path)
        # else:
        #     raise HTTPException(status_code=500, detail="Couldn't process your request")



try:
    import modules.script_callbacks as script_callbacks
    script_callbacks.on_app_started(facefusion_api)
    
except:
    pass
