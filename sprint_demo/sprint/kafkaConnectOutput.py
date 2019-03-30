import json
from kafka import KafkaConsumer
from json import loads
# from sanityMain import process
# from minio.error import ResponseError
# from minio import Minio

def kafka_consumer(topic_name):

    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=['172.18.0.2:9092'],
        auto_offset_reset='latest')

    for message in consumer:
        json_data = json.loads(message.value)
        bucket_name = json_data['Key'].split('/')[0]
        if (json_data['EventName'] == 's3:ObjectCreated:Put' and bucket_name == 'test2'):
            print('\nOutput Bucket :', bucket_name)
            print('\nOutput File name :', json_data['Key'].split('/')[1])

if __name__ == "__main__":
    kafka_consumer("out-bucket-notifications")
