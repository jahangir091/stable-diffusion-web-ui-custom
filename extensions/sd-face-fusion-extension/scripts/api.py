from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from fastapi import File, UploadFile, Form

from typing import List, Optional, Tuple
import gradio as gr

from modules.api import api

import facefusion.globals
from facefusion.utilities import is_image, is_video
from facefusion.uis.components.output import predict, start
 
from facefusion.uis.typing import Update
from facefusion.typing import Frame
from facefusion.vision import read_static_image, resize_frame_dimension 
from facefusion.face_analyser import get_many_faces

import os
import shutil
import time
import base64
import cv2



def facefusion_api(_: gr.Blocks, app: FastAPI):
    @app.post('/facefusion/faces')
    async def extract_face(
        source_image: UploadFile = File(),
        max_size: str = Form("200", title = "maximum size of the images")
    ):
        #  Source image must be an image
        start_time = time.time()
        
        curDir = os.getcwd()
        input_dir = curDir + "/output/input/"
        source_file_location = input_dir + source_image.filename
        save_file(source_image, source_file_location)

        static_image = read_static_image(source_file_location)
        faces = get_faces_frames(static_image)

        try:
            max_size_int = int(max_size)
        except ValueError:
            raise HTTPException(status_code=422, detail= "max_size couldn't be converted to integer")
        
        base64_faces = frames_to_base64(faces, max_size_int)
        os.remove(source_file_location)

        end_time = time.time()
        server_process_time = end_time - start_time
        
        return {
            "server_hit_time": start_time,
            "server_process_time": server_process_time, 
            "faces": base64_faces,
        }

    
    def frames_to_base64(frames, max_size: int):
        frames_b64 = []
        #  iterate frames and convert each of them to base64
        for frame in frames:
            resized_frame = resize_frame_dimension(frame, max_size, max_size)
            _, encoded_img = cv2.imencode('.jpg', resized_frame)
            frames_b64.append(base64.b64encode(encoded_img).decode("utf-8"))
        return frames_b64   


    def get_faces_frames(reference_frame : Frame) -> List[Frame]:
    	crop_frames = []
    	faces = get_many_faces(reference_frame)
    	for face in faces:
    		start_x, start_y, end_x, end_y = map(int, face['bbox'])
    		padding_x = int((end_x - start_x) * 0.25)
    		padding_y = int((end_y - start_y) * 0.25)
    		start_x = max(0, start_x - padding_x)
    		start_y = max(0, start_y - padding_y)
    		end_x = max(0, end_x + padding_x)
    		end_y = max(0, end_y + padding_y)
    		crop_frame = reference_frame[start_y:end_y, start_x:end_x]
    		crop_frames.append(crop_frame)
    	return crop_frames
        

    
    @app.post('/facefusion/video')
    async def facefusion_video(
        source_image: UploadFile = File(),
        target_video: UploadFile = File(None),
        target_video_name: str = Form("", title='target video name including extension')
    ):
        #  Source image must be an image
        start_time = time.time()
        
        curDir = os.getcwd()
        output_dir = curDir + "/output"
        output_video_dir = output_dir + "/videos"

        # Testing only..........this two directory should be update.
        input_dir = output_dir + "/input/"
        template_dir = output_dir + "/template/"
        
        source_file_location = input_dir + source_image.filename
        save_file(source_image, source_file_location)
        facefusion.globals.source_path = source_file_location

        if target_video_name == "":
            target_file_location = input_dir + target_video.filename
            save_file(target_video, target_file_location)
            facefusion.globals.target_path = target_file_location
        else:
            target_file_location = template_dir + target_video_name
            if is_video(target_file_location):
                facefusion.globals.target_path = target_file_location
            else:
                raise HTTPException(status_code=404, detail="Target Video not found.")
        
        isTemplate = True 
        if target_video_name == "":
            isTemplate = False
        
        video_path = process_face_fusion(output_video_dir, isTemplate)
        if video_path == None:
            raise HTTPException(status_code=502, detail="Couldn't process your request")
        
        end_time = time.time()
        server_process_time = end_time - start_time
        return {
            "server_hit_time": start_time,
            "server_process_time": server_process_time, 
            "url": "file=" + video_path
        }


    
    @app.post('/facefusion/image')
    async def facefusion_image(
        source_image: UploadFile = File(),
        target_image: UploadFile = File(None),
        target_image_name: str = Form("", title='target image name including extension')
    ):
        #  Source image must be an image
        start_time = time.time()
        
        curDir = os.getcwd()
        output_dir = curDir + "/output"

        # Testing only..........this two directory should be update.
        input_dir = output_dir + "/input/"
        template_dir = output_dir + "/template/"
        
        source_file_location = input_dir + source_image.filename
        save_file(source_image, source_file_location)
        facefusion.globals.source_path = source_file_location

        if target_image_name == "":
            target_file_location = input_dir + target_image.filename
            save_file(target_image, target_file_location)
            facefusion.globals.target_path = target_file_location
        else:
            target_file_location = template_dir + target_image_name
            if is_image(target_file_location):
                facefusion.globals.target_path = target_file_location
            else:
                raise HTTPException(status_code=404, detail="Target Image not found.")

        isTemplate = True 
        if target_image_name == "":
            isTemplate = False
        
        image_path = process_face_fusion(output_dir, isTemplate)
        if image_path == None:
            raise HTTPException(status_code=502, detail="Couldn't process your request")
        
        end_time = time.time()
        server_process_time = end_time - start_time
        return {
            "server_hit_time": start_time,
            "server_process_time": server_process_time, 
            "url": "file=" + image_path
        }

    

    def save_file(file: UploadFile, path: str):
        with open(path, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)  

    # isTemplate = True means this target data belongs to us. And should not be deleted
    def process_face_fusion(output_dir: str, isTemplate: bool):
        process_response = start(output_dir)

        # extracting relative file url
        file_path = None
        for response in process_response:
            if response["value"] != None:
                file_path = response["value"] 
                if file_path != None:
                    file_path = os.path.relpath(file_path, os.getcwd())

        # removing users data
        os.remove(facefusion.globals.source_path)
        facefusion.globals.source_path = None

        # only delete data if its not template ie, users data
        if not isTemplate:
            os.remove(facefusion.globals.target_path)
            facefusion.globals.target_path = None

        return file_path
        



try:
    import modules.script_callbacks as script_callbacks
    script_callbacks.on_app_started(facefusion_api)
    
except:
    pass
