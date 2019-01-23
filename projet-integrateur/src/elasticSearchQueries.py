#!/usr/bin/python3
# #coding: UTF-8

from elasticsearch import Elasticsearch
import globalConstants
import image

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

def checkNumberOfResults(index, size):
    allNumberOfResults = {}
    allResults = {}
    for i in range(5):
        res = es.search(index=index, body={"from": 0, "size": size, "query": {"match": {'value': i}}})
        numberOfResults = res['hits']['total']
        allNumberOfResults[i] = numberOfResults
        allResults[i] = res['hits']['hits']
    return allNumberOfResults, allResults


def printNumberOfResults(allNumberOfResults):
    total = 0
    for i in range(5):
        print("value : " + str(i))
        print("%d results found" % allNumberOfResults[i])
        total = total+allNumberOfResults[i]
    print("\nTotal : "+str(total)+"\n")


def makeArraysOfIds(allResults):
    dictionnaryOfArraysOfIds = {}
    for key in allResults:
        newArray = []
        length = len(allResults[key])
        for i in range(length):
            id = allResults[key][i]['_id']
            newArray.append(id)
        dictionnaryOfArraysOfIds[key] = newArray
    return dictionnaryOfArraysOfIds

def query(index, length):
    es.indices.put_settings(index=index,
                            body={"index": {
                                "max_result_window": length
                            }})
    allNumberOfResultsTest, allResultsTest = checkNumberOfResults(index, length)
    printNumberOfResults(allNumberOfResultsTest)
    return makeArraysOfIds(allResultsTest)


def mainElasticSearchQuery():
    dictionnaryOfArraysOfIdsTest = query("test_labels", globalConstants.elasticsearch_TEST_LENGTH)
    #dictionnaryOfArraysOfIdsTrain = mainQuery("train_labels", globalConstants.elasticsearch_TRAIN_LENGTH)
    image.mainImage(globalConstants.elasticsearch_TEST_RGB_PATH, globalConstants.elasticsearch_TEST_LABEL_PATH, dictionnaryOfArraysOfIdsTest[0])
