from docker import *
from file import *

#createNewDocker("testminioscript2", "9001", "accesskey", "secretkey")
allNumberOfSubFiles = get_number_of_sub_files()
totalNumberOfSubFiles = get_total_number_of_sub_files(allNumberOfSubFiles)
print(totalNumberOfSubFiles)

#createAllDockers(15)