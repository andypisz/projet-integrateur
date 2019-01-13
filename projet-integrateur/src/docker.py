from subprocess import call
import time

FIRST_PORT_NUMBER = 9000

def createNewDocker(name, port, accesskey, secretkey):
    portOption = port + ':' + port
    accessKeyOption = '"MINIO_ACCESS_KEY=' + accesskey + '"'
    secretKeyOption = '"MINIO_SECRET_KEY=' + secretkey + '"'
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