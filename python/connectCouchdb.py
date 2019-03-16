import couchdb

def connect_couchdb():
    couch = couchdb.Server("http://52.116.33.131:5984")
    return couch

def addFunctionIfNotExist(couch,db_name="sanity"):

    if db_name not in couch:
        db = couch.create(db_name)
        doc = {
            "function": [
				{
				  "fid": "6a9746b1a0016b37219b90ebf534b443",
				  "ref": [
					{
					  "checksum": "48480882390a88a0b933b3ff0bf62dc5",
					  "minio_ref": "abc"
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