FROM ubuntu
MAINTAINER Paritosh Shirodkar (paritoshshirodkar@gmail.com)
COPY run2.py ./
RUN apt-get update
RUN apt install python3-pip -y
RUN pip3 install requests
RUN pip3 install minio
CMD ["python3", "./run2.py"]
