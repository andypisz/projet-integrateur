#!/usr/bin/python3
from numpy import load
from matplotlib import pyplot as plt 
from random import randint as rand
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists)
from subprocess import call


# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio('172.17.0.2:9000',
                    access_key='testaccesskey',
                    secret_key='testsecretkey',
                    secure=False)


#Importation des donnees 
#test_labels = load("./test_labels_0_10_25.npy")
#train_labels = load("./train_labels_0_10_25.npy")
#test_RGB = load("./test_RGB_0_10_25.npy")
#train_RGB = load("./train_RGB_0_10_25.npy")
def get_data_from_minio(bucket, data):
	path = '/tmp/'+data
	try:
		minioClient.fget_object(bucket, data, path)
		print("File : ", bucket, "/" , data, " downloaded --> check " ,path) 
	except ResponseError as err:
		print(err)
	return load(path)

test_RGB = get_data_from_minio('images', 'test_RGB_0_10_25.npy')
test_labels = get_data_from_minio('labels', 'test_labels_0_10_25.npy')
#train_RGB = get_data_from_minio('images', 'train_RGB_0_10_25.npy')
#train_labels = get_data_from_minio('labels', 'train_labels_0_10_25.npy')



#parametres imshow, trouves suite a nos tests :
imshow_alpha = 0.85
imshow_interpolation = "spline36"
imshow_facteur_rgb = 4.5


#Les 5 classes de labels :
labels = ["urban area", "agricultural territory", "forests", "wetlands", "surfaces with water"]


### Tests ###

#Tableau contenant l'ensemble des valeurs possibles pour le paraetre interpolation de la fonction matplotlip.pyplot.imshow
interpolations = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

#Test de toutes les valeurs possibles d'interpolation sur la 256eme image
def test_interpolation(num_image):
    for interpolation in interpolations:
        print("interpolation : ",interpolation)
        plt.imshow(train_RGB[num_image]*imshow_facteur_rgb,alpha=imshow_alpha, interpolation=interpolation) 
        plt.show() 
        
#test_interpolation(10485)
#Resultat : le meilleur semble etre spline36

        
def test_alpha():
    for alpha in range (5,105,5):
        print("alpha : ",alpha/100)
        plt.imshow(train_RGB[10485]*imshow_facteur_rgb,alpha=alpha/100, interpolation=imshow_interpolation) 
        plt.show() 
        
#test_alpha()
#Resultat : le meilleur alpha semble etre 0.85
        
def test_facteur_rgb():
    for i in range (1,16) :
        print("facteur rgb : ",i)
        plt.imshow(test_RGB[256]*i,alpha=1, interpolation=imshow_interpolation) 
        plt.show() 
        
#test_facteur_rgb()
#Resultat : le meilleur semble etre compris entre 4 et 5

def test_facteur_rgb2():
    for i in range (40,51) :
        print("facteur rgb : ",i/10)
        plt.imshow(test_RGB[256]*i/10,alpha=1, interpolation=imshow_interpolation) 
        plt.show() 
        
#eest_facteur_rgb2()
#Resultat : le meilleur semble etre 4.5
       

### FIN DES TESTS ###
        
    


#Fonction permettant de tirer au sort la prochaine technologie inconnue a etudier
def tirage_techno():
    techno_inconnues = ["minio","elastic search","spark"]
    random = rand(0,len(techno_inconnues)-1)
    print("le grand gagnant est : ",techno_inconnues[random])
    
#tirage_techno()
    

    
#Affichage d'images avec les parametres choisis suite aux tests 
def affiche_images(donnees,label,debut,fin):
    label_found = False
    j = 0
    for i in range (debut,fin):
        while(not label_found):
            if label[i][j] == 1:
                label_found = True
            else:
                j += 1
        print("Label : ",labels[j])
        print(i)
        plt.imshow(donnees[i]*imshow_facteur_rgb,alpha=imshow_alpha, interpolation=imshow_interpolation)
        plt.show()
        plt.savefig("/tmp/img")
        label_found = False
        j = 0
        
#affiche_images(test_RGB,test_labels,0,test_RGB.shape[0])
affiche_images(test_RGB,test_labels,0,10)



#Affichage d'images en fonction d'une classe de label
def affiche_images_fct_label(label,nbr_images):
    i = 0
    compteur_images = 0
    while(compteur_images < nbr_images):
        if train_labels[i][label] == 1:
            print(i)
            plt.imshow(train_RGB[i]*imshow_facteur_rgb,alpha=imshow_alpha, interpolation=imshow_interpolation) 
            plt.show()
            compteur_images += 1
        i += 1
    print("Label : ",labels[label])

#affiche_images_fct_label(1,10)


call(["rm","-f","/tmp/test_RGB_0_10_25.npy"])
call(["rm","-f","/tmp/test_labels_0_10_25.npy"])




