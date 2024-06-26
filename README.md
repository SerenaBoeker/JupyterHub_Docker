Table of contents:
- [Introduction](#introduction)
- [Using JupyterLab](#using-jupyterlab)
  - [Setting up new virtual environment and installing it as jupyter kernel](#setting-up-new-virtual-environment-and-installing-it-as-jupyter-kernel)
- [JupyterHub Setup](#jupyterhub-setup)



# Introduction
This repository is a containerized solution for deploying JupyterHub using Docker. Both JupyterHub and the user environments run in Docker containers, ensuring sudo rights for each user. The users must have a user account on the server in order to be able to log into JupyterHub.

The user JupyterLab environments are based on the python-only image of [GPU-Jupyter](https://github.com/iot-salzburg/gpu-jupyter). See the following collapsible section for provided packages:

<details>
    <summary>Available packages (click me!)</summary>

    absl-py==1.4.0
    aiofiles==22.1.0
    aiosqlite==0.18.0
    alembic==1.10.2
    altair==4.2.2
    anyio==3.6.2
    argon2-cffi==21.3.0
    argon2-cffi-bindings==21.2.0
    arrow==1.2.3
    asttokens==2.2.1
    astunparse==1.6.3
    async-generator==1.10
    attrs==22.2.0
    Babel==2.12.1
    backcall==0.2.0
    backports.functools-lru-cache==1.6.4
    beautifulsoup4==4.12.0
    bleach==6.0.0
    blinker==1.5
    bokeh==3.1.0
    boltons==23.0.0
    Bottleneck==1.3.7
    branca==0.6.0
    brotlipy==0.7.0
    cached-property==1.5.2
    cachetools==5.3.0
    certifi==2022.12.7
    certipy==0.1.3
    cffi==1.15.1
    charset-normalizer==3.1.0
    click==8.1.3
    cloudpickle==2.2.1
    colorama==0.4.6
    comm==0.1.3
    conda==23.3.1
    conda-package-handling==2.0.2
    conda_package_streaming==0.7.0
    contourpy==1.0.7
    cryptography==40.0.1
    cycler==0.11.0
    Cython==0.29.33
    cytoolz==0.12.0
    dask==2023.3.0
    debugpy==1.6.6
    decorator==5.1.1
    defusedxml==0.7.1
    dill==0.3.6
    distributed==2023.3.0
    entrypoints==0.4
    exceptiongroup==1.1.1
    executing==1.2.0
    fastjsonschema==2.16.3
    flatbuffers==23.3.3
    flit_core==3.8.0
    fonttools==4.39.3
    fqdn==1.5.1
    fsspec==2023.3.0
    gast==0.4.0
    gitdb==4.0.10
    GitPython==3.1.31
    gmpy2==2.1.2
    google-auth==2.17.1
    google-auth-oauthlib==0.4.6
    google-pasta==0.2.0
    graphviz==0.19.1
    greenlet==2.0.2
    grpcio==1.53.0
    h5py==3.8.0
    HeapDict==1.0.1
    idna==3.4
    imagecodecs==2023.1.23
    imageio==2.27.0
    importlib-metadata==6.1.0
    importlib-resources==5.12.0
    iniconfig==2.0.0
    ipykernel==6.22.0
    ipyleaflet==0.17.2
    ipympl==0.9.3
    ipython==8.12.0
    ipython-genutils==0.2.0
    ipywidgets==8.0.4
    isoduration==20.11.0
    jedi==0.18.2
    Jinja2==3.1.2
    joblib==1.2.0
    json5==0.9.5
    jsonpatch==1.32
    jsonpointer==2.0
    jsonschema==4.17.3
    jupyter_client==8.1.0
    jupyter-contrib-core==0.4.2
    jupyter-contrib-nbextensions==0.7.0
    jupyter_core==5.3.0
    jupyter-events==0.6.3
    jupyter-highlight-selected-word==0.2.0
    jupyter-nbextensions-configurator==0.6.1
    jupyter_server==2.4.0
    jupyter_server_fileid==0.8.0
    jupyter-server-mathjax==0.2.6
    jupyter_server_terminals==0.4.4
    jupyter_server_ydoc==0.8.0
    jupyter-telemetry==0.1.0
    jupyter-ydoc==0.2.3
    jupyterhub==3.1.1
    jupyterlab==3.6.3
    jupyterlab-drawio==0.9.0
    jupyterlab-git==0.41.0
    jupyterlab-pygments==0.2.2
    jupyterlab_server==2.22.0
    jupyterlab-spellchecker==0.7.3
    jupyterlab-widgets==3.0.7
    keras==2.10.0
    Keras-Preprocessing==1.1.2
    kiwisolver==1.4.4
    libclang==16.0.0
    libmambapy==1.4.1
    llvmlite==0.39.1
    locket==1.0.0
    lxml==4.9.2
    lz4==4.3.2
    Mako==1.2.4
    mamba==1.4.1
    Markdown==3.4.3
    MarkupSafe==2.1.2
    matplotlib==3.7.1
    matplotlib-inline==0.1.6
    mistune==2.0.5
    mpmath==1.3.0
    msgpack==1.0.5
    munkres==1.1.4
    nbclassic==0.5.3
    nbclient==0.7.2
    nbconvert==7.2.10
    nbdime==3.1.1
    nbformat==5.8.0
    nest-asyncio==1.5.6
    networkx==3.0
    notebook==6.5.3
    notebook_shim==0.2.2
    numba==0.56.4
    numexpr==2.7.3
    numpy==1.23.5
    oauthlib==3.2.2
    opt-einsum==3.3.0
    packaging==23.0
    pamela==1.0.0
    pandas==2.0.0
    pandocfilters==1.5.0
    parso==0.8.3
    partd==1.3.0
    patsy==0.5.3
    pexpect==4.8.0
    pickleshare==0.7.5
    Pillow==9.4.0
    pip==23.0.1
    pkgutil_resolve_name==1.3.10
    platformdirs==3.2.0
    plotly==5.13.1
    pluggy==1.0.0
    pooch==1.7.0
    prometheus-client==0.16.0
    prompt-toolkit==3.0.38
    protobuf==3.19.6
    psutil==5.9.4
    ptyprocess==0.7.0
    pure-eval==0.2.2
    pyasn1==0.4.8
    pyasn1-modules==0.2.8
    pycosat==0.6.4
    pycparser==2.21
    pycurl==7.45.1
    Pygments==2.14.0
    PyJWT==2.6.0
    pyOpenSSL==23.1.1
    pyparsing==3.0.9
    pyrsistent==0.19.3
    PySocks==1.7.1
    pytest==7.2.2
    python-dateutil==2.8.2
    python-json-logger==2.0.7
    pytz==2023.3
    PyWavelets==1.4.1
    PyYAML==6.0
    pyzmq==25.0.2
    requests==2.28.2
    requests-oauthlib==1.3.1
    rfc3339-validator==0.1.4
    rfc3986-validator==0.1.1
    rise==5.7.1
    rsa==4.9
    ruamel.yaml==0.17.21
    ruamel.yaml.clib==0.2.7
    scikit-image==0.19.3
    scikit-learn==1.2.2
    scipy==1.10.1
    seaborn==0.12.2
    Send2Trash==1.8.0
    setuptools==67.6.1
    six==1.16.0
    smmap==5.0.0
    sniffio==1.3.0
    sortedcontainers==2.4.0
    soupsieve==2.3.2.post1
    SQLAlchemy==2.0.8
    stack-data==0.6.2
    statsmodels==0.13.5
    sympy==1.11.1
    tables==3.7.0
    tblib==1.7.0
    tenacity==8.2.2
    tensorboard==2.10.1
    tensorboard-data-server==0.6.1
    tensorboard-plugin-wit==1.8.1
    tensorflow==2.10.1
    tensorflow-estimator==2.10.0
    tensorflow-io-gcs-filesystem==0.32.0
    termcolor==2.2.0
    terminado==0.17.1
    threadpoolctl==3.1.0
    tifffile==2023.3.21
    tinycss2==1.2.1
    tomli==2.0.1
    toolz==0.12.0
    torch==1.13.1+cu116
    torchaudio==0.13.1+cu116
    torchvision==0.14.1+cu116
    torchviz==0.0.2
    tornado==6.2
    tqdm==4.65.0
    traitlets==5.9.0
    traittypes==0.2.1
    typing_extensions==4.5.0
    tzdata==2023.3
    unicodedata2==15.0.0
    uri-template==1.2.0
    urllib3==1.26.15
    wcwidth==0.2.6
    webcolors==1.13
    webencodings==0.5.1
    websocket-client==1.5.1
    Werkzeug==2.2.3
    wheel==0.40.0
    widgetsnbextension==4.0.7
    wrapt==1.15.0
    xlrd==2.0.1
    xyzservices==2023.2.0
    y-py==0.5.9
    ypy-websocket==0.8.2
    zict==2.2.0
    zipp==3.15.0
    zstandard==0.19.0
</details>


# Using JupyterLab
To access the Lab go to https://192.168.0.177:8000 and log in using your username and password (same username and password as for your user account on the server). You will be redirected to your workspace. The two folders `data` and `shared` are available to all users, `data` is read-only, used to make files available to all users, whereas users can use the `shared` folder to share files with each other.

## Setting up new virtual environment and installing it as jupyter kernel
To set up a new virtual environment, you can use the terminal of JupyterLab to install `virtualenv`, create a new environment and activate it:
```
pip install virtualenv
virtualenv <env-name>
source <env-name>/bin/activate
```
To use the newly created virtual environment as a jupyter kernel, perform following steps:
```
pip install jupyter
ipython kernel install --name "<kernelname>" --user
```
You should be able to pick the kernel now in the jupyterlab launcher tab (it may take a bit to update).  
Install all needed packages in the new virtual environment using `pip`. 

To list all installed kernels:
```
jupyter kernelspec list
```
To remove a kernel:
```
jupyter kernelspec uninstall <kernelname>
```

<details>
    <summary>Example (<a href="[url](https://github.com/ultralytics/yolov5)">YOLOv5</a>)</summary>
    In terminal:

    pip install virtualenv
    virtualenv yolov5env
    source yolov5env/bin/activate
    git clone https://github.com/ultralytics/yolov5
    cd yolov5
    pip install -r requirements.txt
    pip install jupyter
    ipython kernel install --name "YOLOv5" --user

Use the provided Jupyter Notebook `/shared/yolov5_test.ipynb` to test the installation.
</details>

# JupyterHub Setup
To set up the server and get JupyterHub up and running see [this](doc/Server_JupyterHub_Setup.md).