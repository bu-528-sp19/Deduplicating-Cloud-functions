import couchdb

def connect_couchdb():
    couch = couchdb.Server("http://52.116.33.131:5984")
    return couch

def addFunctionIfNotExist(couch,functionChecksum,user_name,db_name="sanity",map_db_name="user"):

    if db_name not in couch:
        db = couch.create(db_name)
    if map_db_name not in couch:
        db = couch.create(map_db_name)
        doc = {}
        db.save(doc)

    addUserIfNotExist(couch,user_name)
    db = couch[map_db_name]
    for id in db:
        doc = db[id]
        getId = doc[user_name]

    db = couch[db_name]
    docs = db[getId]
    if functionChecksum not in docs:
        docs[functionChecksum] = {}
    db.save(docs)

def addUserIfNotExist(couch,userName,map_db_name="user"):
    #check is user already exist
    db = couch[map_db_name]
    for id in db:
        doc = db[id]
        if userName not in doc:
            userId = createUserDoc(couch)
            doc = {
                userName: userId
            }
            db.save(doc)
            return True

def createUserDoc(couch,db_name="sanity"):

    db = couch[db_name]
    doc = {
    }
    db.save(doc)

    return doc['_id']

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

c=connect_couchdb()
addFunctionIfNotExist(c,"xyxxyxxyxxyx","Ashu")
#addUserIfNotExist(c,"Ashu")