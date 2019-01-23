#!/usr/bin/python3
# #coding: UTF-8

from subprocess import call
from elasticsearch import Elasticsearch
import globalConstants
import os
from numpy import load
import json
import time


def initializeIndexes(es):
    es.index(index='test_index', doc_type='post', id=1, body={
        'author': 'John Doe',
        'blog': 'Learning Elasticsearch',
        'title': 'Using Python with Elasticsearch',
        'tags': ['python', 'elasticsearch', 'tips'],
    })
    print(es.get(index="test_index", doc_type='post', id=1))
    print(es.search(index='test_index', body={
        'query': {
            'match': {
                'title': 'Python',
            }
        }
    }))

def modifyLabelsArray(path):
    labels = load(path)
    new_labels = []
    for label in labels:
        for i in range (5):
            if (label[i] == 1):
                label_value = i
                new_labels.append(label_value)
                break
    return new_labels

def createIndices(es, indexName, array):
    i = 0
    es.indices.create(index=indexName)
    for value in array:
        #print(str(i)+' // '+str(value))
        es.index(index=indexName, doc_type='label', id=i, body={'value': value})
        i += 1
    print(i)



def mainElasticSearch():
    call('docker run --detach --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.5.4', shell=True)
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    testArray = modifyLabelsArray(globalConstants.elasticsearch_TEST_LABEL_PATH)
    trainArray = modifyLabelsArray(globalConstants.elasticsearch_TRAIN_LABEL_PATH)
    #es.indices.delete(index='test_labels', ignore=[400, 404])

    begin_test = time.time()
    createIndices(es, 'test_labels', testArray)
    end_test = time.time()
    print('\n(Time for test index : ' + str(end_test - begin_test) + ' seconds)')

    begin_train = time.time()
    createIndices(es, 'train_labels', trainArray)
    end_train = time.time()
    print('\n(Time for train index : ' + str(end_train - begin_train) + ' seconds)')

    #print(es.get(index='test_labels', doc_type='label', id=1))
    #print(es.search(index="test_labels", body={"query": {"match": {'value': 2}}}))


