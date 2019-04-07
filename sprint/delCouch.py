import couchdb

def connect_couchdb():
    couch = couchdb.Server("http://52.116.33.131:5984")
    return couch

def delete(couch):
    del couch['sanity']

if __name__ == "__main__":
    couch = connect_couchdb()
    delete(couch)

