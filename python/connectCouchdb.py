import couchdb

def connect_couchdb():
    couch = couchdb.Server("http://localhost:5984")
    return couch

def addFunctionIfNotExist(couch,functionId,db_name="test"):

    if db_name not in couch:
        db = couch.create(db_name)
        doc = {
            'function': [
                {'fid': functionId,
                'ref': [
                    {'checksum': 'ss','minio_ref': 'asd'}
                ]}
            ]
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