from minio import Minio
from checksum import calculate_checksum
from parseYaml import parse_yaml
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

def main():

    function_name = parse_yaml()
    function_id = calculate_checksum(function_name)
    print("Function id : "+function_id)

    '''data from kafka event, which is yet to implement'''
    fromkafka = "a.jpg"
    bucket = "input"

    '''connect couchdb'''
    db = connect_couchdb()

    '''query if function id exists in the couchdb. If not, create a new one'''
    addFunctionIfNotExist(db,function_id)

    '''Connecting minio'''
    mc = connect_minio()

    '''fetch data from the minio'''
    obj = getObject(mc,fromkafka,bucket)

    '''Calculate checksum'''
    img_checksum = calculate_checksum(obj)
    print("Image Checksum: "+img_checksum)

    '''Adding checksum in couchdb'''
    #addUniqueChecksum(db,img_checksum)

    '''call to openwhisk'''
    #create_thumbnail(fromkafka)

if __name__ == "__main__":
    main()