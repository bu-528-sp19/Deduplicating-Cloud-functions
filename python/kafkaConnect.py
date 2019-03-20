import json
from kafka import KafkaConsumer
from json import loads
from sanityMain import process

def kafka_consumer(topic_name):

    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=['172.18.0.2:9092'],
        auto_offset_reset='latest')

    for message in consumer:
        record = loads(message.value)
        #print("Event Name :", record["EventName"])
        print("File location :", record["Key"])
        event = record["Key"]
        data = process(event)
        print(data)

if __name__ == "__main__":
    kafka_consumer("in-bucket-notifications")
