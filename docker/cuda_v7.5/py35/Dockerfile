FROM nvidia/cuda:7.5-cudnn5-devel

RUN apt-get update 

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN ln -s /usr/local/nvidia/lib64/libcuda.so.1 /usr/lib/x86_64-linux-gnu/libcuda.so

# Install minimum 
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends wget bzip2 ca-certificates \
            libglib2.0-0 libxext6 libsm6 libxrender1 \
             git mercurial subversion

# Install miniconda 
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.1.11-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

# Install python and libraries
ARG python_version=3.5
ARG tensorflow_version=0.10.0rc0-cp35-cp35m
ENV PATH /opt/conda/bin:$PATH
RUN conda install -y python=${python_version} && \
    pip install https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-${tensorflow_version}-linux_x86_64.whl && \
    pip install git+git://github.com/Theano/Theano.git && \
    pip install chainer && \
    pip install ipdb pytest pytest-cov python-coveralls coverage==3.7.1 pytest-xdist pep8 pytest-pep8 pydot_ng && \
    conda install jupyter Pillow scikit-learn notebook pandas matplotlib nose pyyaml six h5py && \
    pip install git+git://github.com/fchollet/keras.git && \
    conda clean -yt

# Set up .theanorc for CUDA
RUN echo "[global]\ndevice=gpu\nfloatX=float32\noptimizer_including=cudnn\n[lib]\ncnmem=0.1\n[nvcc]\nfastmath=True" > /root/.theanorc



# set jupyter config
RUN mkdir -p /root/.jupyter && \
    echo "c.NotebookApp.ip = '*' \nc.NotebookApp.port = 8888 \nc.NotebookApp.open_browser = False" \ 
        > /root/.jupyter/jupyter_notebook_config.py

# port for jupyter notebook
EXPOSE 8888

WORKDIR /root 
#CMD ["jupyter-notebook"]
