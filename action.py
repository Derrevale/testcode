# Importation de la classe tableau
import copy
import random

from bateau import Bateau
from tableau import *

# Importation de la classe joueur
from joueur import Joueur


def nom_de_joueur(x):
    # Fonction d'attribution des noms
    nom_joueur = input("\nJoueur " + str(x) + ", veuillez introduire votre nom : ")
    return nom_joueur


def selection_type_partie_console():
    petite_bat = "P"
    grande_bat = "G"
    lancement = False
    style_partie = input(
        "Choisisez le style de partie que vous voulez jouez."
        "\nGrande Bataille (10*10 , 5 Bateaux)"
        "\nPetite Bataille (06*06 , 3 Bateaux)"
        "\nG/P\n")

    # verification que la valeur entrée est correcte
    while not lancement:

        if style_partie.upper() == petite_bat:
            lancement = True
            nombre_ligne_colonne = 5

        elif style_partie.upper() == grande_bat:
            lancement = True
            nombre_ligne_colonne = 10
        else:
            print("erreur")
            style_partie = input(
                "Le choix entrez est incorecte veuillez réintroduire."
                "\nGrande Bataille (10*10 , 5 Bateaux)"
                "\nPetite Bataille (06*06 , 3 Bateaux)"
                "\nG/P\n")
    return nombre_ligne_colonne


def selection_nombre_bateau(x):
    print(x)
    nombre_bateau = 0
    if x == 5:
        nombre_bateau = 3
    elif x == 10:
        nombre_bateau = 5

    return nombre_bateau


def afficher_tableau(tableau):
    for elements in tableau:
        print(elements)


def creation_tableau_joueur(dimension, nom_joueur):
    plateau_joueur = CreerTableau(dimension)
    plateau_joueur.creation_tableau()
    return Joueur(nom_joueur, plateau_joueur)





def effectuer_tir(self, tab, rangee, col, adversaire):
    coordonnees_plateau = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6
    }
    col = coordonnees_plateau[col]
    rangee = rangee + 1
    if tab[rangee][col] == "o":
        tab[rangee][col] = "@"
        print("Touché")
        for elements in adversaire.porte_avion.coordonnees_bateau:
            if elements[0] == col + 1 and elements[1] == rangee:
                print("dans if")
                adversaire.porte_avion.coordonnees_bateau[0][2] = "X"
                adversaire.porte_avion.etat_bateau = "Touché"
                print(adversaire.porte_avion.coordonnees_bateau)
    elif tab[rangee][col] == "@":
        tab[rangee][col] = "@"
    else:
        print("Raté!")
        tab[rangee][col] = "X"


def choix_action(self, x):
    roulette = ["coup vertical"]
    resultat_roulette = ""
    if x.portefeuille_joueur >= 150:
        choix_roulette = input(
            "{}, Vous avez actuellement {} euros dans votre portefeuille, voulez-vous faire tourner la roulette pour"
            " 150 euros? (o ou n) \n\n".format(x.nom_joueur, x.portefeuille_joueur))
        if choix_roulette == "o":
            # x.portefeuille_joueur = x.portefeuille_joueur - 150
            resultat_roulette = random.choice(roulette)
            if resultat_roulette == "rien":
                print("Dommage, vous n'avez rien gagné !")
            else:
                print("Félicitations vous avez gagné le sort suivant : {} ".format(resultat_roulette))
    else:
        print("Vous n'avez pas assez d'argent pour faire tourner la roulette\n\n")
    return resultat_roulette


def plateau_invisible_adversaire(plateau_invisible, plateau_a_copier):
    print(plateau_a_copier)
    plateau_invisible = copy.deepcopy(plateau_a_copier)
    print(plateau_a_copier)
    for elements in range(len(plateau_invisible.plateau_joueur)):
        for ele in range(len(plateau_invisible.plateau_joueur[elements])):
            if plateau_invisible.plateau_joueur[elements][ele] == "o":
                plateau_invisible.plateau_joueur[elements][ele] = "~"
    for elements in plateau_invisible:
        print(elements)


def tour_de_jeu(x, z, adversaire, plateau_invisible):
    # x = joueur actuel
    # z = listeplateau joueur adverse

    while True:
        try:
            print(adversaire)
            print("non")
            plateau_invisible_adversaire(plateau_invisible, adversaire)
            choix_col_joueur = input(
                "Joueur : {}, Veuillez introduire la colonne : ".format(x.nom))
            choix_rangee_joueur = int(
                input("Joueur : {}, Veuillez introduire la ligne : ".format(x.nom)))
            effectuer_tir(z, choix_rangee_joueur, choix_col_joueur.upper(), adversaire)
        except KeyError:
            print("Erreur, veuillez introduire des coordonnées valides\n")
            continue
        except ValueError:
            print("Erreur, veuillez introduire des coordonnées valides\n")
            continue
        else:
            plateau_invisible_adversaire(plateau_invisible, z)
            break

    print("==========================================\n"
          "==========================================\n"
          "==========================================\n")


def positionner_bateau(joueur, number_of_ships):
    print(number_of_ships)
    for elements in range(1, number_of_ships + 1):
        afficher_tableau(joueur.plateau_joueur.tableau)
        if elements == 1:
            porte_avion = Bateau("porte-avion", 3)
            joueur.porte_avion = porte_avion
            joueur.nom_des_bateaux.append("porte-avion")
            bateau = porte_avion

        elif elements == 2:
            torpilleur = Bateau("torpilleur", 2)
            joueur.torpilleur = torpilleur
            joueur.nom_des_bateaux.append("torpilleur")
            bateau = torpilleur
        elif elements == 3:
            croiseur = Bateau("croiseur", 2)
            joueur.croiseur = croiseur
            joueur.nom_des_bateaux.append("croiseur")
            bateau = croiseur
        print("Joueur {} le bateau que vous placez est le : {} avec une taille de : {}".format(joueur.nom, bateau.nom_bateau,
                                                                                               bateau.taille_bateau))
        while True:
            try:
                coord_col = input(
                    "Joueur {}, veuillez choisir une colonne comme point de départ pour placer le {} : ".format(joueur.nom,
                                                                                                                bateau.nom_bateau)).upper()
                coord_rangee = int(input(
                    "Joueur {}, veuillez choisir une ligne comme point de départ pour placer le {} : ".format(joueur.nom,
                                                                                                              bateau.nom_bateau)))
                bateau.position_bateau(coord_col, coord_rangee, bateau, joueur.plateau_joueur.tableau)
            except KeyError:
                print("Erreur, veuillez introduire des coordonnées valides\n")
                continue
            except ValueError:
                print("Erreur, veuillez introduire des coordonnées valides\n")
                continue
            else:
                break
    print(joueur.nom_joueur)
    print(joueur.porte_avion.coordonnees_bateau)
    fin_de_tour = False
    while fin_de_tour == False:
        print("Votre tour est fini , le joueur suivant peut s'installer devant l'ordinateur...\n\n\n")
        valid_fin_de_tour = input("joueur suivant êtes vous prêt o/n\n\n").upper()
        if valid_fin_de_tour == "O" or valid_fin_de_tour == "OUI":
            fin_de_tour = True


def verif_bateau(nom_du_bateau, x):
    counter = []
    for elements in range(nom_du_bateau.taille_bateau):
        if nom_du_bateau.etat_bateau == "inactif":
            print("ce bateau a déjà été détruit")
            break
        if nom_du_bateau.coordonnees_bateau[elements][2] == "@":
            print("{} est endommagé".format(nom_du_bateau.nom_bateau))
            counter.append("@")
            nom_du_bateau.etat_bateau = "Touché"
            if len(counter) == nom_du_bateau.taille_bateau:
                nom_du_bateau.etat_bateau = "inactif"
                if nom_du_bateau.etat_bateau == "inactif":
                    x.portefeuille_joueur = x.portefeuille_joueur + 150
                    print(x.portefeuille_joueur)
                else:
                    print("pas encore")
    print("L'état du bateau {} est le suivant : {} ".format(nom_du_bateau.nom_bateau, nom_du_bateau.etat_bateau))


def rafraichir_position(z, nom_du_bateau):
    for elements in range(nom_du_bateau.taille_bateau):
        col = nom_du_bateau.coordonnees_bateau[elements][1]
        rangee = nom_du_bateau.coordonnees_bateau[elements][0]
        if z[rangee][col] == "@":
            nom_du_bateau.coordonnees_bateau[elements][2] = "@"
    print(nom_du_bateau.coordonnees_bateau)


def verif_win(y, number_of_ship):
    # y = joueur_1 ou 2
    if number_of_ship == 3:
        if y.porte_avion.etat_bateau and y.torpilleur.etat_bateau and y.croiseur.etat_bateau == "inactif":
            return True
    elif number_of_ship == 2:
        if y.porte_avion.etat_bateau and y.torpilleur.etat_bateau == "inactif":
            return True
    elif number_of_ship == 1:
        if y.porte_avion.etat_bateau == "inactif":
            return True


def debut_partie(joueur1,joueur2,
                 tableau_invisible_joueur1, tableau_invisible_joueur2,
                 number_of_ships):
    print(number_of_ships)
    victoire = False
    print("test2")
    positionner_bateau(joueur1, number_of_ships)
    positionner_bateau(joueur2, number_of_ships)
    print("test3")
    while victoire == False:

        if number_of_ships == 3:
            verif_3_BATEAUX(joueur1,
                            joueur2,
                            tableau_invisible_joueur1, tableau_invisible_joueur2,
                            )

        elif number_of_ships == 2:
            verif_2_BATEAUX(joueur1,
                            joueur2,
                            tableau_invisible_joueur1, tableau_invisible_joueur2,
                            )

        elif number_of_ships == 1:
            verif_1_BATEAUX(joueur1,
                            joueur2,
                            tableau_invisible_joueur1, tableau_invisible_joueur2,
                            )

        if verif_win(joueur2, number_of_ships) == True:
            victoire = True
            print("le joueur 1 a gagné")

        if verif_win(joueur1, number_of_ships) == True:
            victoire = True
            print("le joueur 2 a gagné")


def verif_3_BATEAUX(joueur1,
                    joueur2,
                    tableau_invisible_joueur1, tableau_invisible_joueur2,
                    ):
    print("plateau du joueur 2 : \n")
    tour_de_jeu(joueur1, joueur2, joueur2.plateau_joueur, tableau_invisible_joueur2)
    rafraichir_position(joueur2,joueur2.porte_avion)
    verif_bateau(joueur2.porte_avion, joueur1)
    rafraichir_position(joueur2, joueur2.torpilleur)
    verif_bateau(joueur2.torpilleur, joueur1)
    rafraichir_position(joueur2, joueur2.croiseur)
    verif_bateau(joueur2.croiseur, joueur1)

    print("plateau du joueur 1 : \n")
    tour_de_jeu(joueur2, joueur1, joueur1.plateau_joueur, tableau_invisible_joueur1)
    rafraichir_position(joueur1, joueur1.porte_avion)
    verif_bateau(joueur1.porte_avion, joueur2)
    rafraichir_position(joueur1, joueur1.torpilleur)
    verif_bateau(joueur1.torpilleur, joueur2)
    rafraichir_position(joueur1, joueur1.croiseur)
    verif_bateau(joueur1.croiseur, joueur2)


def verif_2_BATEAUX(joueur1,joueur2,
                    tableau_invisible_joueur1, tableau_invisible_joueur2,
                    ):
    print("plateau du joueur 2 : \n")
    tour_de_jeu(joueur1, joueur2, joueur2.plateau_joueur, tableau_invisible_joueur2)
    rafraichir_position(joueur2, joueur2.porte_avion)
    verif_bateau(joueur2.porte_avion, joueur1)
    rafraichir_position(joueur2, joueur2.torpilleur)
    verif_bateau(joueur2.torpilleur, joueur1)

    print("plateau du joueur 1 : \n")
    tour_de_jeu(joueur2, joueur1, joueur1.plateau_joueur, tableau_invisible_joueur1)
    rafraichir_position(joueur1, joueur1.porte_avion)
    verif_bateau(joueur1.porte_avion, joueur2)
    rafraichir_position(joueur1,joueur1.torpilleur)
    verif_bateau(joueur1.torpilleur, joueur2)


def verif_1_BATEAUX(joueur1,joueur2,
                    tableau_invisible_joueur1, tableau_invisible_joueur2,
                    ):
    print("plateau du joueur 2 : \n")
    tour_de_jeu(joueur1, joueur2, joueur2.plateau_joueur, tableau_invisible_joueur2)
    rafraichir_position(joueur2, joueur2.porte_avion)
    verif_bateau(joueur2.porte_avion, joueur1)

    print("plateau du joueur 1 : \n")
    tour_de_jeu(joueur2, joueur1, joueur1.plateau_joueur, tableau_invisible_joueur1)
    rafraichir_position(joueur1, joueur1.porte_avion)
    verif_bateau(joueur1.porte_avion, joueur2)
