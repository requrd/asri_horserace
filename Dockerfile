FROM tensorflow/tensorflow:latest-gpu-py3-jupyter

ENV PYTHONPATH=/opt/lib \
    DB=mariadb+pymysql://astroripple:S#tonoprime0407@192.168.0.197/astroripple \
    SETUPTOOLS_USE_DISTUTILS=stdlib

#Install Jupyter Environment
RUN pip install --upgrade pip && \
    pip install jupyterlab seaborn graphviz pydotplus sklearn pymysql && \
    apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/3bf863cc.pub && \
    apt update && \
    apt install -y git fonts-ipaexfont graphviz && \
    echo -e "font.family       : IPAexGothic" >> /usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/matplotlibrc

#Install JRDB Environment
RUN mkdir code && \
    mkdir /opt/lib && \
    git clone https://github.com/astroripple/horseview.git /opt/lib/horseview && \
    git clone https://github.com/astroripple/jra-tools.git /opt/lib/util && \
    pip uninstall -y enum34 && \
    pip install flask_sqlalchemy flask_migrate

WORKDIR /code
#Launch JUPYTER COMMAND
EXPOSE 8888
CMD ["jupyter-lab","--no-browser", "--port=8888", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''"]