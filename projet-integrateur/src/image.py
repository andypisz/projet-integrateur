from numpy import load
from matplotlib import pyplot as plt



#parametres imshow, trouves suite a nos tests :
imshow_alpha = 0.85
imshow_interpolation = "spline36"
imshow_facteur_rgb = 4.5


#Les 5 classes de labels :
labels = ["urban area", "agricultural territory", "forests", "wetlands", "surfaces with water"]



# Affichage d'images avec les parametres choisis suite aux tests
def affiche_images_from_indices_list(donnees, label, indices_list, debut, fin):
    label_found = False
    j = 0
    for i in range(debut, fin):
        index = int(indices_list[i])
        while (not label_found):
            if label[index][j] == 1:
                label_found = True
            else:
                j += 1
        print("Label : ", labels[j])
        print("Image number "+str(i)+" // index : "+str(index))
        plt.imshow(donnees[index] * imshow_facteur_rgb, alpha=imshow_alpha, interpolation=imshow_interpolation)
        plt.show()
        label_found=False
        j = 0


def mainImage(pathRGB, pathLabel, indices_list):
    test_labels = load(pathLabel)
    print("loaded labels")
    test_RGB = load(pathRGB)
    print("loaded images")
    affiche_images_from_indices_list(test_RGB, test_labels, indices_list, 0, 10)