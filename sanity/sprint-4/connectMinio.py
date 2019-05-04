from minio import Minio
from checksum import calculate_checksum
from connectCouchdb import connect_couchdb,addFunctionIfNotExist


def connect_minio():
    mc = Minio('52.116.33.131:9000',
                   access_key='sanity',
                   secret_key='CloudforAll!',
                   secure=False)

    return mc

def getObject(mc,fromkafka,bucket):

    data = mc.get_object(bucket, fromkafka)
    obj = "testImg"
    with open(obj, 'wb') as file_data:
        for d in data.stream(32 * 1024):
            file_data.write(d)
    return obj
