#!/usr/bin/python3
# coding: UTF-8

import docker
import file
import time
import minioManagement

begin = time.time()

allNumberOfSubFiles = file.get_all_number_of_sub_files()
totalNumberOfSubFiles = int(file.get_total_number_of_sub_files(allNumberOfSubFiles))

#print('totalNumberOfSubFiles: '+str(totalNumberOfSubFiles))

#dictionnaryOfFiles = file.import_files()
#file.divide_files(dictionnaryOfFiles)


docker.createAllDockers(totalNumberOfSubFiles)
dictionnaryOfMinios = minioManagement.initializeAllMinio(totalNumberOfSubFiles)
print(dictionnaryOfMinios)
minioManagement.uploadData(dictionnaryOfMinios)


end = time.time()
total = end - begin

print("temps total : "+str(total))