#!/usr/bin/env bash
#################################################
#script Installation of sd web ui
# 1. Use docker image: pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime
# 2. go to /home directory:
# 3. keep the run_script.sh file here
# 4. chmod +x run_script.sh
# 5. just run ./runscript.sh
#Voila
#################################################


apt update
apt upgrade
apt install nvtop vim
apt install libgl1 libglib2.0-0
cmd=$(curl -v -H -s "A: B" curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash)
apt install git-lfs
git lfs install
sudo chmod 777 -R /tmp
adduser sduser
cd sduser

wget -q https://raw.githubusercontent.com/jahangir091/stable-diffusion-web-ui-custom/master/webui.sh
wget -q https://raw.githubusercontent.com/jahangir091/stable-diffusion-web-ui-custom/master/webui-user.sh
chmod +x webui.sh
chmod +x webui-user.sh
runuser -u sduser ./webui.sh