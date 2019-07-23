FROM nvidia/cuda:10.0-cudnn7-runtime-ubuntu18.04

RUN apt-get update && apt-get install -y wget vim bzip2 && \
    wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh -O Anaconda.sh && \
    /bin/bash Anaconda.sh -b -p /opt/conda && \
	rm Anaconda.sh

ENV PATH /opt/conda/bin:$PATH

#Install ANACONDA Environment
RUN conda create -y -n jupyter_env python=3.6 anaconda && \
	/opt/conda/envs/jupyter_env/bin/pip install tensorflow-gpu keras jupyter-tensorboard jupyterlab && \
    mkdir code && \
    mkdir /code/lib

WORKDIR /code
ADD ./JRA/util /code/lib
#Launch JUPYTER COMMAND
EXPOSE 8888
CMD ["/opt/conda/envs/jupyter_env/bin/jupyter-lab --no-browser --port=8888 --ip=0.0.0.0 --allow-root"]