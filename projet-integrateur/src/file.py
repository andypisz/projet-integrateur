import os
from math import ceil
from numpy import load

#Path of the folder containing all the files
FILES_PATH = '/home/andy/Desktop/INSA/5A/projet-integrateur/INSA_data_images/'

#Get All files in the directory
ALL_FILES = os.listdir(FILES_PATH)

#Size max of the file we want on a docker container : 250 MB
SIZE = 250000000


def divide_file(path):
    size = os.path.getsize(path)
    if (size < SIZE):
        return 1
    else:
        return ceil(size/SIZE)


def get_number_of_sub_files():
    allNumberOfSubFiles = {}

    for file in ALL_FILES:
        filePath = FILES_PATH+file
        allNumberOfSubFiles[filePath] = divide_file(filePath)

    return allNumberOfSubFiles

def get_total_number_of_sub_files(dic):
    total = 0
    for value in dic.values():
        total += value
    return total

def import_files():
    dictionnaryOfFiles = {}
    for file in ALL_FILES:
        if(file != 'train_RGB_0_10_25.npy'):
            filePath = FILES_PATH + file
            dictionnaryOfFiles[file] = load(filePath)
            print('loaded: '+file)
    return dictionnaryOfFiles

