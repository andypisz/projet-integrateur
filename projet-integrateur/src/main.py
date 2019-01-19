#!/usr/bin/python3
# coding: UTF-8

import docker
import file
import time
import minioManagement

begin = time.time()

#allNumberOfSubFiles = file.get_all_number_of_sub_files()
#totalNumberOfSubFiles = file.get_total_number_of_sub_files(allNumberOfSubFiles)
#minioManagement.editConfigForElasticSearch(totalNumberOfSubFiles)
totalNumberOfSubFiles = file.mainFile()
docker.mainDocker(totalNumberOfSubFiles)
minioManagement.mainMinio(totalNumberOfSubFiles)

end = time.time()
total = end - begin

print("temps total : "+str(total))