#!/usr/bin/python3
# coding: UTF-8

import os
from math import ceil, floor
from numpy import load, save, arange
from subprocess import call
import globalConstants
import time
import re

#Path of the folder containing all the files
FILES_PATH = globalConstants.file_FILES_PATH
IMAGES_PATH = globalConstants.file_IMAGES_PATH
SUBFILES_PATH = globalConstants.file_SUBFILES_PATH


#Get All files in the directory
ALL_DIRECTORIES = os.listdir(IMAGES_PATH)
ALL_FILES = os.listdir(IMAGES_PATH)

#Size max of the file we want on a docker container : 250 MB
SIZE = globalConstants.file_SIZE


#Function to calculate how many subfiles of approximately 250MB we will have to do for a specific file, given by its path
#Return an int
def get_number_of_sub_files(path):
    size = os.path.getsize(path)
    if (size < SIZE):
        return 1
    else:
        return int(ceil(size/SIZE))



#Function to calculate, for every file
# Return a dictionnary with the name of a file as a key and the number of subiles corresponding as value
def get_all_number_of_sub_files():
    allNumberOfSubFiles = {}
    for directory in ALL_DIRECTORIES:
        directoryPath = IMAGES_PATH+directory
        for file in os.listdir(directoryPath):
            if (re.match(".*RGB.*",file)):
                filePath = directoryPath+'/'+file
        allNumberOfSubFiles[file] = get_number_of_sub_files(filePath)
    return allNumberOfSubFiles



#Function to calculate the total number of subfiles to create, from the dictionnary given by the previous function
#Return an int
def get_total_number_of_sub_files(allNumberOfSubFiles):
    total = 0
    for value in allNumberOfSubFiles.values():
        total += value
    return total



#Function to import all the files
#Return a dictionnary with the name of the file as key and the imported array as value
#Return a second dictionnary with the name ofthe directory (usually an int) and an array containing the 2 names of the label and RGB files as value
def import_files():
    dictionnaryOfFiles = {}
    directoryFiles = {}
    for directory in ALL_DIRECTORIES:
        directoryPath = IMAGES_PATH+directory
        i = 0
        for file in os.listdir(directoryPath):
            #if(file != 'train_RGB_0_10_25.npy'):
            filePath = directoryPath + '/' + file
            dictionnaryOfFiles[file] = load(filePath)
            print('loaded: '+file)
            i+=1
            if (i==1):
                firstFile = file
            elif(i==2):
                secondFile = file
                directoryFiles[directory] = [firstFile, secondFile]
    return dictionnaryOfFiles, directoryFiles



#Function to divide all the files into subfiles and put them into the good directories
#Return the total number of subfiles
def divide_files(dictionnaryOfFiles):
    check_subfiles_directory_existance_and_create()
    allNumberOfSubFiles = get_all_number_of_sub_files()
    for file in dictionnaryOfFiles:
        print("\n*** Working on : "+file+" ***\n")
        numberOfSubFile = allNumberOfSubFiles[file]
        print('number of sub files to create : '+str(numberOfSubFile))
        if(numberOfSubFile == 1):
            newPath = SUBFILES_PATH+file
            call(["mkdir", newPath])
            savePath = newPath+'/'+file
            save(savePath, dictionnaryOfFiles[file])
            print('created 1/1')
        else:
            newPath = SUBFILES_PATH + file
            call(["mkdir", newPath])
            lengthOfSubFile = int(ceil(len(dictionnaryOfFiles[file])/numberOfSubFile))
            print('total length : '+str(len(dictionnaryOfFiles[file])))
            print('subfiles length : '+str(lengthOfSubFile))
            for j in range (0, numberOfSubFile):
                #premiere boucle : de 0 a 8561-1, deuxieme : de 8561 à 8561*2-1, troisieme : de 8561*2 à 8561*3-1 ...
                startIndex = lengthOfSubFile*j
                endIndex = lengthOfSubFile*(j+1)
                if (endIndex >= len(dictionnaryOfFiles[file])):
                    endIndex = len(dictionnaryOfFiles[file])
                indexes = arange(startIndex, endIndex)
                filearray = dictionnaryOfFiles[file]
                print('start : '+str(indexes[0])+' / end : '+str(indexes[-1]))
                subfilearray = [ filearray[index] for index in indexes ]
                savePath = newPath + '/' + str(j) + file
                save(savePath, subfilearray)
                print('created '+str(j+1)+'/'+str(numberOfSubFile))
    return allNumberOfSubFiles



#Function to check if the subfiles directory exist, to create anew one
def check_subfiles_directory_existance_and_create():
    directories = os.listdir(FILES_PATH)
    directoryPath = FILES_PATH+"Subfiles"
    for directory in directories:
        if(directory == "Subfiles"):
            call(["rm", "-rf", directoryPath])
    call(["mkdir", directoryPath])



#Function that use all the previous functions for the project
def mainFile():
    begin_import = time.time()
    dictionnaryOfFiles = import_files()
    end_import = time.time()
    print('\n(Time for import : ' + str(end_import-begin_import) + ' seconds)')

    begin_divide = time.time()
    allNumberOfSubFiles = divide_files(dictionnaryOfFiles)
    end_divide = time.time()
    print('\n(Time for creating subfiles : ' + str(end_divide - begin_divide) + ' seconds)')

    return get_total_number_of_sub_files(allNumberOfSubFiles)

all = get_all_number_of_sub_files()
print(get_total_number_of_sub_files(all))
dicOfFiles, directoryFiles = import_files()
print(directoryFiles)





