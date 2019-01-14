#!/usr/bin/python3
# coding: UTF-8

from subprocess import call

FIRST_PORT_NUMBER = 9000

def createNewDocker(name, port, accesskey, secretkey):
    portOption = port + ':' + str(FIRST_PORT_NUMBER)
    accessKeyOption = '"MINIO_ACCESS_KEY=' + accesskey + '"'
    secretKeyOption = '"MINIO_SECRET_KEY=' + secretkey + '"'
    print(accessKeyOption)
    print(secretKeyOption)
    call(['docker', 'run',
          '--detach',
          '-p', portOption,
          '--name', name,
          '-e', accessKeyOption,
          '-e', secretKeyOption,
          '-v', '/mnt/data:/data',
          '-v', '/mnt/config:/root/.minio', 'minio/minio',
          'server', '/data'])
    #call(['docker', 'ps', '-a'])

def createAllDockers(number):
    accesskey = 'accesskey'
    secretkey = 'secretkey'
    print('number = '+str(number))
    for i in range(0, number):
        name = 'minio' + str(i)
        port = str(FIRST_PORT_NUMBER + i)
        print('creating '+name)
        createNewDocker(name, port, accesskey, secretkey)
        print('created')