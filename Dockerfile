FROM nvidia/cuda:10.0-cudnn7-runtime-ubuntu18.04

RUN apt-get update && apt-get install -y wget vim bzip2 git && \
    wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh -O Anaconda.sh && \
    /bin/bash Anaconda.sh -b -p /opt/conda && \
	rm Anaconda.sh

ENV PATH=/opt/conda/bin:$PATH \
    PYTHONPATH=/opt/lib \
    DB=/code

#Install ANACONDA Environment
RUN conda create -y -n jupyter_env python=3.6 anaconda && \
	/opt/conda/envs/jupyter_env/bin/pip install tensorflow-gpu keras jupyter-tensorboard jupyterlab

#Install JRDB Environment
RUN mkdir code && \
    mkdir /opt/lib && \
    git clone https://github.com/astroripple/horseview.git /opt/lib/horseview && \
    /opt/conda/envs/jupyter_env/bin/pip install flask_sqlalchemy flask_restless flask_migrate

COPY ./JRA/util /opt/lib
WORKDIR /code
#Launch JUPYTER COMMAND
EXPOSE 8888
CMD ["/opt/conda/envs/jupyter_env/bin/jupyter-lab","--no-browser", "--port=8888", "--ip=0.0.0.0", "--allow-root"]