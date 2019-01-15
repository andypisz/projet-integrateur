#!/usr/bin/python3
# coding: UTF-8

import globalConstants
from subprocess import call

FIRST_PORT_NUMBER = globalConstants.docker_FIRST_PORT_NUMBER
ACCESS_KEY = globalConstants.docker_ACCESS_KEY
SECRET_KEY = globalConstants.docker_SECRET_KEY

def createNewDocker(name, port, accesskey, secretkey, volumeOption):
    portOption = port + ':' + str(FIRST_PORT_NUMBER)
    accessKeyOption = '"MINIO_ACCESS_KEY=' + accesskey + '"'
    secretKeyOption = '"MINIO_SECRET_KEY=' + secretkey + '"'
    command = 'docker run --detach ' + ' -p ' + portOption + ' --name ' + name + ' --env ' + accessKeyOption + ' --env ' + secretKeyOption + ' -v ' + volumeOption + ' minio/minio server /data'
    call(command, shell=True)


def createAllDockers(number):
    accesskey = ACCESS_KEY
    secretkey = SECRET_KEY
    print('number = '+str(number))
    for i in range(0, number):
        name = 'minio' + str(i)
        port = str(FIRST_PORT_NUMBER + i)
        volumeOption = '/mnt/data' + str(i) + ':/data'
        print('creating '+name)
        createNewDocker(name, port, accesskey, secretkey, volumeOption)
        print('created')