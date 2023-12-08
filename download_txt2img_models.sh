#!/usr/bin/env bash

#download pretrained models for text2img inference

print "\n************************ Downloading models from huggingface *********************************************\n\n"
wget -nc -P /home/sduser/stable-diffusion-webui/models/Stable-diffusion https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0_0.9vae.safetensors
wget -nc -P /home/sduser/stable-diffusion-webui/models/Stable-diffusion https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/Models/AbyssOrangeMix3/AOM3B2_orangemixs.safetensors
wget -nc -P /home/sduser/stable-diffusion-webui/models/Stable-diffusion https://huggingface.co/dreamlike-art/dreamlike-anime-1.0/resolve/main/dreamlike-anime-1.0.safetensors
wget -nc -P /home/sduser/stable-diffusion-webui/models/Stable-diffusion https://huggingface.co/SG161222/RealVisXL_V2.0/resolve/main/RealVisXL_V2.0.safetensors
wget -nc -P /home/sduser/stable-diffusion-webui/models/Stable-diffusion https://huggingface.co/SG161222/Realistic_Vision_V3.0_VAE/resolve/main/Realistic_Vision_V3.0.safetensors
wget -nc -P /home/sduser/stable-diffusion-webui/models/Stable-diffusion https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0/resolve/main/dreamlike-photoreal-2.0.safetensors
wget -nc -P /home/sduser/stable-diffusion-webui/models/Stable-diffusion https://huggingface.co/sd-dreambooth-library/EpicMixVirtualRealismv6/resolve/main/EpicV6Realism.safetensors
wget -nc -P /home/sduser/stable-diffusion-webui/models/Stable-diffusion https://huggingface.co/Hypogauge/magicmix/resolve/main/majicmixRealistic_v6.safetensors

print "\n************************ Downloading models from civitai *************************************************\n\n"
wget -nc -O /home/sduser/stable-diffusion-webui/models/Stable-diffusion/Dreamshaper_SDXL.safetensors https://civitai.com/api/download/models/126688
wget -nc -O /home/sduser/stable-diffusion-webui/models/Stable-diffusion/Disney_Pixar_Cartoon.safetensors https://civitai.com/api/download/models/69832
wget -nc -O /home/sduser/stable-diffusion-webui/models/Stable-diffusion/AnimeArt.safetensors https://civitai.com/api/download/models/128592
