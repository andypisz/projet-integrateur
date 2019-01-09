from subprocess import call

def createNewDocker(name, port, accesskey, secretkey):
    portOption = port + ':' + port
    accessKeyOption = '"MINIO_ACCESS_KEY=' + accesskey + '"'
    secretKeyOption = '"MINIO_SECRET_KEY=' + secretkey + '"'
    call(['docker', 'run',
          '-p', portOption,
          '--name', name,
          '-e', accessKeyOption,
          '-e', secretKeyOption,
          '-v', '/mnt/data:/data',
          '-v', '/mnt/config:/root/.minio', 'minio/minio',
          'server', '/data'])
    #call(['docker', 'ps', '-a'])
    exit(0)