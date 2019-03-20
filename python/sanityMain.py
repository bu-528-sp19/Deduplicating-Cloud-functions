from kafkaConnect import kafka_consumer
from connectMinio import connect_minio,getObject
from checksum import calculate_checksum
from connectCouchdb import connect_couchdb,addFunctionIfNotExist,addMinioRef,addInputDataIfNotExist,verfiyDataAvailable
from connectOpenWhisk import execute

def process(event):
    bucket_name = event.split('/')[0]
    file_name = event.split('/')[1]

    #Hard-coded for now
    function_id = "fid123"

    #connect couchdb
    couch = connect_couchdb()

    #connect minio
    mc = connect_minio()

    #fetch file from
    obj = getObject(mc, file_name, bucket_name)

    img_checksum = calculate_checksum(obj)

    if bucket_name == "input":
        #create function if not present
        addFunctionIfNotExist(couch, "sanity")

        # Check if same data is available in the couch db
        state = verfiyDataAvailable(couch,function_id,img_checksum,"sanity")

        if state is not None:
            return state

        #create data if not present
        addInputDataIfNotExist(couch,function_id,img_checksum)

        command = "wsk -i action invoke action_thumbnail"
        execute(command)

    else:
        # code to put the ref name in couuchdb
        addMinioRef(couch, function_id, img_checksum, event)
        return event
