** **

# Installation 

### Steps
-   Setup python 3.0 in the first VM
-   Configure Kafka, Minio and Couch db in first VM
-   Configure OpenWhisk in second VM
-   Connect two VMs.Click [here](Openwhiskvm.md) for the setup

### Configure
##### Ubuntu User
- [Setup Python](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04)
- [Setup and Connect Kafka and Minio](kafka-minio.md)
- [Setup Couch db](https://github.com/apache/couchdb-docker/blob/master/README.md)
- [Setup OpenWhisk](https://github.com/apache/incubator-openwhisk/blob/master/ansible/README.md)

### Getting started
##### Install all the Sanity dependencies
```
pip3 install couchdb
pip3 install docopt
pip3 install kafka
pip3 install minio
```
##### Clone the Github [Repository](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions.git)
```
git clone https://github.com/bu-528-sp19/Deduplicating-Cloud-functions.git 
```

##### Change the directory
```
cd Deduplicating-Cloud-functions
cd sanity/final
```

##### Run the CLI
```
python3 sanity.py --i <INPUT_BUCKET_NAME> --o <OUTPUT_BUCKET_NAME> --f <FUNCTION_NAME> --u <USER NAME>
```

#####

