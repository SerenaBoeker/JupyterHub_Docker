# JupyterHub Setup
## Prerequisites
In order to be able to deploy the dockerized JupyterHub, following prerequisites need to be met:
- Install NVIDIA drivers
- Install NVIDIA CUDA Toolkit
- Install Docker Engine
- Install NVIDIA Container Toolkit

--- 
  
### Install NVIDIA drivers
List all NVIDIA driver versions on the machine:

```
apt-cache search 'nvidia-driver-' | grep '^nvidia-driver-[[:digit:]]*'
apt-cache search 'nvidia-dkms-' | grep '^nvidia-dkms-[[:digit:]]*'
```

First update and install all updates:

```
sudo apt update
sudo apt upgrade
```

Install the drivers (change the driver and dkms version if needed):

```
sudo apt install nvidia-driver-530 nvidia-dkms-530
```

And reboot:

```
sudo reboot
```

### Install NVIDIA CUDA Toolkit
Install the NVIDIA CUDA Toolkit following the provided instruction from NVIDIA [here](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/).

### Install Docker Engine
Install the Docker Engine following the steps provided [here](https://docs.docker.com/engine/install/ubuntu/).

### Install NVIDIA Container Toolkit
Finally, in order for the docker containers to be able to access the GPU(s), the NVIDIA Container Toolkit needs to be installed. Follow the steps provided [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) to do so.

---

## Setting up Jupyterhub
First, clone this repository:
```
git clone https://git.uni-due.de/spseboek/JupyterHub_Docker.git 
```
You will probably need to update the server address in the `jupyterhub_config.py`. To do so, go to `JupyterHub_Docker/jupyterhub` and use your preferred editor to change the server address at line 17:
```
c.SSHAuthenticator.server_address = '192.168.0.177'       # the ip of the server
```
You might also need to change the admin user name in the `config` file as well.  

For example using the `nano` editor starting in the `home` directory of the supposed admin user `ncsadmin` :
```
cd JupyterHub_Docker/jupyterhub
sudo nano jupyterhub_config.py
```
Change the address at line 17, and the admin user name at lines 9, 28 and 29, then hit <kbd>CTRL+O</kbd> to save the changes and <kbd>CTRL+X</kbd> to exit. Check that the changes have been saved by viewing the config file with nano again. 

To get JupyterHub up and running, change directory to `JupyterHub_Docker` and start it using `docker compose` (optional argument `-d` to start in detached mode):
```
cd ..
sudo docker compose up
```
JupyterHub will then be available in browser at the provided server address, port `:8000`.

---
## Start JupyterHub on System Startup
The bash script `StartJupyterhub.sh` will be run automatically on startup and will start the JupyterHub. If needed, edit this script to the path of the `JupyterHub_Docker` folder. In the `JupyterHub_Docker` directory, we first need to grand it permissions to make it executable:
```
sudo chmod a+x StartJupyterhub.sh
```
Then, we need to create a Systemd service, which will start this script on startup. Copy the `Jupyterhub.service` file to `/etc/systemd/system`:
```
sudo cp /home/ncsadmin/JupyterHub_Docker/Jupyterhub.service /etc/systemd/system/
```
and also set the permissions of the file with:
```
sudo chmod 644 /etc/systemd/system/Jupyterhub.service
```
Lastly, enable the service:
```
systemctl enable Jupyterhub.service
```
Check that everything is working as intended by rebooting. Use:
```
systemctl status Jupyterhub.service
```


## Maintenance
### To Update the JupyterHub Config
In order for any subsequent changes to the `jupyterhub_config.py` file to take place, it is (probably - see note below) needed to (in this order):

| Steps | Commands |
| --- | --- |
| remove the jupyterhub-container | ``` sudo docker rm jupyterhub-container ``` |  
| remove the jupyterhub-image | ``` sudo docker image rm jupyterhub_img ``` |  
| remove the jupyterhub volume | ``` sudo docker volume rm my_hub_jupyterhub_data ``` |  
| delete the docker builder cache | ``` sudo docker builder prune ``` |  

Then start JupyterHub again using ``` sudo docker compose up ```.

**NOTE** 

Instead of the above steps, it may work updating the `jupyterhub_config.py` file by using the command:
```
docker compose up --build
```
(this yet needs to be tested)

### To Modify the JupyterLab Image of the user environment
The user JupyterLab environments are based on the python-only image of [GPU-Jupyter](https://github.com/iot-salzburg/gpu-jupyter). Check this GitHub site if you want to modify the image. It should also be possible to install additional packages on top of this image by modifying the dockerfile in `JupyterHub_Docker/juypterlab`. Consult the [Docker documentation for best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) for doing so.
