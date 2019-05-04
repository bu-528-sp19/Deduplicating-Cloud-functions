import couchdb
import hashlib

mapdocId = 0 
mapdocRev = 0

def connect_couchdb():
	couch = couchdb.Server("http://52.116.33.131:5984")
	return couch

def addInputDataIfNotExist(couch, userdocId, functionChecksum, dataChecksum):
	usersdb = couch["users"]
	userdoc = usersdb.get(userdocId)
	userdoc[functionChecksum][dataChecksum]= ""
	usersdb.save(userdoc)
	
def addMinioRef(couch,userdocId,functionChecksum,dataChecksum,minioRef):
	usersdb = couch["users"]
	userdoc = usersdb.get(userdocId)
	if dataChecksum in userdoc[functionChecksum]:
		userdoc[functionChecksum][dataChecksum]= minioRef
		usersdb.save(userdoc)
	else:
		print("The input data checksum ",dataChecksum," not available")

	
def authenticateUser(username, password):
	#toHash = username.encode('utf-8') 
	#hash_object = hashlib.md5(toHash)
	#hashedUsername = hash_object.hexdigest()
	hashedUsername = username
	return hashedUsername
	
def createDBsIfNotExist(couch):
	global mapdocId, mapdocRev
	
	if "mappings" not in couch:
		mapdb = couch.create("mappings")
		mapdocId, mapdocRev = mapdb.save({})
	else:
		mapdb = couch["mappings"]
		for id in mapdb:
			mapdocId = id
	if "users" not in couch:
		couch.create("users")
		
		
def getUpdateDocOfUser(couch, hashedUsername, functionChecksum, dataChecksum):
	global mapdocId
	mapdb = couch["mappings"]
	mapdoc = mapdb.get(mapdocId)
	usersdb = couch["users"]
	##new user --> create userdoc
	if hashedUsername not in mapdoc:
		##first, create userdoc under users db
		userdocId, userdocRev = usersdb.save({functionChecksum:{}})
		##second, save userdocId to mappings db
		mapdoc[hashedUsername] = userdocId
		mapdb.save(mapdoc)
		state = None
	
	##old user --> get userdocid from mappings
	else:
		userdocId = mapdb[mapdocId][hashedUsername]
		userdoc = usersdb.get(userdocId)
		if functionChecksum not in userdoc:
			userdoc[functionChecksum] = {}
			usersdb.save(userdoc)
			state = None
		else:
			if dataChecksum in userdoc[functionChecksum]:
				state = userdoc[functionChecksum][dataChecksum]
			else:
				state = None
			
	return state, userdocId

	
def main():
	couch = connect_couchdb()
	functionChecksum = "belizfunc"
	dataChecksum = "belizdata"
	
	createDBsIfNotExist(couch)
	hashedUsername = authenticateUser(username="beliz", password="12345")
	state, userdocId = getUpdateDocOfUser(couch, hashedUsername, functionChecksum, dataChecksum)
	
	# Check if same data is available in the couch db
	if state is not None:
		print("\n**Duplicate Data**")
		print(state)
	else:
		print("\nNew Data")
		#create data if not present
		addInputDataIfNotExist(couch, userdocId, functionChecksum, dataChecksum)
	
      	
if __name__	== '__main__':
	main()