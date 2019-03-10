from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'in-bucket-notifications',
    bootstrap_servers=['172.18.0.2:9092'],
    auto_offset_reset='latest')
    #value_deserializer=lambda x: loads(x.decode('utf-8')))
    #enable_auto_commit=True,
    #group_id='my-group',
    #api_version=(0,10))

for message in consumer:
    record = loads(message.value)
    print(record)
