from connectMinio import connect_minio,getObject
from checksum import calculate_checksum
from connectCouchdb import connect_couchdb,addFunctionIfNotExist,addMinioRef,addInputDataIfNotExist,verfiyDataAvailable
from connectOpenWhisk import execute
import json
import time

def process(event,function_name):
    bucket_name = event.split('/')[0]
    file_name = event.split('/')[1]

    function_id = calculate_checksum(function_name)

    #connect couchdb
    couch = connect_couchdb()

    #connect minio
    mc = connect_minio()

    #fetch file from
    obj = getObject(mc, file_name, bucket_name)

    img_checksum = calculate_checksum(obj)

    #create function if not present
    addFunctionIfNotExist(couch, function_id)

    # Check if same data is available in the couch db
    state = verfiyDataAvailable(couch,function_id,img_checksum,"sanity")

    if state is not None:
        print("\n**Duplicate data**")
        return state

    #create data if not present
    addInputDataIfNotExist(couch,function_id,img_checksum)

    #create command that makes an action
    action_name = "random"

    command = "wsk -i action invoke weatherhit"
    execute(command)
    print(function_name+" Invoked Successfully")
    time.sleep(5)
    obj = getObject(mc, "minio_log.json", "store")
    with open(obj) as json_file:
        data = json.load(json_file)
        ref = data['reference']

        addMinioRef(couch, function_id, img_checksum, ref)
    print("\n**Unique data**")
    return ref

'''
    else:
        # code to put the ref name in couuchdb
        addMinioRef(couch, function_id, img_checksum, event)
        return event
'''
