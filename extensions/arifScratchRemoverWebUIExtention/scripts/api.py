from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from fastapi import File, UploadFile, Form
import gradio as gr
import time
from datetime import datetime, timezone
from pipeline_stable_diffusion_controlnet_inpaint import *
from scratch_detection import ScratchDetection
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
import  numpy

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
    @app.post('/sdapi/ai/v1/scratchRemove/downloadModel')
    async def download_model(
    ):
        #  Source image must be an image
        utc_time = datetime.now(timezone.utc)
        start_time = time.time()

        downloadScratchRemoverModel()

        end_time = time.time()
        server_process_time = end_time - start_time

        return {
            "model_download_time": server_process_time
        }

    @app.post('/sdapi/ai/v1/scratch_remove')
    async def generate_mask_image(
            source_image: UploadFile = File()
    ):
        utc_time = datetime.now(timezone.utc)
        start_time = time.time()

        downloadScratchRemoverModelModel()
        image_base64_str = remove_scratch_using_mask(source_image)

        end_time = time.time()
        server_process_time = end_time - start_time
        return {
            "server_hit_time": str(utc_time),
            "server_process_time": server_process_time,
            "output_image": image_base64_str
        }

    def remove_scratch_using_mask(source_image: UploadFile):
        curDir = os.getcwd()
        # input_dir = curDir + "/extensions/arifScratchRemoverWebUIExtention/Arif/"

        fileName = source_image.filename
        filename_without_extention = os.path.splitext(fileName)[0]

        # source_file_location = input_dir + source_image.filename
        # save_file(source_image, source_file_location)
        # input_image = PIL.Image.open(source_file_location).convert('RGB')
        # input_image = PIL.Image.open(img_p).convert('RGB')

        input_path = curDir + "/extensions/arifScratchRemoverWebUIExtention/input_images"
        output_dir = curDir + "/extensions/arifScratchRemoverWebUIExtention/output_masks"

        # remove previous image from output directory
        remove_all_file_in_dir(folder=("%s/*" % input_path))
        remove_all_file_in_dir(folder=(curDir + "/extensions/arifScratchRemoverWebUIExtention/output_masks/mask/*"))
        remove_all_file_in_dir(folder=(curDir + "/extensions/arifScratchRemoverWebUIExtention/output_masks/input/*"))

        # Save the input image to a directory
        source_file_location = input_path + "/" + fileName
        save_file(source_image, source_file_location)

        # remove_all_file_in_dir(folder=("%s/*" % input_path))
        # input_image_path = (f'{input_path}/{fileName}')
        # # input_image_resized = resize_image(input_image, 768)
        # input_image.save(input_image_path)

        scratch_detector = ScratchDetection(input_path, output_dir, input_size="scale_256", gpu=0)
        scratch_detector.run()

        pngExt = '.png'
        mask_image = scratch_detector.get_mask_image((filename_without_extention + pngExt))

        # Resize the mask to match the input image size
        mask_image = mask_image.resize(mask_image.size, Image.BICUBIC)

        # Apply dilation to make the lines bigger
        kernel = np.ones((5, 5), np.uint8)
        mask_image_np = np.array(mask_image)
        mask_image_np_dilated = cv2.dilate(mask_image_np, kernel, iterations=2)
        mask_image_dilated = Image.fromarray(mask_image_np_dilated)


        ##scratck removing

        main_image_dir = curDir + "/extensions/arifScratchRemoverWebUIExtention/output_masks/input/" + filename_without_extention + pngExt
        main_image = Image.open(main_image_dir).convert("RGB")
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


        #return base64 image
        opencvImage = cv2.cvtColor(numpy.array(without_scratch_Image_output), cv2.COLOR_RGB2BGR)
        _, encoded_img = cv2.imencode('.jpg', opencvImage)
        img_str = base64.b64encode(encoded_img).decode("utf-8")
        return img_str

        # opencvImage = cv2.cvtColor(numpy.array(mask_image_dilated), cv2.COLOR_RGB2BGR)
        # buffered = BytesIO()
        # mask_image_dilated.save(buffered, format="JPEG")
        # img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        # return img_str

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
