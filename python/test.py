import sys
import requests
from minio import Minio
import os
from minio.error import ResponseError
from PIL import Image

def main():
    client = Minio('52.116.33.131:9000',
                   access_key='sanity',
                   secret_key='CloudforAll!',
                   secure=False)
    try:
        client.fget_object('test1', 'a.jpg', 'a.jpg')
    except ResponseError as err:
        print(err)

    im = Image.open('a.jpg')
    im.thumbnail((120,120), Image.ANTIALIAS)
    im.save("thumbnail.jpg")
    print("Thumbnail generated thumbnail.jpg")

    try:
        client.fput_object('test2', 'a.jpg','thumbnail.jpg')
    except ResponseError as err:
        print(err)
if __name__ == "__main__":
    main()