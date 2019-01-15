#!/usr/bin/python3
# coding: UTF-8

from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists)
import globalConstants


ip_adress = globalConstants.minio_IP_ADRESS

def initializeMinio(endpoint):
    # Initialize minioClient with an endpoint and access/secret keys.
    minioClient = Minio(endpoint,
                        access_key=globalConstants.docker_ACCESS_KEY,
                        secret_key=globalConstants.docker_SECRET_KEY,
                        secure=False)
    return minioClient


def initializeAllMinio(numberOfMinio):
    dictionnaryOfMinio = {}
    for i in range (0, numberOfMinio):
        endpoint = ip_adress+':'+str(globalConstants.docker_FIRST_PORT_NUMBER+i)
        minioName = 'minio' + str(i)
        print("Initializing minio client : "+minioName)
        minioClient = initializeMinio(endpoint)
        dictionnaryOfMinio[minioName] = minioClient
    return dictionnaryOfMinio

def uploadData(dictionnaryOfMinio):
    for minio in dictionnaryOfMinio:
        minioClient = dictionnaryOfMinio[minio]
        minioClient.make_bucket('data', location="eu-west-1")
        print("Uploading data on "+minio)


