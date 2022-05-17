FROM python:3.7.5
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install tensorflow==1.14.0
RUN pip install numpy \
        pandas \
        sklearn \
        pyyaml \
        h5py
RUN pip install keras==2.3.1 --no-deps
