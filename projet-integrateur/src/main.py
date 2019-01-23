#!/usr/bin/python3
# coding: UTF-8

import docker
import file
import time
import minioManagement
import elasticSearch
import elasticSearchQueries

begin = time.time()

#Déploiement de l'architecture distribuée Minio
#Découpage des fichiers
totalNumberOfSubFiles = file.mainFile()
#Déploiement des conteneurs Minio
docker.mainDocker(totalNumberOfSubFiles)
#Upload des fichiers
minioManagement.mainMinio(totalNumberOfSubFiles)

#Indexation Elasticsearch
elasticSearch.mainElasticSearch()

#Requête sur elasticsearch et affichage des images
elasticSearchQueries.mainElasticSearchQuery()

end = time.time()
total = end - begin

print("temps total : "+str(total))