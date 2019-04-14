from minio import Minio
from checksum import calculate_checksum
from minio.error import ResponseError
from connectCouchdb import connect_couchdb,addFunctionIfNotExist


def connect_minio():
    mc = Minio('52.116.33.131:9000',
                   access_key='Q3AM3UQ867SPQQA43P2F',
                   secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                   secure=True)

    return mc

def getObject(mc,fromkafka,bucket):

    data = mc.get_object(bucket, fromkafka)
    obj = "testImg"
    with open(obj, 'wb') as file_data:
        for d in data.stream(32 * 1024):
            file_data.write(d)
    return obj

def createBucket(mc,bucket):
    try:
        if not mc.bucket_exists(bucket):
            mc.make_bucket(bucket,location="sanity-local")

    except ResponseError as err:
        print(err)
