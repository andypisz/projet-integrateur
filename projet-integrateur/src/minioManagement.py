#!/usr/bin/python3
# coding: UTF-8

from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists)
import globalConstants
import os


#Path of the folder containing all the files
FILES_PATH = globalConstants.file_FILES_PATH
IMAGES_PATH = globalConstants.file_IMAGES_PATH
SUBFILES_PATH = globalConstants.file_SUBFILES_PATH


#Get All files in the directory
ALL_FILES = os.listdir(SUBFILES_PATH)


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
        try:
            #minioClient.make_bucket('data', location="eu-west-1")
            print('bucketing')
        except BucketAlreadyOwnedByYou as err:
            pass
        except BucketAlreadyExists as err:
            pass
        except ResponseError as err:
            raise
        else:
            # Put an object 'test_RGB_0_10_25.npy' with contents from 'test_RGB_0_10_25.npy'.
            try:
                # minioClient.fput_object('images', 'test_RGB_0_10_25.npy',
                #                         '/home/hamid/Téléchargements/INSA_data_images/test_RGB_0_10_25.npy')
                print(ALL_FILES)
                print('Uploaded ' + 'data' + ' on ' + minio)
            except ResponseError as err:
                print(err)

def constructDictionnaryOfSubfiles():
    dictionnaryOfSubfiles = {}
    for file in ALL_FILES:
        print(os.listdir(SUBFILES_PATH+file))
        for subfile in os.listdir(SUBFILES_PATH+file):
            dictionnaryOfSubfiles[subfile] = SUBFILES_PATH+file+'/'+subfile
    return dictionnaryOfSubfiles

#dic = initializeAllMinio(22)
#uploadData(dic)
print(constructDictionnaryOfSubfiles())
