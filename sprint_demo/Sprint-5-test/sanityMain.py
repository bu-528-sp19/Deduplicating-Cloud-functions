from connectMinio import connect_minio,getObject
from checksum import calculate_checksum
from connectCouchdbMulti import *
from connectOpenWhisk import execute
import json
import time

def process(event,function_name,user_name):
    bucket_name = event.split('/')[0]
    file_name = event.split('/')[1]

    function_id = calculate_checksum(function_name)
    mc = connect_minio()
    obj = getObject(mc, file_name, bucket_name)
    img_checksum = calculate_checksum(obj)

    couch = connect_couchdb()
    createDBsIfNotExist(couch)
    hashedUsername = authenticateUser(user_name)
    state, userdocId = getUpdateDocOfUser(couch, hashedUsername, function_id, img_checksum)

    if state is not None:
        print("\n**Duplicate Data**")
        return state

    #create data if not present
    addInputDataIfNotExist(couch,userdocId,function_id,img_checksum)

    command = "wsk -i action invoke weatherhit"
    execute(command)
    print(function_name+" Invoked Successfully")
    time.sleep(5)

    obj = getObject(mc, "minio_log.json", "store")
    with open(obj) as json_file:
        data = json.load(json_file)
        ref = data['reference']

        addMinioRef(couch,userdocId, function_id, img_checksum, ref)
    print("\n**Unique Data**")
    return ref
