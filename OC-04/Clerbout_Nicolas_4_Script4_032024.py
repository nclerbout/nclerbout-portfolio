# importation du module os pour utiliser methodes permettant de lister et manipuler des fichiers

import os

# Ce script permet d'identifier les fichiers dont le nom commence par "xmc6_" et ceux qui contiennent l'IP
# 8.13.193.9 presents dans le dossier sites_clients ET de les renommer en ajoutant l'extension ".txt"
# Une condition est ajoutee pour eviter que de multiples lancements du script ne provoquent une accumulation
# d'extensions ".txt.txt.txt...."


# Le programme demarre ici
print("Recherche de fichiers malveillants...")


# On commence par recuperer le chemin complet du dossier sites_clients pour pouvoir iterer sur les fichiers presents
# dans celui-ci

# racine est une variable qui contient le nom du repertoire: e.g., ./sites_clients/site_photographes_paris/
# fichiers est une liste de fichiers presents dans le repertoire: ["fichier1.php", "fichier2.php"...]

chemin_complet = os.path.dirname(os.path.abspath(__file__))

for racine, _, fichiers in os.walk(chemin_complet + "/sites_clients"):
    for fichier in fichiers:
        # variable malveillant egale a False par defaut
        malveillant = False

        # Utilisation de la methode .startswith() avec le debut de nom de fichier identifie.
        # Affichage des fichiers trouves dont le nom commence avec ces caracteres
        # Mise a jour de la variable malveillant pour les fichiers identifies

        if fichier.startswith("xmc6_"):
            print(fichier)
            malveillant = True

        # On recupere le chemin complet vers les fichiers afin de pouvoir les ouvrir avec open()
        # puis on verifie si la chaine "8.13.193.9" apparait dans le fichier quand on le lit (read())
        # si c'est le cas on l'affiche
        # Mise a jour de la variable malveillant pour les fichiers identifies

        nom_complet = racine + "/" + fichier
        fichier_ouvert = open(nom_complet, 'r')
        contenu = "8.13.193.9"
        if contenu in fichier_ouvert.read():
            print(fichier)
            malveillant = True

        # referme les fichiers ouverts - necessaire pour les renommer si besoin
        fichier_ouvert.close()

        # Si le fichier est identifie comme malveillant, et qu'il n'a pas deja l'extension .txt, on definit un nouveau
        # nom en ajoutant l'extension ".txt"
        # on renomme le fichier avec son nouveau nom
        # on affiche le nouveau nom avec son chemin complet

        if malveillant and not fichier.endswith(".txt"):
            print("Renommer le fichier %s" % fichier)
            nouveau_nom = nom_complet + ".txt"
            os.rename(nom_complet, nouveau_nom)
            print(nouveau_nom)

            # Affichage d'un separateur pour lisibilite entre les differents fichiers traites
            print("************************************")
