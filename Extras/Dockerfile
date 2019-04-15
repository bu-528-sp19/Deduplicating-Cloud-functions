FROM ubuntu
WORKDIR ~
COPY test.py ./
RUN apt-get update
RUN apt install python3-pip -y
RUN pip3 install couchdb 
RUN pip3 install minio 
RUN pip3 install ruamel.yaml 
RUN pip3 install Pillow 
RUN pip3 install kafka-python 
RUN pip3 install kafka
CMD ["python3", "./test.py"]
