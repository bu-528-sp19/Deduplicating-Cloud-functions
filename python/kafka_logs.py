import os
import json
from kafka import KafkaConsumer
from minio import Minio
from minio.error import ResponseError

consumer = KafkaConsumer('in-bucket-notifications', bootstrap_servers=['172.18.0.2:9092'], auto_offset_reset='latest')
# value_deserializer=lambda x: loads(x.decode('utf-8')))
# enable_auto_commit=True,
# group_id='my-group',
# api_version=(0,10))

# to store kafka logs in Minio Cloud Storage only for s3:ObjectCreated:Put event
for message in consumer:
    json_data = json.loads(message.value)
    bucket_name = json_data['Key'].split('/')[0]
    if (json_data['EventName'] == 's3:ObjectCreated:Put' and bucket_name == 'test1'):
        print(json_data)
        with open('kafka_log.json', 'w') as outfile:
            json.dump(json_data, outfile)

        # Initialize minioClient with an endpoint and access/secret keys.
        minioClient = Minio('52.116.33.131:9000', access_key='sanity', secret_key='CloudforAll!', secure=False)

        # Put a json object log with contents from kafka consumer in store bucket
        try:
            minioClient.fput_object('store', 'kafka_log.json', 'kafka_log.json')

        except ResponseError as err:
           print(err)
