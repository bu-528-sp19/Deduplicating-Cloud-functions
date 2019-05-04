** **

# Installation 

### Steps
-   Setup python 3.0 in the first VM
-   [Configure](#configure) Kafka, Minio and Couch db in first VM
-   [Configure](#configure) OpenWhisk in second VM
-   Connect two VMs.Click [here](Openwhiskvm.md) for the setup
-   Create a function, you want to deploy in OpenWhisk. Click [here](#steps-for-creating-a-function-in-openWhisk) for the setup
-   Use the above created action name while running CLI as **function name**
-   Follow [Getting started](#getting-started) for running the sanity

** **

### Configure
##### Ubuntu User
- [Setup Python](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04)
- [Setup and Connect Kafka and Minio](kafka-minio.md)
- [Setup Couch db](https://github.com/apache/couchdb-docker/blob/master/README.md)
- [Setup OpenWhisk](https://github.com/apache/incubator-openwhisk/blob/master/ansible/README.md)

** **

### Getting started
##### Install all the Sanity dependencies
```
$ pip3 install couchdb
$ pip3 install docopt
$ pip3 install kafka
$ pip3 install minio
$ pip3 install requests   
```
##### Clone the Github [Repository](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions.git)
```
$ git clone https://github.com/bu-528-sp19/Deduplicating-Cloud-functions.git 
```

##### Change the directory
```
$ cd Deduplicating-Cloud-functions
$ cd sanity/final
```

##### Run the CLI
```
$ python3 sanity.py --i <INPUT_BUCKET_NAME> --o <OUTPUT_BUCKET_NAME> --f <FUNCTION_NAME> --u <USER NAME>
```
![alt_text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Installation/1.PNG)
 
##### Add one file to the input bucket
![alt_text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Installation/2.PNG)

##### Unique Data
![alt_text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Installation/3.PNG)

##### De duplication effect
![alt_text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Installation/4.PNG)

![alt_text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Installation/5.PNG)
** **
### Steps for creating a function in OpenWhisk

##### Create a file named thumbnail.py
```
import sys
import requests
from minio import Minio
import os
from minio.error import ResponseError
from PIL import Image
from json import loads

client = Minio('52.116.33.131:9000',
               access_key='sanity',
               secret_key='CloudforAll!',
               secure=False)
try:
    client.fget_object(bucket_name, file_name, 'local.jpg')
except ResponseError as err:
    print(err)

im = Image.open('local.jpg')
im.thumbnail((120,120), Image.ANTIALIAS)
im.save("thumbnail.jpg")
print("Thumbnail generated thumbnail.jpg")

try:
    client.fput_object('test2', 'thumbnail.jpg','thumbnail.jpg')
except ResponseError as err:
    print(err)
```

##### Create an action called sprint using thumbnail.py
```
$ wsk -i action create sprint thumbnail.py
```
```
ok: created action sprint
```
