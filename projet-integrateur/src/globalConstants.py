

#file constants
file_FILES_PATH = '/home/andy/Desktop/INSA/5A/projet-integrateur/INSA_data_images/'
file_IMAGES_PATH = file_FILES_PATH+'Original_Images/'
file_SUBFILES_PATH = file_FILES_PATH+'Subfiles/'
#Size max of the file we want on a docker container : 250 MB
file_SIZE = 250000000

#docker constants
docker_FIRST_PORT_NUMBER = 90
docker_ACCESS_KEY = 'accesskey'
docker_SECRET_KEY = 'secretkey'

#minio constants
minio_IP_ADRESS = '127.0.0.1'