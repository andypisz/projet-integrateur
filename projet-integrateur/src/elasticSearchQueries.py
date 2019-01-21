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

def mainQuery(index, length):
    es.indices.put_settings(index=index,
                            body={"index": {
                                "max_result_window": length
                            }})
    allNumberOfResultsTest, allResultsTest = checkNumberOfResults(index, length)
    return makeArraysOfIds(allResultsTest)



es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


dictionnaryOfArraysOfIdsTest = mainQuery("test_labels", globalConstants.elasticsearch_TEST_LENGTH)
dictionnaryOfArraysOfIdsTrain = mainQuery("train_labels", globalConstants.elasticsearch_TRAIN_LENGTH)