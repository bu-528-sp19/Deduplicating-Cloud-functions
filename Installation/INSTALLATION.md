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
import os
from PIL import Image
from json import loads

def main(location):
  im = Image.open(location)
  im.thumbnail((120,120), Image.ANTIALIAS)
  image_path="thumbnail.jpg"
  im.save(image_path)
  print("Thumbnail generated thumbnail.jpg")
  return image_path

```

##### Create Dockerfile to load the python file and the dependency

##### Create an action called sprint using the Docker file containing the code
```
$ wsk -i action create sprint <docker hub path of the image>
```
```
ok: created action sprint
```
