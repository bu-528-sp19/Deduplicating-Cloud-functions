import couchdb

def connect_couchdb():
    couch = couchdb.Server("http://localhost:5984")
    return couch

def addFunctionIfNotExist(couch,functionId,db_name="test"):

    if db_name not in couch:
        db = couch.create(db_name)
        doc = {
            "function": [
				{
				  "fid": "6a9746b1a0016b37219b90ebf534b443",
				  "ref": [
					{
					  "checksum": "48480882390a88a0b933b3ff0bf62dc5",
					  "minio_ref": "http://localhost:9000/output/out120.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=DCJSAEHVFETULK44U89V%2F20190228%2F%2Fs3%2Faws4_request&X-Amz-Date=20190228T170652Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=250d562571de25b845c7ea85ae3aa887bb920d7b945940f1932c11f9444b8473"
					}
				  ]
				}]
        }
        db.save(doc)

def addUniqueChecksum(couch,checksum,db_name="test"):
    db = couch[db_name]
    #print(db)
    for id in db:
        #print(id)
        doc = db[id]
        #print("id: "+doc)
        print(doc['function']['ref'])
        doc['function'] = {'fid': 1222,
                'ref': [
                    {'checksum': 'ss','minio_ref': 'asd'}
                ]}
        db[doc.id] = doc


if __name__ == "__main__":
    couch = connect_couchdb()
    addFunctionIfNotExist(couch,"a")
    '''error-resolve this'''
    addUniqueChecksum(couch,"check")