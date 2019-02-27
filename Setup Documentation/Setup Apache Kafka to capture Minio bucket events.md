# Steps to setup Apache Kafka to capture Minio bucket events


### Setup mc client


```
mkdir /home/mclient
docker export $(docker create shri4u/mc) | tar -C /home/mclient/ -xvf -
mv /home/mclient/mc /usr/local/bin/
```


### Setup Minio 
```
mkdir /mnt/config
mkdir /mnt/data
copy attached config file to /mnt/config
```
![alt text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Setup%20Documentation/Screenshots-Minio-Kafka/s2.JPG)


```git
git clone https://github.com/wurstmeister/kafka-docker.git
```




#### Install docker-compose (if you have not done it)
```
apt install docker-compose
```
####  Update docker-compose.yml and change ADVERTISE_HOST to local machine IP
![alt text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Setup%20Documentation/Screenshots-Minio-Kafka/s1.JPG)
![alt text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Setup%20Documentation/Screenshots-Minio-Kafka/s3.JPG)




```
docker-compose up –d
```


### Setup Kafka 
```
 docker run -it shri4u/kafkacat bash
```


#### Test your Kafka setup


##### Setup Kafka Producer with Topic test


###### The IP is your machine IP and port number can be checked using:




``` 
docker ps –a 
```
The port number is corresponding to your shri4u/kafkacat container


![alt text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Setup%20Documentation/Screenshots-Minio-Kafka/s4.JPG)


```
kafkacat -P -b 10.0.2.15:32768 -t test
```


##### Setup Kafka Consumer with Topic test
```
kafkacat -C -b 10.0.2.15:32768 -t test
```
![alt text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Setup%20Documentation/Screenshots-Minio-Kafka/s5.JPG)


#### Start the Minio Server


Open a new terminal


```
docker run -d -p 9000:9000 --name minio1   -v /mnt/data:/data   -v /mnt/config:/root/.minio   shri4u/minio server /data
```
```
docker logs minio1
```


Copy the line corresponding to add a host 
eg. 
```
mc config host add <ALIAS> <YOUR-S3-ENDPOINT> <YOUR-ACCESS-KEY> <YOUR-SECRET-KEY> <API-SIGNATURE>
```
Give it a name eg. myminio
![alt text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Setup%20Documentation/Screenshots-Minio-Kafka/s6.JPG)


Make a new bucket using:


```
mc mb --region=sanity-local myminio/test1
```








Setup the event
```
mc event add myminio/test1 arn:minio:sqs:sanity-local:1:kafka
```


![alt text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Setup%20Documentation/Screenshots-Minio-Kafka/s7.JPG)


#### Monitor the bucket events using Kafka


Open a new terminal


```
docker run -it shri4u/kafkacat bash
```


##### Set up a consumer with the topic name you have given in the config.json file eg.
in-bucket-notifications


```
kafkacat -C -b 10.0.2.15:32768 -t in-bucket-notifications
```




Go back to the previous terminal where you have myminio running


###### Create a new file


```
vi testfile
```








###### Copy it in the bucket


```
mc cp testfile myminio/test1
```
![alt text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Setup%20Documentation/Screenshots-Minio-Kafka/s8.JPG)
![alt text](https://github.com/bu-528-sp19/Deduplicating-Cloud-functions/blob/master/Setup%20Documentation/Screenshots-Minio-Kafka/s9.JPG)


#  You should be able to see this event being captured in the kafkacat terminal !
