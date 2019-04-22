FROM ubuntu
COPY hw.png ./
COPY image-uploader.py ./
RUN apt-get update
RUN apt install python3-pip -y
RUN pip3 install couchdb 
RUN pip3 install minio 
RUN pip3 install ruamel.yaml 
RUN pip3 install Pillow 
RUN pip3 install kafka-python 
RUN pip3 install kafka
CMD ["python3", "./image-uploader.py"]
