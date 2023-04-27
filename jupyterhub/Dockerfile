# base image
FROM jupyterhub/jupyterhub

RUN pip install dockerspawner

# install SSH authenticator
RUN pip install https://github.com/andreas-h/sshauthenticator/archive/v0.1.zip

COPY jupyterhub_config.py .