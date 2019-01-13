from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists)

# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio('172.17.0.2:9000',
                    access_key='testaccesskey',
                    secret_key='testsecretkey',
                    secure=False)

# Get a full object and prints the original object stat information.

def get_data_from_minio(bucket, data):
	path = '/tmp/'+data
	try:
		minioClient.fget_object(bucket, data, path)
		print("File : ", bucket, "/" , data, " downloaded --> check " ,path)
	except ResponseError as err:
		print(err)
	return load(path)

