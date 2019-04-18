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
    city = data['city']
    country = data['country']
	
##input file to this function should be of the form(.json):
##{'city':'Boston',
##'country':'US',
##'date':'04/18/2019'}


#city_name = 'Boston,US'
city_name = city + ',' + country
call = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&APPID=8ddb21521e40ef1e715fb26942922b92'
r = requests.get(call)

max_temp = r.json()['main']['temp_max']
min_temp = r.json()['main']['temp_min']

diff = int(max_temp) - int(min_temp)

outputFile = "outputweather.txt"
with open(outputFile, 'w') as fp:
    fp.write('Difference between max and min temperature is {:d}'.format(diff))
	
##output file will be .txt:
##Difference between max and min temperature is 3.

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
