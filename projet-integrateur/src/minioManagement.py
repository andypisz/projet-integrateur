#!/usr/bin/python3
# coding: UTF-8

from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists)
import globalConstants
import os
import time


#Path of the folder containing all the files
FILES_PATH = globalConstants.file_FILES_PATH
IMAGES_PATH = globalConstants.file_IMAGES_PATH
SUBFILES_PATH = globalConstants.file_SUBFILES_PATH


#Get All files in the directory
ALL_FILES = os.listdir(SUBFILES_PATH)


ip_adress = globalConstants.minio_IP_ADRESS
bucket_name = globalConstants.minio_BUCKET_NAME

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
    dictionnaryOfSubFiles = constructDictionnaryOfSubfiles()
    for minio, subfile in zip(dictionnaryOfMinio, dictionnaryOfSubFiles):
        minioClient = dictionnaryOfMinio[minio]
        try:
            minioClient.make_bucket(bucket_name, location="eu-west-1")
            print('bucketing')
        except BucketAlreadyOwnedByYou as err:
            print(err)
        except ResponseError as err:
            print(err)
        try:
            minioClient.fput_object(bucket_name, subfile, dictionnaryOfSubFiles[subfile])
            print('Uploaded ' + subfile + ' on ' + minio)
        except ResponseError as err:
            print(err)

def constructDictionnaryOfSubfiles():
    dictionnaryOfSubfiles = {}
    for file in ALL_FILES:
        for subfile in os.listdir(SUBFILES_PATH+file):
            dictionnaryOfSubfiles[subfile] = SUBFILES_PATH+file+'/'+subfile
    return dictionnaryOfSubfiles


def mainMinio(totalNumberOfSubFiles):
    dictionnaryOfMinios = initializeAllMinio(totalNumberOfSubFiles)

    begin_upload = time.time()
    uploadData(dictionnaryOfMinios)
    end_upload = time.time()
    print('\n(Time for upload : ' + str(end_upload - begin_upload) + ' seconds)')