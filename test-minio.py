#!/usr/bin/python3
# Import Minio library.
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists)
from matplotlib import pyplot as plt 
from numpy import load
from subprocess import call

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

test_images = get_data_from_minio('images', 'test_RGB_0_10_25.npy')
test_labels = get_data_from_minio('labels', 'test_labels_0_10_25.npy')
#train_images = get_data_from_minio('images', 'train_RGB_0_10_25.npy')
#train_labels = get_data_from_minio('labels', 'train_labels_0_10_25.npy')

plt.imshow(test_images[0]*4.5,alpha=0.85,interpolation="spline36")
plt.show()

call(["rm","-f","/tmp/test_RGB_0_10_25.npy"])
call(["rm","-f","/tmp/test_labels_0_10_25.npy"])
