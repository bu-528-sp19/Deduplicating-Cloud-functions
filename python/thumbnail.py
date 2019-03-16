import sys
import requests
from minio import Minio
import os
from minio.error import ResponseError
from PIL import Image
from kafka import KafkaConsumer
from json import loads


consumer = KafkaConsumer(
    "in-bucket-notifications",
    bootstrap_servers=['172.18.0.2:9092'],
    auto_offset_reset='latest')

event = None

for message in consumer:
    record = loads(message.value)
    # print("Event Name :", record["EventName"])
    print("File location :", record["Key"])
    event = record["Key"]

bucket_name=event.split('/')[0]
file_name=event.split('/')[1]

client = Minio('52.116.33.131:9000',
               access_key='sanity',
               secret_key='CloudforAll!',
               secure=False)
try:
    client.fget_object(bucket_name, file_name, 'local.jpg')
except ResponseError as err:
    print(err)


im = Image.open('local.jpg')
im.thumbnail((120,120), Image.ANTIALIAS)
im.save("thumbnail.jpg")
print("Thumbnail generated thumbnail.jpg")

try:
    client.fput_object('test2', 'thumbnail.jpg','thumbnail.jpg')
except ResponseError as err:
    print(err)


