import json
from kafka import KafkaConsumer
from json import loads
from sanityMain import process
from minio.error import ResponseError
from minio import Minio

def kafka_consumer(topic_name,function_name):

    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=['172.18.0.2:9092'],
        auto_offset_reset='latest')

    for message in consumer:
        json_data = json.loads(message.value)
        bucket_name = json_data['Key'].split('/')[0]
        if (json_data['EventName'] == 's3:ObjectCreated:Put' and bucket_name == 'test1'):
            print('\nInput Bucket :', bucket_name)
            print('\nInput File name :', json_data['Key'].split('/')[1])
            with open('kafka_log.json', 'w') as outfile:
                json.dump(json_data, outfile)

            # Initialize minioClient with an endpoint and access/secret keys.
            minioClient = Minio('52.116.33.131:9000', access_key='sanity', secret_key='CloudforAll!', secure=False)

            # Put a json object log with contents from kafka consumer in store bucket
            try:
                minioClient.fput_object('store', 'kafka_log.json', 'kafka_log.json')
                output_reference = process(json_data['Key'],function_name)
                print('\nOutput File reference :', output_reference)
            except ResponseError as err:
                print(err)

if __name__ == "__main__":
    kafka_consumer("in-bucket-notifications","")
