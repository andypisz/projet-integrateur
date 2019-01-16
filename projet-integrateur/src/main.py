#!/usr/bin/python3
# coding: UTF-8

import docker
import file
import time
import minioManagement

begin = time.time()

totalNumberOfSubFiles = file.mainFile()
docker.mainDocker(totalNumberOfSubFiles)
minioManagement.mainMinio(totalNumberOfSubFiles)

end = time.time()
total = end - begin

print("temps total : "+str(total))