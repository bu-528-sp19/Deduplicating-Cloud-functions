# # getting the kafka logs file from Minio Cloud Store
# client.fget_object('store', 'kafka_log.json', 'kafka_log.json')
#
# with open('kafka_log.json') as file:
#     data = json.load(file)
#
# # getting bucket and object name from logs
# file_location = data["Key"]
# bucket_name = file_location.split('/')[0]
# file_name = file_location.split('/')[1]

def main(dict):
    
    import sys
    import json
    import os
    import requests
    from minio import Minio
    from minio.error import ResponseError
    from PIL import Image
    from kafka import KafkaConsumer
    from json import loads

    source_bucket = dict['source']
    destination_bucket = dict['destination']
    file = dict['file']

    client = Minio('52.116.33.131:9000',
                   access_key='sanity',
                   secret_key='CloudforAll!',
                   secure=False)

    # getting object from source_bucket
    try:
        client.fget_object(source_bucket, file, 'local.jpg')
    except ResponseError as err:
        print(err)

    # generating thumbnail
    im = Image.open('local.jpg')
    im.thumbnail((120, 120), Image.ANTIALIAS)
    new_file_name = (file.split('.')[0]) + '-thumbnail.jpg'
    im.save(new_file_name)

    # storing the result in destination_bucket
    try:
        client.fput_object(destination_bucket, new_file_name, new_file_name)
    except ResponseError as err:
        print(err)



    return {'output_reference' : destination_bucket + '/' + new_file_name}
