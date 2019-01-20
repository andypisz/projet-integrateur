#!/usr/bin/python3
# #coding: UTF-8

from elasticsearch import Elasticsearch
import globalConstants

def checkNumberOfResults(index, size):
    total = 0
    allNumberOfResults = {}
    allResults = {}
    for i in range(5):
        res = es.search(index=index, body={"from": 0, "size": size, "query": {"match": {'value': i}}})
        print("value : "+str(i))
        numberOfResults = res['hits']['total']
        allNumberOfResults[i] = numberOfResults
        allResults[i] = res['hits']['hits']
        total = total+numberOfResults
        print("%d results found" % numberOfResults)
    print("\nTotal : "+str(total)+"\n")
    return allNumberOfResults, allResults

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


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


es.indices.put_settings(index="test_labels",
                        body={"index" : {
                                "max_result_window" : globalConstants.elasticsearch_TEST_LENGTH
                              }})
allNumberOfResultsTest, allResultsTest = checkNumberOfResults("test_labels", globalConstants.elasticsearch_TEST_LENGTH)
dictionnaryOfArraysOfIdsTest = makeArraysOfIds(allResultsTest)



es.indices.put_settings(index="train_labels",
                        body={"index" : {
                                "max_result_window" : globalConstants.elasticsearch_TRAIN_LENGTH
                              }})
allNumberOfResultsTrain, allResultsTrain = checkNumberOfResults("train_labels", globalConstants.elasticsearch_TRAIN_LENGTH)
dictionnaryOfArraysOfIdsTrain = makeArraysOfIds(allResultsTrain)