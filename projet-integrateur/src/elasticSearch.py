#!/usr/bin/python3
# #coding: UTF-8

from subprocess import call
from elasticsearch import Elasticsearch
import globalConstants
import os
from numpy import load
import json


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

def createJsonBody(array):
    data = []
    i = 0
    for value in array:
        label = {}
        label["index"]=i
        label["value"]=value
        data.append(label)
        if (i==900):
            break
        i+=1
    return json.dumps({"labels": data})


def mainElasticSearch():
    #call('docker run --detach --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.5.4', shell=True)
    es = Elasticsearch("localhost:9200")
    testArray = modifyLabelsArray(globalConstants.elasticsearch_TEST_LABEL_PATH)
    #trainArray = modifyLabelsArray(globalConstants.elasticsearch_TRAIN_LABEL_PATH)
    testBody = createJsonBody(testArray)
    #trainBody = createJsonBody(trainArray)
    es.indices.delete("test_index", ignore=[400, 404])
    es.indices.delete("labels", ignore=[400, 404])
    es.indices.create(index="labels", body=json.dumps({
        "mappings": {
            "label": {
                "properties": {
                    "labels": {
                        "type": "nested",
                        "properties": {
                            "index": {"type": "keyword"},
                            "value": {"type": "keyword"}
                        }
                    }
                }
            }
        }
    }))
    print(es.index(index="labels", doc_type="label", id=1, body=testBody, ignore=400))
    print(es.get(index="labels", doc_type="label", id=1))
    print(es.search(index="labels", body=json.dumps({
        "query": {
            "nested": {
                "path": "labels",
                "query": {
                    "bool": {
                        "must": [
                            {"match": {"labels.value": "1"}}
                        ]
                    }
                }
            }
        }
    })))



mainElasticSearch()