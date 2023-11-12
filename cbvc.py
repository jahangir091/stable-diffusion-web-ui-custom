################################################################
Launching launch.py...
################################################################
Cannot locate TCMalloc (improves CPU memory usage)
initial startup: done in 0.001s
  prepare environment:
  checks: done in 0.000s
fatal: No names found, cannot describe anything.
  git version info: done in 0.005s
Python 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0]
Version: 1.6.1
Commit hash: 0b47da59bfc65dd35930e753d96370854e36c517
Installing torch and torchvision
Looking in indexes: https://pypi.org/simple, https://download.pytorch.org/whl/cu118
Requirement already satisfied: torch==2.0.1 in ./venv/lib/python3.10/site-packages (2.0.1+cu118)
Requirement already satisfied: torchvision==0.15.2 in ./venv/lib/python3.10/site-packages (0.15.2+cu118)
Requirement already satisfied: typing-extensions in ./venv/lib/python3.10/site-packages (from torch==2.0.1) (4.8.0)
Requirement already satisfied: filelock in ./venv/lib/python3.10/site-packages (from torch==2.0.1) (3.13.1)
Requirement already satisfied: jinja2 in ./venv/lib/python3.10/site-packages (from torch==2.0.1) (3.1.2)
Requirement already satisfied: sympy in ./venv/lib/python3.10/site-packages (from torch==2.0.1) (1.12)
Requirement already satisfied: triton==2.0.0 in ./venv/lib/python3.10/site-packages (from torch==2.0.1) (2.0.0)
Requirement already satisfied: networkx in ./venv/lib/python3.10/site-packages (from torch==2.0.1) (3.2.1)
Requirement already satisfied: numpy in ./venv/lib/python3.10/site-packages (from torchvision==0.15.2) (1.23.5)
Requirement already satisfied: requests in ./venv/lib/python3.10/site-packages (from torchvision==0.15.2) (2.31.0)
Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in ./venv/lib/python3.10/site-packages (from torchvision==0.15.2) (9.5.0)
Requirement already satisfied: cmake in ./venv/lib/python3.10/site-packages (from triton==2.0.0->torch==2.0.1) (3.27.7)
Requirement already satisfied: lit in ./venv/lib/python3.10/site-packages (from triton==2.0.0->torch==2.0.1) (17.0.4)
Requirement already satisfied: MarkupSafe>=2.0 in ./venv/lib/python3.10/site-packages (from jinja2->torch==2.0.1) (2.1.3)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./venv/lib/python3.10/site-packages (from requests->torchvision==0.15.2) (2.0.7)
Requirement already satisfied: certifi>=2017.4.17 in ./venv/lib/python3.10/site-packages (from requests->torchvision==0.15.2) (2023.7.22)
Requirement already satisfied: idna<4,>=2.5 in ./venv/lib/python3.10/site-packages (from requests->torchvision==0.15.2) (3.4)
Requirement already satisfied: charset-normalizer<4,>=2 in ./venv/lib/python3.10/site-packages (from requests->torchvision==0.15.2) (3.3.2)
Requirement already satisfied: mpmath>=0.19 in ./venv/lib/python3.10/site-packages (from sympy->torch==2.0.1) (1.3.0)

[notice] A new release of pip is available: 23.0.1 -> 23.3.1
[notice] To update, run: pip install --upgrade pip
  install torch: done in 2.198s
  torch GPU test: done in 1.347s
  clone repositores: done in 0.021s
Installing requirements
  install requirements: done in 9.758s
    run extensions installers:
2023-11-12 18:12:05 DEBUG [root] Installing StyleSelector-XL
    StyleSelector-XL: done in 0.000s
2023-11-12 18:12:05 DEBUG [root] Installing Text2Video-Zero-sd-webui
no module 'xformers'. Processing without...
no module 'xformers'. Processing without...
No module 'xformers'. Proceeding without it.
Installing requirements for Text2Video-Zero
    Text2Video-Zero-sd-webui: done in 13.045s
2023-11-12 18:12:18 DEBUG [root] Installing put extensions here.txt
2023-11-12 18:12:18 DEBUG [root] Installing stable-diffusion-webui-rembg
    stable-diffusion-webui-rembg: done in 0.053s
Launching Web UI with arguments: --listen --port 8001 --api --enable-insecure-extension-access --reinstall-torch --loglevel DEBUG --api-log --log-startup
launcher: done in 0.001s
import torch: done in 1.061s
2023-11-12 18:12:20 DEBUG [matplotlib] matplotlib data path: /home/sduser/stable-diffusion-webui/venv/lib/python3.10/site-packages/matplotlib/mpl-data
2023-11-12 18:12:20 DEBUG [matplotlib] CONFIGDIR=/home/sduser/.config/matplotlib
2023-11-12 18:12:20 DEBUG [matplotlib] interactive is False
2023-11-12 18:12:20 DEBUG [matplotlib] platform is linux
2023-11-12 18:12:20 DEBUG [matplotlib] CACHEDIR=/home/sduser/.cache/matplotlib
2023-11-12 18:12:20 DEBUG [matplotlib.font_manager] Using fontManager instance from /home/sduser/.cache/matplotlib/fontlist-v330.json
import torch: done in 1.304s
2023-11-12 18:12:21 DEBUG [httpx] load_ssl_context verify=True cert=None trust_env=True http2=False
2023-11-12 18:12:21 DEBUG [httpx] load_verify_locations cafile='/home/sduser/stable-diffusion-webui/venv/lib/python3.10/site-packages/certifi/cacert.pem'
2023-11-12 18:12:21 DEBUG [httpx] load_ssl_context verify=True cert=None trust_env=True http2=False
2023-11-12 18:12:21 DEBUG [httpx] load_verify_locations cafile='/home/sduser/stable-diffusion-webui/venv/lib/python3.10/site-packages/certifi/cacert.pem'
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing BlpImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing BmpImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing BufrStubImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing CurImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing DcxImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing DdsImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing EpsImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing FitsImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing FitsStubImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing FliImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing FpxImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Image: failed to import FpxImagePlugin: No module named 'olefile'
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing FtexImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing GbrImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing GifImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing GribStubImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing Hdf5StubImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing IcnsImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing IcoImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing ImImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing ImtImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing IptcImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing JpegImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing Jpeg2KImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing McIdasImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing MicImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Image: failed to import MicImagePlugin: No module named 'olefile'
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing MpegImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing MpoImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing MspImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing PalmImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing PcdImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing PcxImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing PdfImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing PixarImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing PngImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing PpmImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing PsdImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing QoiImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing SgiImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing SpiderImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing SunImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing TgaImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing TiffImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing WebPImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing WmfImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing XbmImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing XpmImagePlugin
2023-11-12 18:12:21 DEBUG [PIL.Image] Importing XVThumbImagePlugin
import gradio: done in 0.579s
no module 'xformers'. Processing without...
no module 'xformers'. Processing without...
setup paths: done in 0.582s
import ldm: done in 0.004s
import sgm: done in 0.000s
No module 'xformers'. Proceeding without it.
2023-11-12 18:12:22 DEBUG [git.cmd] Popen(['git', 'version'], cwd=/home/sduser/stable-diffusion-webui, universal_newlines=False, shell=None, istream=None)
2023-11-12 18:12:22 DEBUG [git.cmd] Popen(['git', 'version'], cwd=/home/sduser/stable-diffusion-webui, universal_newlines=False, shell=None, istream=None)
initialize shared: done in 0.130s
other imports: done in 0.421s
opts onchange: done in 0.000s
setup SD model: done in 0.000s
setup codeformer: done in 0.081s
setup gfpgan: done in 0.008s
set samplers: done in 0.000s
list extensions: done in 0.000s
restore config state file: done in 0.000s
list SD models: done in 0.000s
list localizations: done in 0.000s
  load scripts:
  custom_code.py: done in 0.001s
  img2imgalt.py: done in 0.000s
  loopback.py: done in 0.000s
  outpainting_mk_2.py: done in 0.000s
  poor_mans_outpainting.py: done in 0.000s
  postprocessing_codeformer.py: done in 0.000s
  postprocessing_gfpgan.py: done in 0.000s
  postprocessing_upscale.py: done in 0.000s
  prompt_matrix.py: done in 0.000s
  prompts_from_file.py: done in 0.000s
  refiner.py: done in 0.000s
  sd_upscale.py: done in 0.000s
  seed.py: done in 0.000s
  xyz_grid.py: done in 0.002s
  StyleSelectorXL.py: done in 0.337s
  __init__.py: done in 0.000s
cuda
cuda
  api.py: done in 3.756s
  main.py: done in 0.027s
  api.py: done in 0.550s
  postprocessing_rembg.py: done in 0.000s
  ldsr_model.py: done in 0.026s
  lora_script.py: done in 0.148s
  scunet_model.py: done in 0.025s
  swinir_model.py: done in 0.025s
  hotkey_config.py: done in 0.000s
  extra_options_section.py: done in 0.000s
load upscalers: done in 0.001s
refresh VAE: done in 0.001s
refresh textual inversion templates: done in 0.000s
scripts list_optimizers: done in 0.000s
scripts list_unets: done in 0.000s
Loading weights [6ce0161689] from /home/sduser/stable-diffusion-webui/models/Stable-diffusion/v1-5-pruned-emaonly.safetensors
reload hypernetworks: done in 0.003s
initialize extra networks: done in 0.008s
scripts before_ui_callback: done in 0.001s
2023-11-12 18:12:28 DEBUG [urllib3.connectionpool] Starting new HTTPS connection (1): huggingface.co:443
Creating model from config: /home/sduser/stable-diffusion-webui/configs/v1-inference.yaml
Applying attention optimization: Doggettx... done.
Model loaded in 2.2s (load weights from disk: 0.7s, create model: 0.3s, apply weights to model: 1.0s).
2023-11-12 18:12:33 DEBUG [urllib3.connectionpool] https://huggingface.co:443 "GET /models?p=0&sort=downloads&search=dreambooth HTTP/1.1" 200 None
2023-11-12 18:12:33 DEBUG [urllib3.connectionpool] Starting new HTTPS connection (1): huggingface.co:443
2023-11-12 18:12:38 DEBUG [urllib3.connectionpool] https://huggingface.co:443 "GET /models?p=1&sort=downloads&search=dreambooth HTTP/1.1" 200 None
2023-11-12 18:12:38 DEBUG [urllib3.connectionpool] Starting new HTTPS connection (1): huggingface.co:443
2023-11-12 18:12:44 DEBUG [urllib3.connectionpool] https://huggingface.co:443 "GET /models?p=2&sort=downloads&search=dreambooth HTTP/1.1" 200 None
2023-11-12 18:12:44 DEBUG [urllib3.connectionpool] Starting new HTTPS connection (1): huggingface.co:443
2023-11-12 18:12:49 DEBUG [urllib3.connectionpool] https://huggingface.co:443 "GET /models?p=3&sort=downloads&search=dreambooth HTTP/1.1" 200 None
2023-11-12 18:12:49 DEBUG [urllib3.connectionpool] Starting new HTTPS connection (1): huggingface.co:443
2023-11-12 18:12:55 DEBUG [urllib3.connectionpool] https://huggingface.co:443 "GET /models?p=4&sort=downloads&search=dreambooth HTTP/1.1" 200 None
2023-11-12 18:12:55 DEBUG [asyncio] Using selector: EpollSelector
/home/sduser/stable-diffusion-webui/extensions/Text2Video-Zero-sd-webui/app_pix2pix_video.py:37: GradioDeprecationWarning: The `style` method is deprecated. Please set these arguments in the constructor instead.
  input_image = gr.Video(label="Input Video", source='upload',
/home/sduser/stable-diffusion-webui/extensions/Text2Video-Zero-sd-webui/app_pose.py:24: GradioDeprecationWarning: The `style` method is deprecated. Please set these arguments in the constructor instead.
  gallery_pose_sequence = gr.Gallery(label="Pose Sequence", value=[('extensions/Text2Video-Zero-sd-webui/__assets__/poses_skeleton_gifs/dance1.gif', "Motion 1"), ('extensions/Text2Video-Zero-sd-webui/__assets__/poses_skeleton_gifs/dance2.gif', "Motion 2"), (
/home/sduser/stable-diffusion-webui/extensions/Text2Video-Zero-sd-webui/app_pose.py:24: GradioDeprecationWarning: The 'grid' parameter will be deprecated. Please use 'columns' in the constructor instead.
  gallery_pose_sequence = gr.Gallery(label="Pose Sequence", value=[('extensions/Text2Video-Zero-sd-webui/__assets__/poses_skeleton_gifs/dance1.gif', "Motion 1"), ('extensions/Text2Video-Zero-sd-webui/__assets__/poses_skeleton_gifs/dance2.gif', "Motion 2"), (
/home/sduser/stable-diffusion-webui/extensions/Text2Video-Zero-sd-webui/app_canny.py:41: GradioDeprecationWarning: The `style` method is deprecated. Please set these arguments in the constructor instead.
  input_video = gr.Video(
/home/sduser/stable-diffusion-webui/extensions/Text2Video-Zero-sd-webui/app_canny.py:56: GradioDeprecationWarning: The `style` method is deprecated. Please set these arguments in the constructor instead.
  result = gr.Video(label="Generated Video").style(height="auto")
/home/sduser/stable-diffusion-webui/extensions/Text2Video-Zero-sd-webui/app_canny_db.py:60: GradioDeprecationWarning: The `style` method is deprecated. Please set these arguments in the constructor instead.
  result = gr.Image(label="Generated Video").style(height=400)
/home/sduser/stable-diffusion-webui/extensions/Text2Video-Zero-sd-webui/app_canny_db.py:63: GradioDeprecationWarning: The `style` method is deprecated. Please set these arguments in the constructor instead.
  gallery_db = gr.Gallery(label="Db models", value=[('extensions/Text2Video-Zero-sd-webui/__assets__/db_files/anime.jpg', "anime"), ('extensions/Text2Video-Zero-sd-webui/__assets__/db_files/arcane.jpg', "Arcane"), (
/home/sduser/stable-diffusion-webui/extensions/Text2Video-Zero-sd-webui/app_canny_db.py:63: GradioDeprecationWarning: The 'grid' parameter will be deprecated. Please use 'columns' in the constructor instead.
  gallery_db = gr.Gallery(label="Db models", value=[('extensions/Text2Video-Zero-sd-webui/__assets__/db_files/anime.jpg', "anime"), ('extensions/Text2Video-Zero-sd-webui/__assets__/db_files/arcane.jpg', "Arcane"), (
/home/sduser/stable-diffusion-webui/extensions/Text2Video-Zero-sd-webui/app_canny_db.py:66: GradioDeprecationWarning: The `style` method is deprecated. Please set these arguments in the constructor instead.
  gallery_canny = gr.Gallery(label="Motions", value=[('extensions/Text2Video-Zero-sd-webui/__assets__/db_files/woman1.gif', "woman1"), ('extensions/Text2Video-Zero-sd-webui/__assets__/db_files/woman2.gif', "woman2"), (
/home/sduser/stable-diffusion-webui/extensions/Text2Video-Zero-sd-webui/app_canny_db.py:66: GradioDeprecationWarning: The 'grid' parameter will be deprecated. Please use 'columns' in the constructor instead.
  gallery_canny = gr.Gallery(label="Motions", value=[('extensions/Text2Video-Zero-sd-webui/__assets__/db_files/woman1.gif', "woman1"), ('extensions/Text2Video-Zero-sd-webui/__assets__/db_files/woman2.gif', "woman2"), (
/home/sduser/stable-diffusion-webui/extensions/Text2Video-Zero-sd-webui/app_depth.py:41: GradioDeprecationWarning: The `style` method is deprecated. Please set these arguments in the constructor instead.
  input_video = gr.Video(
/home/sduser/stable-diffusion-webui/extensions/Text2Video-Zero-sd-webui/app_depth.py:56: GradioDeprecationWarning: The `style` method is deprecated. Please set these arguments in the constructor instead.
  result = gr.Video(label="Generated Video").style(height="auto")
create ui: done in 27.879s
2023-11-12 18:12:55 DEBUG [asyncio] Using selector: EpollSelector
2023-11-12 18:12:56 DEBUG [httpx] load_ssl_context verify=None cert=None trust_env=True http2=False
Running on local URL:  http://0.0.0.0:8001
2023-11-12 18:12:56 DEBUG [urllib3.connectionpool] Starting new HTTP connection (1): localhost:8001
2023-11-12 18:12:56 DEBUG [urllib3.connectionpool] http://localhost:8001 "GET /startup-events HTTP/1.1" 200 5
2023-11-12 18:12:56 DEBUG [urllib3.connectionpool] Starting new HTTP connection (1): localhost:8001
2023-11-12 18:12:56 DEBUG [urllib3.connectionpool] http://localhost:8001 "HEAD / HTTP/1.1" 200 0

To create a public link, set `share=True` in `launch()`.
gradio launch: done in 0.347s
add APIs: done in 0.097s
  app_started_callback:
  api.py: done in 0.001s
  api.py: done in 0.001s
  lora_script.py: done in 0.000s
Startup time: 63.8s (prepare environment: 26.4s, import torch: 2.4s, import gradio: 0.6s, setup paths: 0.6s, initialize shared: 0.1s, other imports: 0.4s, load scripts: 4.9s, create ui: 27.9s, gradio launch: 0.3s).
