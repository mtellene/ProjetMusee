# ! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    fonctions.py
    fonctions de traitement
"""
__author__ = "Maxime Tellene"
__copyright__ = "Univ Lyon1, 2020"
__license__ = "Public Domain"
__version__ = "3.0"

import sqlite3
from PIL.Image import *

from init import recuperer_les_oeuvres, mon_graphe, liste_des_salles, couleurs_salles
from Dessin_b import *
from Dessin_h import *
import shutil


def separation_par_types():
    """
    sépare les oeuvres en fonction de leur type
    :return: 4 listes (une de chaque type d'oeuvre)
    """
    liste_oeuvres = recuperer_les_oeuvres()
    type_ecrit = []
    type_peinture = []
    type_sculpture = []
    type_artefact = []
    for oeuvre in liste_oeuvres:
        if oeuvre['Type'] == "Ecrits":
            type_ecrit.append(oeuvre)
        elif oeuvre['Type'] == "Peinture":
            type_peinture.append(oeuvre)
        elif oeuvre['Type'] == "Sculpture":
            type_sculpture.append(oeuvre)
        elif oeuvre['Type'] == "Artefact":
            type_artefact.append(oeuvre)
    return type_ecrit, type_peinture, type_sculpture, type_artefact


def avoir_nom_salles_oeuvres(liste_oeuvres):
    """
    récupére le nom des salles d'exposition des oeuvres contenues dans liste_oeuvres (via une requête SQL)
    :param liste_oeuvres: liste de noms d'oeuvres
    :return: liste contenant les salles associées aux salles
    """
    liste_salles = []
    conn = sqlite3.connect('db/database.db')
    for oeuvre in liste_oeuvres:
        cur = conn.cursor()
        cur.execute("""SELECT salle FROM oeuvres WHERE nom=?""", (oeuvre,))
        records = cur.fetchall()
        for r in records:
            if r[0] not in liste_salles:
                liste_salles.append(r[0])
        cur.close()
    conn.close()
    return liste_salles


# todo pour eleve
def from_liste_oeuvres_to_liste_id_salles(liste_oeuvres):
    """
    récupère le nom des salles de chaque oeuvre avec la fonction avoir_nom_salles_oeuvres() dans liste_salles
    :param liste_oeuvres: liste de noms d'oeuvres
    :return: liste d'id de salles correspondantes aux oeuvres
    """
    liste_id_salles = []
    liste_salles = avoir_nom_salles_oeuvres(liste_oeuvres)
    for salle in liste_salles:
        id = liste_des_salles.index(salle)
        if id not in liste_id_salles:
            liste_id_salles.append(id)
    return liste_id_salles


# todo pour eleve
def lister_tous_les_chemins(graph, depart, chemin=[]):
    """
    retourne tous les chemins possibles
    :param graph: graphe modélisant le musée
    :param depart: salle de départ d'un chemin
    :param chemin: chemin actuel
    :return: une liste de chemins (liste de listes)
    """
    chemin = chemin + [depart]
    if not depart in graph:
        return [chemin]
    liste_chemins = [chemin]
    for noeud in graph[depart]:
        if noeud not in chemin:
            nouveau_chemins = lister_tous_les_chemins(graph, noeud, chemin)
            for n_chemin in nouveau_chemins:
                liste_chemins.append(n_chemin)
    return liste_chemins


# todo pour eleve
def garder_chemins_entree_sortie(liste_chemins):
    """
    garde les chemins entrée-sortie
    :param liste_chemins: liste de tous les chemins possibles dans le graphe
    :return: liste de tous les chemins entrée-sortie
    """
    chemins = []
    for chem in liste_chemins:
        if chem[-1] == list(mon_graphe.keys())[-1]:  # list(mon_graph.keys())[-1] = recup la derniere key du dict
            chemins.append(chem)
    return chemins


# todo pour eleve
def garder_chemin_oeuvres(liste_chemins_ES, id_salle):
    """
    garde les chemins qui passent par toutes les oeuvres
    :param liste_chemins_ES: liste de tous les chemins entrée-sortie
    :param id_salle: liste de tous les chemins entrée-sortie qui passent par toutes les oeuvres
    :return:
    """
    chemins = []
    for i in range(len(liste_chemins_ES)):
        if id_salle in liste_chemins_ES[i]:
            chemins.append(liste_chemins_ES[i])
    return chemins


# todo pour eleve
def garder_plus_court_chemin(liste_chemins):
    """
    garde le plus court chemin
    :param liste_chemins: liste de tous les chemins entrée-sortie qui passent par toutes les oeuvres
    :return: le plus court chemin
    """
    min = liste_chemins[0]
    for i in range(len(liste_chemins)):
        if len(min) > len(liste_chemins[i]):
            min = liste_chemins[i]
    return min


# todo pour eleve
def plus_court_chemin(liste_id_salles):
    """
    - liste tous les chemins possibles
    - liste les chemins entrée-sortie
    - enleve les chemins qui ne passent pas dans les salles désirées
    - garde le plus court chemin
    :param liste_id_salles: liste d'id des salles à voir
    :return: le plus court chemin pour passer dans toutes les salles
    """
    chemin = lister_tous_les_chemins(mon_graphe, list(mon_graphe.keys())[0])
    chemin = garder_chemins_entree_sortie(chemin)
    for salle in liste_id_salles:
        chemin = garder_chemin_oeuvres(chemin, str(salle))
    chemin = garder_plus_court_chemin(chemin)
    return chemin


# todo pour eleve
def from_id_to_nom(liste_id_salles):
    """
    recupère à partir d'une liste d'ids de salles, la liste des noms correspondants
    :param liste_id_salles: liste d'ids de salles
    :return: liste de noms de salles
    """
    liste_salles = []
    for id_salle in liste_id_salles:
        salle = liste_des_salles[int(id_salle)]
        if salle not in liste_salles:
            liste_salles.append(salle)
    return liste_salles


# todo pour eleve
def from_nom_to_id(liste_nom_salles):
    """
    recupère à partir d'une liste de noms de salles, la liste d'ids correspondants
    :param liste_nom_salles: liste de noms de salle
    :return: liste d'id de salle
    """
    liste_id_salles = []
    for nom_salle in liste_nom_salles:
        id = liste_des_salles.index(nom_salle)
        if id not in liste_id_salles:
            liste_id_salles.append(id)
    return liste_id_salles


# todo pour eleve
def charger_resultat(liste_oeuvres):
    """
    - récupére les ids des salles
    - récupére le plus court chemin
    - convertit la liste d'id en liste de nom de salle
    :param liste_oeuvres: liste des oeuvres à voir
    :return: liste de noms de salle où il faut passer
    """
    liste_id_salles = from_liste_oeuvres_to_liste_id_salles(liste_oeuvres)
    id_plus_court_chemin = plus_court_chemin(liste_id_salles)
    liste_salles_a_voir = from_id_to_nom(id_plus_court_chemin)
    return liste_salles_a_voir


def coloration(chemin, liste_oeuvres):
    """
    Première liste:
        - itére sur les éléments de la liste
        - récupére l'index de l'élément dans liste_des_salles
        - crée le tuple et l'ajouter à la liste résultat
    Seconde liste:
        - itére sur les éléments de la liste
        - récupére la salle de l'élément
        - récupére la couleur de la salle
        - crée le tuple et l'ajouter à la liste résultat
    :param chemin: liste avec le plus court chemin
    :param liste_oeuvres: liste avec les oeuvres selectionnées
    :return: deux listes où chaque élément est un tuple (1ere: (salle, couleur associée), 2e: (oeuvre, couleur de la salle))
    """
    colore_salle = []
    colore_oeuvre = []
    for c in chemin:
        i = liste_des_salles.index(c)
        colore_salle.append(tuple([c, couleurs_salles[i]]))

    for oeuvre in liste_oeuvres:
        nom_salle = avoir_nom_salles_oeuvres([oeuvre])[0]
        couleur = couleurs_salles[liste_des_salles.index(nom_salle)]
        colore_oeuvre.append(tuple([oeuvre, couleur]))
    return colore_salle, colore_oeuvre


def remove_images():
    """
    - supprime les répertoires contenant les plans dessinés
    - recrée les dossiers vierges pour mettre les nouveaux plans
    :return:
    """
    if os.path.exists("static/temp_n"):
        shutil.rmtree("static/temp_n")
    os.popen("mkdir static/temp_n")
    if os.path.exists("static/temp_f"):
        shutil.rmtree("static/temp_f")
    os.popen("mkdir static/temp_f")


def dessiner_n(coloree_salles):
    """
    dessine sur les plans du musée pour que l'utilisateur puisse voir le chemin à prendre
    :param coloree_salles: liste avec les salles par lesquels il faut passer
    :return: plans avec le chemin dessiné
    """
    liste_salles = []
    for (salle, couleur) in coloree_salles:
        liste_salles.append(salle)
    liste_id_salles = from_nom_to_id(liste_salles)

    image0 = DessinB("static/etage0_res.png")
    image1 = DessinB("static/etage1_res.png")
    image_1 = DessinB("static/etage-1_res.png")

    is1 = False
    is9 = False
    is10 = False
    is11 = False
    image0.draw_entree()
    if 1 in liste_id_salles:
        image0.relier_entree_1()
        image0.traverser_1()
        is1 = True

    # si on doit aller au sous sol
    if 2 not in liste_id_salles and 3 not in liste_id_salles and 4 not in liste_id_salles:
        if is1:
            image0.pas_passer_ss()
    else:
        image0.relier_1_2(image_1)
        image_1.traverser_2()
        if 3 in liste_id_salles:
            image_1.relier_et_traverser_3()
        else:
            image_1.raccourci_ss()
        image_1.relier_4()
        image_1.traverser_4()
        image_1.sortir_ss()
        image0.relier_ss_etage0()

    if 5 in liste_id_salles or 6 in liste_id_salles:
        image0.traverser_5()
        image0.relier_5_6()
        image0.traverser_6()
        if is1:
            image0.relier_1_5()
        else:
            image0.relier_entree_5()
    else:
        image0.raccourci_etage_0_1()

    # si on doit aller à l'étage
    if 7 in liste_id_salles or 8 in liste_id_salles or 9 in liste_id_salles or 10 in liste_id_salles or 11 in liste_id_salles or 12 in liste_id_salles:
        image0.relier_etage_0_7(image1)
        # si seulement 7
        if 8 not in liste_id_salles and 9 not in liste_id_salles and 10 not in liste_id_salles and 11 not in liste_id_salles and 12 not in liste_id_salles:
            image1.raccourci_etage_1_1()
            image1.sortie_etage_1()
        else:
            image1.traverser_7()
            image1.relier_7_8()
            image1.traverser_8()
            if 9 in liste_id_salles:
                image1.relier_8_9()
                image1.traverser_9()
                is9 = True
            if 10 in liste_id_salles:
                image1.traverser_10()
                if is9:
                    image1.relier_9_10()
                else:
                    image1.raccourci_etage_1_2()
                    image1.relier_raccourci_etage1_2_10()
                is10 = True
            if 11 in liste_id_salles:
                image1.traverser_11()
                if is10:
                    image1.relier_10_11()
                else:
                    image1.relier_8_11()
                is11 = True
            if 12 in liste_id_salles:
                if not is11 and not is10:
                    image1.raccourci_etage_1_3()
            image1.relier_11_12()
            image1.traverser_12()
        image1.sortie_etage_1()
        image0.sortie_depuis_etage_1()
    else:
        image0.raccourci_etage_0_2()
    image0.sortie()

    image0.save_draw()
    image1.save_draw()
    image_1.save_draw()

    return image0, image1, image_1


def dessiner_f(coloree_salles):
    """
    dessine sur les plans du musée pour que l'utilisateur puisse voir le chemin à prendre
    personne à mobilité réduite
    :param coloree_salles: liste avec les salles par lesquels il faut passer
    :return: plans avec le chemin dessiné
    """
    liste_salles = []
    for (salle, couleur) in coloree_salles:
        liste_salles.append(salle)
    liste_id_salles = from_nom_to_id(liste_salles)

    image0 = DessinH("static/etage0_res.png")
    image1 = DessinH("static/etage1_res.png")
    image_1 = DessinH("static/etage-1_res.png")

    is1 = False
    is9 = False
    is10 = False
    is11 = False
    image0.draw_entree()
    if 1 in liste_id_salles:
        image0.relier_entree_1()
        image0.traverser_1()
        is1 = True

    # si on doit aller au sous sol
    if 2 not in liste_id_salles and 3 not in liste_id_salles and 4 not in liste_id_salles:
        if is1:
            image0.pas_passer_ss()
    else:
        image0.relier_1_2(image_1)
        image_1.traverser_2()
        if 3 in liste_id_salles:
            image_1.relier_et_traverser_3()
        else:
            image_1.raccourci_ss()
        image_1.relier_4()
        image_1.traverser_4()
        image_1.sortir_ss()
        image0.relier_ss_etage0()

    if 5 in liste_id_salles or 6 in liste_id_salles:
        image0.traverser_5()
        image0.relier_5_6()
        image0.traverser_6()
        if is1:
            image0.relier_1_5()
        else:
            image0.relier_entree_5()
    else:
        image0.raccourci_etage_0_1()

    # si on doit aller à l'étage
    if 7 in liste_id_salles or 8 in liste_id_salles or 9 in liste_id_salles or 10 in liste_id_salles or 11 in liste_id_salles or 12 in liste_id_salles:
        image0.relier_etage_0_7(image1)
        # si seulement 7
        if 8 not in liste_id_salles and 9 not in liste_id_salles and 10 not in liste_id_salles and 11 not in liste_id_salles and 12 not in liste_id_salles:
            image1.raccourci_etage_1_1()
            image1.sortie_etage_1()
        else:
            image1.traverser_7()
            image1.relier_7_8()
            image1.traverser_8()
            if 9 in liste_id_salles:
                image1.relier_8_9()
                image1.traverser_9()
                is9 = True
            if 10 in liste_id_salles:
                image1.traverser_10()
                if is9:
                    image1.relier_9_10()
                else:
                    image1.raccourci_etage_1_2()
                    image1.relier_raccourci_etage1_2_10()
                is10 = True
            if 11 in liste_id_salles:
                image1.traverser_11()
                if is10:
                    image1.relier_10_11()
                else:
                    image1.relier_8_11()
                is11 = True
            if 12 in liste_id_salles:
                if not is11 and not is10:
                    image1.raccourci_etage_1_3()
            image1.relier_11_12()
            image1.traverser_12()
        image1.sortie_etage_1()
        image0.sortie_depuis_etage_1()
    else:
        image0.raccourci_etage_0_2()
    image0.sortie()

    image0.save_draw()
    image1.save_draw()
    image_1.save_draw()

    return image0, image1, image_1


def dessiner_plan(coloree_salles):
    """
    supprime les plans obsolètes puis recrée les nouveaux
    :param coloree_salles: liste des salles par lesquels il faut passer
    :return: plans dessinés
    """
    remove_images()
    img0_n, img1_n, img_1_n = dessiner_n(coloree_salles)
    img0_f, img1_f, img_1_f = dessiner_f(coloree_salles)
    return img0_n, img1_n, img_1_n, img0_f, img1_f, img_1_f
