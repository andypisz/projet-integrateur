import docker
import file
#docker.createNewDocker("testminioscript2", "9001", "accesskey", "secretkey")
allNumberOfSubFiles = file.get_number_of_sub_files()
totalNumberOfSubFiles = int(file.get_total_number_of_sub_files(allNumberOfSubFiles))

print('totalNumberOfSubFiles: '+str(totalNumberOfSubFiles))

#print(len(file.import_files().keys()))

docker.createAllDockers(totalNumberOfSubFiles)