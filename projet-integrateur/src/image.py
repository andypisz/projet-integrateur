from numpy import load
from matplotlib import pyplot as plt



#parametres imshow, trouves suite a nos tests :
imshow_alpha = 0.85
imshow_interpolation = "spline36"
imshow_facteur_rgb = 4.5


#Les 5 classes de labels :
labels = ["urban area", "agricultural territory", "forests", "wetlands", "surfaces with water"]



# Affichage d'images avec les parametres choisis suite aux tests
def affiche_images_from_indices_list(donnees, labels, indices_list, debut, fin):
    for i in range(debut, fin):
        index = indices_list[i]
        print("Label : ", labels[index])
        print("Image number "+str(i)+" // index : "+str(index))
        plt.imshow(donnees[index] * imshow_facteur_rgb, alpha=imshow_alpha, interpolation=imshow_interpolation)
        plt.show()


def mainImage(pathRGB, pathLabel, indices_list):
    test_RGB = load(pathRGB)
    test_labels = load(pathLabel)
    affiche_images_from_indices_list(test_RGB, test_labels, indices_list, 0, 10)