from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'in-bucket-notifications',
    bootstrap_servers=['52.116.33.131:9092'],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='my-group',
    api_version=(0,10))
    #value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    record = json.loads(message.value)
    print(record)
