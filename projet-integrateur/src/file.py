#!/usr/bin/python3
# coding: UTF-8

import os
from math import ceil
from numpy import load
from numpy import save
from numpy import arange
from subprocess import call
import globalConstants
import time

#Path of the folder containing all the files
FILES_PATH = globalConstants.file_FILES_PATH
IMAGES_PATH = globalConstants.file_IMAGES_PATH
SUBFILES_PATH = globalConstants.file_SUBFILES_PATH


#Get All files in the directory
ALL_FILES = os.listdir(IMAGES_PATH)

#Size max of the file we want on a docker container : 250 MB
SIZE = globalConstants.file_SIZE


def get_number_of_sub_files(path):
    size = os.path.getsize(path)
    if (size < SIZE):
        return 1
    else:
        return int(ceil(size/SIZE))


def get_all_number_of_sub_files():
    allNumberOfSubFiles = {}

    for file in ALL_FILES:
        filePath = IMAGES_PATH+file
        allNumberOfSubFiles[file] = get_number_of_sub_files(filePath)

    return allNumberOfSubFiles

def get_total_number_of_sub_files(allNumberOfSubFiles):
    total = 0
    for value in allNumberOfSubFiles.values():
        total += value
    return total

def import_files():
    dictionnaryOfFiles = {}
    for file in ALL_FILES:
        #if(file != 'train_RGB_0_10_25.npy'):
        filePath = IMAGES_PATH + file
        dictionnaryOfFiles[file] = load(filePath)
        print('loaded: '+file)
    return dictionnaryOfFiles

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

def check_subfiles_directory_existance_and_create():
    directories = os.listdir(FILES_PATH)
    directoryPath = FILES_PATH+"Subfiles"
    for directory in directories:
        if(directory == "Subfiles"):
            call(["rm", "-rf", directoryPath])
    call(["mkdir", directoryPath])


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



