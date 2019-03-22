import couchdb

def connect_couchdb():
    couch = couchdb.Server("http://localhost:5984")
    return couch

def addFunctionIfNotExist(couch,functionChecksum,db_name="test"):
	
	if db_name not in couch:
		db = couch.create(db_name)
	
		doc = {
			functionChecksum: {
	
	
			}	
        }
		db.save(doc)
	# db exists
	else:
		db = couch[db_name]
		for doc in db:
			docs = db[doc]
		# function does not exist in db
			#print(docs['function'])
			#doc1 = {"checksum": ""}
			#for funcs in docs:
				#print(type(docs['function']))
			#print(functionChecksum)
			#print(funcs)
			if functionChecksum not in docs:
				docs[functionChecksum]={}
			#else:
			#	docs[functionChecksum].append(doc1)
			print(docs)
					
			db.save(docs)

def addInputDataIfNotExist(couch,functionChecksum,inputChecksum, outputBucketName="obucket",db_name="test"):
	db = couch[db_name]
    #print(db)
	for id in db:
        #print(id)
		doc = db[id]
        #print("id: "+doc)
		if inputChecksum not in doc[functionChecksum]:
			
			doc[functionChecksum][inputChecksum]= ""
			print(doc[functionChecksum][inputChecksum])
			db.save(doc)
			
		
		
        


if __name__ == "__main__":
    couch = connect_couchdb()
    addFunctionIfNotExist(couch,"a")
    '''error-resolve this'''
    addInputDataIfNotExist(couch,"a","a2")