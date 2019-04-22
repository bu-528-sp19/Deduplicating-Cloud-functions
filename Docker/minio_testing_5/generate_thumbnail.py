import sys
import json
import os
import requests
from minio import Minio
from minio.error import ResponseError
from PIL import Image
from kafka import KafkaConsumer
from json import loads


client = Minio('52.116.33.131:9000',
               access_key='sanity',
               secret_key='CloudforAll!',
               secure=False)


# getting the kafka logs file from Minio Cloud Store
client.fget_object('store', 'kafka_log.json', 'kafka_log.json')

with open('kafka_log.json') as file:
    data = json.load(file)

# getting bucket and object name from logs
file_location = data["Key"]
bucket_name = file_location.split('/')[0]
file_name = file_location.split('/')[1]

# getting object from Minio
try:
    client.fget_object(bucket_name, file_name, 'local.jpg')
except ResponseError as err:
    print(err)


im = Image.open('local.jpg')
im.thumbnail((120,120), Image.ANTIALIAS)
new_file_name = (file_name.split('.')[0]) + '-thumbnail.jpg'
im.save(new_file_name)
print("Thumbnail generated", new_file_name)

try:
    client.fput_object('test2', new_file_name, new_file_name)
except ResponseError as err:
    print(err)

# storing thumbnail reference in json format in store bucket
location = "test2" + "/" + new_file_name
reference = {"reference":location}

# storing reference in JSON
with open('minio_log.json', 'w') as file:
    json.dump(reference, file)

# storing JSON in Minio store bucket
try:
    client.fput_object('store', 'minio_log.json', 'minio_log.json')
except ResponseError as err:
    print(err)

    







