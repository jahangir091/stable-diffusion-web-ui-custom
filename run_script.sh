#!/usr/bin/env bash
#################################################
# Please do not make any changes to this file,  #
# change the variables in webui-user.sh instead #
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