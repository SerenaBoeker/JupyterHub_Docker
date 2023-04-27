import os
import docker

c = get_config()
c.JupyterHub.spawner_class   = "dockerspawner.DockerSpawner"
c.DockerSpawner.image        = os.environ["DOCKER_JUPYTER_IMAGE"]
c.DockerSpawner.network_name = os.environ["DOCKER_NETWORK_NAME"]
c.JupyterHub.hub_ip          = os.environ["HUB_IP"]
c.Authenticator.admin_users  = {'ncsadmin'}

# DummyAuthenticator:
# from jupyterhub.auth import DummyAuthenticator
# c.JupyterHub.authenticator_class = DummyAuthenticator

# SSH Authenticator:
c.JupyterHub.authenticator_class  = 'sshauthenticator.SSHAuthenticator'
c.SSHAuthenticator.server_address = '192.168.0.177'       # the ip of the server
c.SSHAuthenticator.server_port    = 22

## User data persistence
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
c.DockerSpawner.volumes = {
          'jupyterhub-user-{username}': notebook_dir,
          '/home/ncsadmin/JupyterHub_Docker/volumes/shared': { 'bind': '/home/jovyan/work/shared', 'mode': 'rw'},
          '/home/ncsadmin/JupyterHub_Docker/volumes/data':   { 'bind': '/home/jovyan/work/data',   'mode': 'ro'} 
}

# GPU access
c.DockerSpawner.extra_host_config = {
    "device_requests": [
        docker.types.DeviceRequest(
            count=-1,
            capabilities=[["gpu"]],
        ),
    ],
}

c.DockerSpawner.remove_containers = True
c.Spawner.default_url = '/lab'