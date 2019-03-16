from kafkaConnect import kafka_consumer
from connectMinio import connect_minio,getObject
from checksum import calculate_checksum
from connectCouchdb import connect_couchdb,addFunctionIfNotExist
from connectOpenWhisk import execute

topicName = "abc"

event = kafka_consumer(topicName)
#parse the file name

bucket_name=event.split('/')[0]
file_name=event.split('/')[1]

mc = connect_minio()
obj = getObject(mc,file_name,bucket_name)

img_checksum = calculate_checksum(obj)

'''connect couchdb'''
couch = connect_couchdb()

addFunctionIfNotExist(couch,"sanity")

##couch db code to check if data exists or not

command = "wsk -i action invoke action_thumbnail"
execute(command)



