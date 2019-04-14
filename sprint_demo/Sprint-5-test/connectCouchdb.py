import couchdb

def connect_couchdb():
    couch = couchdb.Server("http://52.116.33.131:5984")
    return couch

def addFunctionIfNotExist(couch,functionChecksum,db_name="sanity"):

    if db_name not in couch:
        db = couch.create(db_name)

        doc = {
            functionChecksum: {
            }
        }
        db.save(doc)
    else:
        db = couch[db_name]
        for doc in db:
            docs = db[doc]
            if functionChecksum not in docs:
                docs[functionChecksum]={}
            db.save(docs)

def createUserDoc(couch,db_name="sanity"):
    if db_name not in couch:
        db = couch.create(db_name)

    doc = {
    }
    db.save(doc)
    return doc['_id']

def addUserIfNotExist(couch,userName,db_name="user"):
    #addFunctionIfNotExist(couch)
    userId = createUserDoc(couch)
    db = None
    if db_name not in couch:
        db = couch.create(db_name)

    doc = {
        userName: userId
    }
    db.save(doc)


def addInputDataIfNotExist(couch,functionChecksum,inputChecksum,db_name="sanity"):
    db = couch[db_name]
    for id in db:
        doc = db[id]
        if inputChecksum not in doc[functionChecksum]:

            doc[functionChecksum][inputChecksum]= ""
            print(doc[functionChecksum][inputChecksum])
            db.save(doc)

def addMinioRef(couch,functionChecksum,inputChecksum,minioRef,db_name="sanity"):
    db = couch[db_name]
    for id in db:
        doc = db[id]
        if inputChecksum in doc[functionChecksum]:
            doc[functionChecksum][inputChecksum]= minioRef
            db.save(doc)
        else:
            print("The input checksum ",inputChecksum," not available")

def verfiyDataAvailable(couch,functionChecksum,inputChecksum,db_name="sanity"):
    db = couch[db_name]
    for id in db:
        doc = db[id]
        if functionChecksum not in doc:
            return None
        if inputChecksum in doc[functionChecksum]:
            return doc[functionChecksum][inputChecksum]
        else:
            return None

