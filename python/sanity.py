import sys
import checksum

def main():
	inputBucketName = argv[2].split("/")[0]
	objectName = argv[2].split("/")[1]
	outputBucketName = argv[3]
	
	functionChecksum = calculate_checksum(sys.argv[1])
	#if function exists calculate checksum of incoming data if not first create function
    couch = connect_couchdb()
	addFunctionIfNotExist(couch, functionChecksum)
	inputChecksum = calculate_checksum(getObject(inputBucketName,objectName))
	addInputDataIfNotExist(couch,functionChecksum,inputChecksum, outputBucketName, db_name="test")
	
def getObject(inputBucketName,objectName):
	# Initialize minioClient with an endpoint and access/secret keys.
	minioClient = Minio('52.116.33.131:9000', access_key='sanity', secret_key='CloudforAll!', secure=False)

	
	# get the object from bucket
	try:
		object = minioClient.fget_object(inputBucketName, objectName, objectName) 

	except ResponseError as err:
	   print(err)
	   
	return object
		
		
if __name__ == "__main__":
    main()