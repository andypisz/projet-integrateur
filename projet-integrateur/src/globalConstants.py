

#file constants
file_FILES_PATH = '/home/andy/Desktop/INSA/5A/projet-integrateur/INSA_data_images/'
file_IMAGES_PATH = file_FILES_PATH+'Original_Images/'
file_SUBFILES_PATH = file_FILES_PATH+'Subfiles/'
#Size max of the file we want on a docker container : 250 MB
file_SIZE = 250000000

#docker constants
docker_FIRST_PORT_NUMBER = 9000
docker_ACCESS_KEY = 'accesskey'
docker_SECRET_KEY = 'secretkey'

#minio constants
minio_IP_ADRESS = '127.0.0.1'
minio_BUCKET_NAME = 'data'
minio_CONFIG_PATH_START = '/mnt/data'
minio_CONFIG_END_PATH = '/.minio.sys/config/config.json'

#elasticsearch constants
elasticsearch_TEST_LABEL_PATH = file_IMAGES_PATH+'1/test_labels_0_10_25.npy'
elasticsearch_TEST_RGB_PATH = file_IMAGES_PATH+'1/test_RGB_0_10_25.npy'
elasticsearch_TRAIN_LABEL_PATH = file_IMAGES_PATH+'2/train_labels_0_10_25.npy'
elasticsearch_TRAIN_RGB_PATH = file_IMAGES_PATH+'2/train_RGB_0_10_25.npy'
elasticsearch_TEST_LENGTH = 42805
elasticsearch_TRAIN_LENGTH = 171222