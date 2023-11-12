#!/usr/bin/env bash
#################################################
#script Installation of sd web ui
# 1. Use docker image: pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime
# 2. Open terminal and download the run_script.sh file: wget https://raw.githubusercontent.com/jahangir091/stable-diffusion-web-ui-custom/master/run_script.sh
# 3. chmod +x run_script.sh
# 4. just run ./runscript.sh
#Voila
#** The project files can be found here: /home/sduser/

#################################################


printf "****************************** Updating system packages ***************************************************\n"
apt update -y
apt upgrade -y

printf "****************************** Installing nvtop & vim ******************************************************\n"
apt install nvtop vim -y


printf "****************************** Installing libgl1 & libglib2.0-0 ********************************************\n"
apt install libgl1 libglib2.0-0 -y

printf "****************************** Installing git-lfs **********************************************************\n"
cmd=$(curl -v -H -s "A: B" curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash)
apt install git-lfs -y
git lfs install


printf "****************************** Set write permission to /tmp directory **************************************\n"
sudo chmod 777 -R /tmp

cd
cd /home/

printf "****************************** Adding new user 'sduser' ***************************************************\n"
sudo useradd -m sduser -p 'sduser' -s /bin/bash


printf "****************************** cd to directory 'sduser' ***************************************************\n"
cd sduser


printf "***************************** Download installation files webui.sh & webui-user.sh  **********************\n"
wget -q https://raw.githubusercontent.com/jahangir091/stable-diffusion-web-ui-custom/master/webui.sh
wget -q https://raw.githubusercontent.com/jahangir091/stable-diffusion-web-ui-custom/master/webui-user.sh

printf "****************************** Setting permissions to installation files *********************************\n"
chmod +x webui.sh
chmod +x webui-user.sh

printf "**********************************************************************************************************\n"
printf "******************************                              ***********************************************\n"
printf "****************************** THE MAIN ACTION STARTED HERE ***********************************************\n"
printf "******************************      INSTALLING SD-WEBUI     **********************************************\n"
printf "******************************           PLEASE WAIT        **********************************************\n"
printf "**********************************************************************************************************\n"
printf "**********************************************************************************************************\n"
printf "**********************************************************************************************************\n"

runuser -u sduser ./webui.sh

#sleep infinity