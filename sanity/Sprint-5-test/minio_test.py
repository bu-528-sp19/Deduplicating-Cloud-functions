from connectMinio import connect_minio,createBucket

mc = connect_minio()
createBucket(mc,"input")
