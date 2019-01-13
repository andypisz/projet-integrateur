import docker
import file
import time

begin = time.time()

allNumberOfSubFiles = file.get_all_number_of_sub_files()
totalNumberOfSubFiles = int(file.get_total_number_of_sub_files(allNumberOfSubFiles))

#print('totalNumberOfSubFiles: '+str(totalNumberOfSubFiles))

dictionnaryOfFiles = file.import_files()

file.divide_files(dictionnaryOfFiles)

#print(len(file.import_files().keys()))

#docker.createAllDockers(totalNumberOfSubFiles)


end = time.time()
total = end - begin

print("temps total : "+str(total))