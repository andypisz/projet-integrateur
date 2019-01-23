# projet-integrateur

## Organisation des scripts

Il y a un script pour chaque partie du projet.
Pour lancer la mise en place de l'architecture disribuée, puis l'indexation elasticsearch et enfin une requête sur elasticsearh qui aboutira sur l'affichage de 10 images ayant le label "urban area", il suffit de lancer le script python nommé "main.py", après avoir modifié les variables globales pour s'adapter à l'environnement (voir "Mise en place de l'environnement") :

```bash python main.py```

## Fonctionnalité de chaque script :

### main.py

Exécuter les fonctions "main" de chacun des sous scripts, afin de :
  - Mettre en place l'architecture distribuée Minio
  - Indexer dans Elasticsearch
  - Faire une requête sur Elasticsearch
  
  
### file.py
  
Importer les fichiers, les découper et placer les sous-fichiers dans des répertoires correspondant à chaque conteneur Minio.


### docker.py

Déployer tous les containers minio


### minioManagement.py

Créer tous les buckets, sur chaque Minio, puis uploader les fichiers conteneur par conteneur.


### elasticSearch.py

Changer le format des tableaux de label afin de ne plus avoir un tableau de tableaux contenant quatre zéro et un un à un indice compris entre 0 et 4 (définissant le type de photographie), mais plutôt un tableau contenant une valeur entre 0 et 4 pour chaque label. Puis, indexer les valeurs dans Elasticsearch avec l'id correspondant à l'indice du label (et de l'image) et en body, une valeur entre 0 et 4, la valeur du label.


### elasticSearchQueries.py

Lancer des requêtes sur Elasticsearch, pour récupérer un dictionnaire ayant pour clé la valeur que l'on cherche (pour les labels, entre 0 et 4), et en valeur un tableau contenant tous les indices des images qui ont le label cherché.
Puis on appelle le script image.py, pour afficher les 10 premières images ayant pour label 0, grâce au tableau d'indice renvoyé par nos requêtes sur Elasticsearch.


### image.py

Script pour afficher des images grâce à la librairie matplotlib.pyplot.


### globalConstants.py

Un script regroupant l'ensemble des variables que l'on peut utiliser dans les différents scripts, afin de pouvoir les modifier facilement, notamment pour la mise en place de l'environnement

### clean.py

Script annexe au projet, permettant de nettoyer après de tests. Il faut lui donner en argumant le nombre de conteneurs Minio que l'on a créé pour qu'il les supprime tous.


## Mise en place de l'environnement

Il faut mettre en place les répertoires contenant les fichiers (images et labels de test et de train) de la façon suivante pour le bon déroulement des scripts :

Images > Original_images > 1 > fichiers de test (labels et images)
Images > Images_originales > 2 > fichiers de train (labels et images)

Pour mettre en place l'environnement, il faut modifier la variable suivante dans le script globalConstants.py :
  - file_FILES_PATH : chemin absolu du répertoire "Images" (voir ci-dessus)
