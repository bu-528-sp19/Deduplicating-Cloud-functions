import json
from kafka import KafkaConsumer


def kafka_consumer(topic_name):
    consumer = KafkaConsumer(topic_name, auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)

    inf = 1
    while inf == 1:
        for msg in consumer:
            record = json.loads(msg.value)
            print(record)


        if consumer is not None:
            consumer.close()

if __name__ == "__main__":
    kafka_consumer("test")