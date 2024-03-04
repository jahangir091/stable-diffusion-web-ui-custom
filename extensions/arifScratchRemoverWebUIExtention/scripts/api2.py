from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from fastapi import File, UploadFile, Form
import gradio as gr
import time
from datetime import datetime, timezone
from pipeline_stable_diffusion_controlnet_inpaint import *
from scratch_detection import ScratchDetection, ScratchDetectionNew
from diffusers import ControlNetModel, DEISMultistepScheduler
from arif_install import downloadScratchRemoverModel
from PIL import Image
import cv2
import glob
import shutil
import os
from os.path import exists
import subprocess
import base64
from io import BytesIO
import numpy
from sympy import true, false

# new
from modules.api.models import *
from modules.api import api
from modules.api import models
from modules import sd_samplers, deepbooru, sd_hijack, images, scripts, ui, postprocessing, errors, restart, \
    shared_items, postprocessing
from typing_extensions import Literal

import uuid


def get_img_path(directory_name):
    current_dir = '/tmp'
    img_directory = current_dir + '/.temp' + directory_name
    os.makedirs(img_directory, exist_ok=True)
    img_file_name = uuid.uuid4().hex[:20] + '.jpg'
    return img_directory + img_file_name


device = "cuda"

# load control net and stable diffusion v1-5
controlnet = ControlNetModel.from_pretrained("thepowefuldeez/sd21-controlnet-canny", torch_dtype=torch.float16)

pipe = StableDiffusionControlNetInpaintPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-inpainting", controlnet=controlnet, torch_dtype=torch.float16
)

pipe.scheduler = DEISMultistepScheduler.from_config(pipe.scheduler.config)

# speed up diffusion process with faster scheduler and memory optimization
# remove following line if xformers is not installed
# pipe.enable_xformers_memory_efficient_attention()
pipe.to('cuda')


def scratch_remove_api(_: gr.Blocks, app: FastAPI):
    @app.post('/sdapi/ai/v1/scratch_remove_new')
    async def generate_mask_image(
            input_image: str = Body("", title='scratch remove input image'),
            upscale: bool = Body(False, title='input image name')
    ):
        start_time = time.time()

        downloadScratchRemoverModelModel()
        pil_image = api.decode_base64_to_image(input_image).convert("RGB")
        out_image = remove_scratch_using_mask(pil_image, upscale)

        out_images_directory_name = '/scratch_images/'

        out_image_path = get_img_path(out_images_directory_name)
        out_image.save(out_image_path)

        return {
            "success": True,
            "message": "Returned output successfully",
            "server_process_time": time.time() - start_time,
            "output_image_urls": '/media' + out_images_directory_name + out_image_path.split('/')[-1]
        }

    def remove_scratch_using_mask(source_image: Image, upscale: bool):
        start_time = time.time()
        # curDir = os.getcwd()
        # fileName = "arif.png"

        # input_path = curDir + "/extensions/arifScratchRemoverWebUIExtention/input_images"
        # output_dir = curDir + "/extensions/arifScratchRemoverWebUIExtention/output_masks"

        # remove previous image from output directory
        # remove_all_file_in_dir(folder=("%s/*" % input_path))
        # remove_all_file_in_dir(folder=(curDir + "/extensions/arifScratchRemoverWebUIExtention/output_masks/mask/*"))
        # remove_all_file_in_dir(folder=(curDir + "/extensions/arifScratchRemoverWebUIExtention/output_masks/input/*"))

        # Save the input image to a directory
        # source_file_location = input_path + "/" + fileName
        # image = source_image.save(f"{source_file_location}")

        scratch_detector = ScratchDetectionNew(source_image, input_size="scale_256", gpu=0)
        main_image, mask_image = scratch_detector.run()
        # mask_image = scratch_detector.get_mask_image(fileName)

        # Resize the mask to match the input image size
        mask_image = mask_image.resize(mask_image.size, Image.BICUBIC)

        # Apply dilation to make the lines bigger
        kernel = np.ones((5, 5), np.uint8)
        mask_image_np = np.array(mask_image)
        mask_image_np_dilated = cv2.dilate(mask_image_np, kernel, iterations=2)
        mask_image_dilated = Image.fromarray(mask_image_np_dilated)

        ##scratck removing
        # main_image_dir = curDir + "/extensions/arifScratchRemoverWebUIExtention/output_masks/input/" + fileName
        # main_image = Image.open(main_image_dir).convert("RGB")
        main_image = main_image.convert("RGB")
        main_image = resize_image(main_image, 768)

        main_mask = mask_image_dilated
        main_mask = resize_image(main_mask, 768)

        image = np.array(main_image)
        low_threshold = 100
        high_threshold = 200
        canny = cv2.Canny(image, low_threshold, high_threshold)
        canny = canny[:, :, None]
        canny = np.concatenate([canny, canny, canny], axis=2)
        canny_image = Image.fromarray(canny)
        generator = torch.manual_seed(0)

        without_scratch_Image_output = pipe(
            prompt="",
            num_inference_steps=20,
            generator=generator,
            image=main_image,
            control_image=canny_image,
            controlnet_conditioning_scale=0,
            mask_image=main_mask
        ).images[0]
        # return base64 image
        if upscale == False:
            return without_scratch_Image_output

        args = scripts.scripts_postproc.create_args_for_run({
            "Upscale": {
                "upscale_mode": 0,
                "upscale_by": 1,
                "upscale_to_width": 512,
                "upscale_to_height": 512,
                "upscale_crop": True,
                "upscaler_1_name": "R-ESRGAN 4x+",
                "upscaler_2_name": "None",
                "upscaler_2_visibility": 0,
            },
            "GFPGAN": {
                "gfpgan_visibility": 1,
            },
            "CodeFormer": {
                "codeformer_visibility": 0.75,
                "codeformer_weight": 0,
            },
        })

        result = postprocessing.run_postprocessing(0, without_scratch_Image_output, "", "", "", True, *args,
                                                   save_output=False)
        # img_str = api.encode_pil_to_base64(result[0][0])
        print(result[0][0])
        return result[0][0]

    def save_file(file: UploadFile, path: str):
        with open(path, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)

    def resize_image(image, target_size):
        width, height = image.size
        aspect_ratio = float(width) / float(height)
        if width > height:
            new_width = target_size
            new_height = int(target_size / aspect_ratio)
        else:
            new_width = int(target_size * aspect_ratio)
            new_height = target_size
        return image.resize((new_width, new_height), Image.BICUBIC)

    def remove_all_file_in_dir(folder):
        # '/YOUR/PATH/*'
        files = glob.glob(folder)
        for f in files:
            os.remove(f)

    def downloadScratchRemoverModelModel():
        curDir = os.getcwd()
        model_name = "FT_Epoch_latest.pt"
        model_dir = curDir + "/extensions/arifScratchRemoverWebUIExtention/"
        model_path = model_dir + model_name

        if exists(model_path):
            print("model already downloaded")
            return
        else:
            command_str = "wget https://www.dropbox.com/s/5jencqq4h59fbtb/FT_Epoch_latest.pt" + " -P " + model_dir
            runcmd(command_str, verbose=True)
            print("model downloaded done")

        # new
        upscaleDir = curDir + "/extensions/arifScratchRemoverWebUIExtention/Bringing-Old-Photos-Back-to-Life/"
        check_file = "/extensions/arifScratchRemoverWebUIExtention/Bringing-Old-Photos-Back-to-Life/Global/global_checkpoints.zip"
        if exists(check_file):
            print("all MS upscale already downloaded")
            return
        else:
            shDir = upscaleDir + "download-weights.sh"
            command_str = "sudo chmod +x " + shDir + " " + upscaleDir
            runcmd(command_str, verbose=True)
            print("all MS scr model downloaded done")

    def runcmd(cmd, verbose=False, *args, **kwargs):

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
        std_out, std_err = process.communicate()
        if verbose:
            print(std_out.strip(), std_err)
        pass


try:
    import modules.script_callbacks as script_callbacks

    script_callbacks.on_app_started(scratch_remove_api)

except:
    pass
