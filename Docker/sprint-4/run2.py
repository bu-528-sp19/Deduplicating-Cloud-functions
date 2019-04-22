import json
from minio import Minio
from minio.error import ResponseError
import time

start_time = time.time()
client = Minio('52.116.33.131:9000',access_key='sanity',secret_key='CloudforAll!',secure=False)

# getting the kafka logs file from Minio Cloud Store
client.fget_object('store', 'kafka_log.json', 'kafka_log.json')

with open('kafka_log.json') as file:
    data = json.load(file)

print(data)
# getting bucket and object name from logs
file_location = data["Key"]
bucket_name = file_location.split('/')[0]
file_name = file_location.split('/')[1]

# getting object from Minio
try:
    client.fget_object(bucket_name, file_name, 's.txt')
except ResponseError as err:
    print(err)

print("Object fetched")

file=open("s.txt")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

print(wordcount)

with open('data.json', 'w') as fp:
    json.dump(wordcount, fp)

print("Data dump is done")

new_file_name='data.json'

try:
    client.fput_object('test2', new_file_name, new_file_name)
except ResponseError as err:
    print(err)

difference = (time.time() - start_time) * 1000
# storing thumbnail reference in json format in store bucket
location = "test2" + "/" + new_file_name
reference = {"reference":location, "time":difference}

print(reference)
# storing reference in JSON
with open('minio_log.json', 'w') as file:
    json.dump(reference, file)

print("Json log is dumped")
# storing JSON in Minio store bucket
try:
    client.fput_object('store', 'minio_log.json', 'minio_log.json')
except ResponseError as err:
    print(err)

print("Minio logs updated")
