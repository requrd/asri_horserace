FROM tensorflow/tensorflow:latest-gpu-py3-jupyter

ENV PYTHONPATH=/opt/lib \
    DB=/code \
    SETUPTOOLS_USE_DISTUTILS=stdlib

#Install Jupyter Environment
RUN pip install --upgrade pip && \
    pip install jupyterlab seaborn graphviz pydotplus sklearn && \
    apt update && \
    apt install -y git fonts-ipaexfont graphviz && \
    echo -e "font.family       : IPAexGothic" >> /usr/local/lib/python3.6/dist-packages/matplotlib/mpl-data/matplotlibrc

#Install JRDB Environment
RUN mkdir code && \
    mkdir /opt/lib && \
    git clone https://github.com/astroripple/horseview.git /opt/lib/horseview && \
    git clone https://github.com/astroripple/jra-tools.git /opt/lib/util && \
    pip uninstall -y enum34 && \
    pip install flask_sqlalchemy flask_restless flask_migrate

WORKDIR /code
#Launch JUPYTER COMMAND
EXPOSE 8888
CMD ["jupyter-lab","--no-browser", "--port=8888", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''"]