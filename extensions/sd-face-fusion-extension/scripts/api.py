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
        source_image: str = Body(title='source image location'),
        target_file: str = Body(title='target image or video file location'),
        target_image_name: str = Body("", title='target image name including extension')
        target_video_name: str = Body("", title='target video name including extension')
    ):
        #  Source image must be a image
        if is_image(source_image):
            facefusion.globals.source_path = source_image
        else:
            facefusion.globals.source_path = None
            raise HTTPException(status_code=404, detail="Source Image not found.")

        output_dir = "/home/sduser/stable-diffusion-webui/output"
        output_dir_video = output_dir + "/videos"
            
        if is_image(target_file):
            facefusion.globals.target_path = target_file
            return start(output_dir)
            
        if is_video(target_file):
            facefusion.globals.target_path = target_file
            return start(output_dir_video)

        # for testing setting it same. But this output directory should be replaced by our templates location
        target_image_path = output_dir + target_image_name
        target_video_path = output_dir_video + target_video_name

        if target_image_name != "" and is_image(target_image_path):
            facefusion.globals.target_path = target_image_path
            return start(output_dir)

        if target_video_name != "" and is_video(target_video_path):
            facefusion.globals.target_path = target_video_path
            return start(output_dir_video)
        
        raise HTTPException(status_code=404, detail="Target Image or Video not found")



try:
    import modules.script_callbacks as script_callbacks
    script_callbacks.on_app_started(facefusion_api)
    
except:
    pass
