import requests
from minio import Minio
from minio.error import ResponseError
import json

client = Minio('52.116.33.131:9000',access_key='sanity',secret_key='CloudforAll!',secure=False)
client.fget_object('store', 'kafka_log.json', 'kafka_log.json')
with open('kafka_log.json') as file:
    data = json.load(file)

file_location = data["Key"]
bucket_name = file_location.split('/')[0]
file_name = file_location.split('/')[1]
print(bucket_name)
print(file_name)

# getting object from Minio
try:
    client.fget_object(bucket_name, file_name, file_name)
except ResponseError as err:
    print(err)

with open(file_name) as json_file:
    data = json.load(json_file)
    min_temp = data['temp_min']
    max_temp = data['temp_max']

weather = {}
avg = (min_temp+max_temp)/2
weather['avg'] = avg

outputFile = file_name+'Output.json'
with open(outputFile, 'w') as fp:
    json.dump(weather, fp)

try:
    client.fput_object('test2', outputFile, outputFile)
except ResponseError as err:
    print(err)

location = "test2" + "/" + outputFile
reference = {"reference":location}
# storing reference in JSON
with open('minio_log.json', 'w') as file:
    json.dump(reference, file)
# storing JSON in Minio store bucket
try:
    client.fput_object('store', 'minio_log.json', 'minio_log.json')
except ResponseError as err:
    print(err)