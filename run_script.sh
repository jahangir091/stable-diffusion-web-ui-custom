#!/usr/bin/env bash
#################################################
#script Installation of sd web ui
# 1. Use docker image: pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime
# 2. Open terminal and download the run_script.sh file: wget https://raw.githubusercontent.com/jahangir091/stable-diffusion-web-ui-custom/master/run_script.sh
# 3. chmod +x run_script.sh
# 4. just run ./runscript.sh install
#    or ./runscript.sh start
#Voila
#** The project files can be found here: /home/sduser/

#################################################

#function for preparing environment for the first time
prepare_installation(){
  delemeter1="\n************************ Updating system packages *************************************************\n\n"
  delemeter2="\n************************ Installing nvtop & vim *****************************************************\n"
  delemeter3="\n************************ Installing libgl1 & libglib2.0-0 *******************************************\n"
  delemeter4="\n************************ Installing git-lfs *********************************************************\n"
  delemeter5="\n************************ Set write permission to /tmp directory *************************************\n"
  delemeter6="\n************************ Adding new user 'sduser' ***************************************************\n"
  delemeter7="\n************************ cd to directory 'sduser' ***************************************************\n"
  delemeter8="\n************************ Download installation files webui.sh & webui-user.sh  **********************\n"
  delemeter9="\n************************ Setting permissions to installation files **********************************\n"
  delemeter10="\n************************ Removeing ffmpeg if exist in conda **********************************\n"
  delemeter11="\n************************ Setting up Nginx **********************************\n"
  delemeter12="\n************************ Started Nginx at port: 8005 **********************************\n"


  printf "\n%s\n" "${delemeter1}"
  apt update -y
  apt upgrade -y

  printf "\n%s\n" "${delemeter10}"
  conda remove ffmpeg -y

  printf "\n%s\n" "${delemeter2}"
  apt install nvtop vim -y

  printf "\n%s\n" "${delemeter3}"
  apt install libgl1 libglib2.0-0 ffmpeg gcc build-essential nginx -y

  printf "\n%s\n" "${delemeter4}"
  cmd=$(curl -v -H -s "A: B" curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash)
  apt install git-lfs -y
  git lfs install

  printf "\n%s\n" "${delemeter5}"
  chmod 777 -R /tmp


  cd
  cd /home/

  printf "\n%s\n" "${delemeter6}"
  useradd -m sduser -p 'sduser' -s /bin/bash

  printf "\n%s\n" "${delemeter7}"
  cd sduser

  rm -f webui.sh
  rm -f webui-user.sh
  rm -rf stable-diffusion-webui

  printf "\n%s\n" "${delemeter8}"
  wget -q https://raw.githubusercontent.com/jahangir091/stable-diffusion-web-ui-custom/master/webui.sh
  wget -q https://raw.githubusercontent.com/jahangir091/stable-diffusion-web-ui-custom/master/webui-user.sh
  wget https://raw.githubusercontent.com/jahangir091/stable-diffusion-web-ui-custom/master/nginx_settings.conf -P /etc/nginx/sites-available/

  printf "\n%s\n" "${delemeter9}"
  chmod +x webui.sh
  chmod +x webui-user.sh

  printf "\n%s\n" "${delemeter11}"
  ln -s /etc/nginx/sites-available/nginx_settings.conf /etc/nginx/sites-enabled/
  service nginx start
  service nginx restart
}

start_webui(){
  printf "**********************************************************************************************************\n"
  printf "******************************                              ***********************************************\n"
  printf "****************************** THE MAIN ACTION STARTED HERE ***********************************************\n"
  printf "******************************      INSTALLING SD-WEBUI     **********************************************\n"
  printf "******************************           PLEASE WAIT        **********************************************\n"
  printf "**********************************************************************************************************\n"
  printf "**********************************************************************************************************\n"
  printf "**********************************************************************************************************\n"
  cd
  cd /home/
  cd sduser
  pip install --upgrade pip
  runuser -u sduser ./webui.sh
}


#main execution entry point
install="install"
start="start"

if [ "$1" == "$start" ]
then
  start_webui
elif [ "$1" == "$install" ]
then
  prepare_installation
  start_webui
else
  printf "\n\n expected flags 'install' or 'start' \n\n"
fi
