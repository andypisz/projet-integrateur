#!/usr/bin/python3
# #coding: UTF-8


from subprocess import call

def mainElasticSearch():
    call('docker run --detach --name elasticsearch -p 9200:9200 -p 9300:9300 docker.elastic.co/elasticsearch/elasticsearch:6.5.4', shell=True)