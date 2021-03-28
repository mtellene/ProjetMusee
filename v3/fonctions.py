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
from Dessin import *
import shutil


def separation_par_types():
    """
    Input: /
    Output: 4 listes, une de chaque type d'oeuvre (écrits, peintures, sculptures ou artefacts)
    les éléments de chaque listes sont des tuples de la forme
    tuple = (type de l'oeuvre, artiste associé, titre de l'oeuvre, salle d'exposition, representation oeuvre)
    """
    liste_oeuvres = recuperer_les_oeuvres()
    type_ecrit = []
    type_peinture = []
    type_sculpture = []
    type_artefact = []
    for oeuvre in liste_oeuvres:
        if oeuvre[0] == "Ecrits":
            type_ecrit.append(oeuvre)
        elif oeuvre[0] == "Peinture":
            type_peinture.append(oeuvre)
        elif oeuvre[0] == "Sculpture":
            type_sculpture.append(oeuvre)
        elif oeuvre[0] == "Artefact":
            type_artefact.append(oeuvre)
    return type_ecrit, type_peinture, type_sculpture, type_artefact


def avoir_nom_salles_oeuvres(liste_oeuvres):
    """
    Input: une liste où chaque élément est une oeuvre
    Output: une liste contenant les noms des salles correspondantes aux oeuvres
    on itére sur les éléments de liste_oeuvres et on effectue une requête SQL pour récupérer le nom de sa salle d'exposition
    si la salle récupérée n'est pas dans la liste résultat alors on ajoute la salle dans la liste
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
    Input: une liste où chaque élément est une oeuvre
    Output: une liste contenant les id des salles correspondantes aux oeuvres
    on récupère le nom des salles de chaque oeuvre avec la fonction avoir_nom_salles_oeuvres() dans la liste_salles
    itére sur les éléments de liste_salles et on récupère l'indice de l'élément dans liste_des_salles
    si cet indice n'est pas dans la liste résultat alors on ajoute l'indice dans la liste
    """
    liste_id_salles = []
    liste_salles = avoir_nom_salles_oeuvres(liste_oeuvres)
    for salle in liste_salles:
        id = liste_des_salles.index(salle)
        if id not in liste_id_salles:
            liste_id_salles.append(id)
    return liste_id_salles


# todo pour eleve
def lister_tous_les_chemins(graph, depart, path=[]):
    """
    Input: un dictionnaire, un noeud de départ
    Output: une liste avec tous les chemins possibles partant du noeud de départ

    """
    path = path + [depart]  # on ajoute le noeud de depart dans la liste path
    if not depart in graph:  # si le noeud de depart n'est pas dans le graphe
        return [path]  # alors on return la liste
    paths = [path]  # sinon, on ajoute la liste path a la liste qui contiendra tous les chemins
    for noeud in graph[depart]:  # on parcourt les successeurs du noeud depart
        if noeud not in path:  # si le noeud n'est pas dans le chemin
            newpaths = lister_tous_les_chemins(graph, noeud,
                                               path)  # on lance la fonction récursivement en prenant comme depart noeud
            for newpath in newpaths:  # on parcourt la liste retournée par l'appel récursif
                paths.append(newpath)  # on ajoute les éléments de newpaths dans la liste paths
    return paths  # on retourne la liste paths (qui contient tous les chemins)


# todo pour eleve
def garder_chemins_entree_sortie(liste_chemins):
    """
    Input: une liste contenant tous les chemins possibles (partant du noeud de 0) dans le graphe
    Output: une liste contenant UNIQUEMENT les chemins entrée-sortie
    astuce: sortie = dernière cle dans le dictionnaire mon graphe
    """
    chemins = []
    for chem in liste_chemins:
        if chem[-1] == list(mon_graphe.keys())[-1]:  # list(mon_graph.keys())[-1] = recup la derniere key du dict
            chemins.append(chem)
    return chemins


# todo pour eleve
def garder_chemin_oeuvres(liste_chemins_ES, id_salle):
    """
    Input: une liste contenant tous les chemins entrée-sortie, un id d'une salle parmi celles à visiter
    Output: une liste contenant tous les chemins qui passent par la salle à visiter
    """
    chemins = []
    for i in range(len(liste_chemins_ES)):
        if id_salle in liste_chemins_ES[i]:
            chemins.append(liste_chemins_ES[i])
    return chemins


# todo pour eleve
def garder_plus_court_chemin(liste_chemins):
    """
    Input: une liste qui contient tous les chemins entrée-sortie qui passent par toutes les salles à visiter
    Output: le plus court chemin parmi tous les chemins dans la liste
    """
    min = liste_chemins[0]
    for i in range(len(liste_chemins)):
        if len(min) > len(liste_chemins[i]):
            min = liste_chemins[i]
    return min


# todo pour eleve
def plus_court_chemin(liste_id_salles):
    """
    Input: une liste avec les id des salles à voir
    Output: le plus court chemin pour passer dans toutes les salles
        -> lister tous les chemins
        -> lister les chemins entrée-sortie
        -> enlever les chemins qui ne passent pas dans les salles désirées
        -> trouver le plus des chemins possibles
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
    Input: une liste où chaque élément est l'id d'une salle
    Output: une liste où chaque élément est le nom d'une salle
    avec les id des salle de la liste en input on recupère les noms correspondants
    attention, vérifier que la salle n'est pas déjà dans la liste résultat
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
    Input: une liste où chaque élément est le nom d'une salle
    Output: une liste où chaque élément est l'id d'une salle
    avec les noms des salles de la liste en input on recupère les id correspondants
    attention, vérifier que la salle n'est pas déjà dans la liste résultat
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
    Input: une liste des oeuvres à voir
    Output: une liste où chaque élément est une salle où il faut passer
        -> récupérer les id des salles
        -> récupérer le plus court chemin
        -> convertir la liste d'id en liste de nom de salle
    """
    liste_id_salles = from_liste_oeuvres_to_liste_id_salles(liste_oeuvres)
    id_plus_court_chemin = plus_court_chemin(liste_id_salles)
    liste_salles_a_voir = from_id_to_nom(id_plus_court_chemin)
    return liste_salles_a_voir


# todo pour eleve
def coloration(chemin, liste_oeuvres):
    """
    Input: une liste contenant le plus court chemin, une liste contenant les oeuvres selectionnées
    Output: deux listes où chaque élément est un tuple
    une première liste où les tuples seront de la forme (salle, couleur associée)
    une seconde liste où les tuples seront de la forme (oeuvre, couleur de la salle)
    Première liste:
        -> itérer sur les éléments de la liste
        -> récupérer l'index de l'élément dans liste_des_salles
        -> crée le tuple et l'ajouter à la liste résultat
    Seconde liste:
        -> itérer sur les éléments de la liste
        -> récupérer la salle de l'élément
        -> récupérer la couleur de la salle
        -> créer le tuple et l'ajouter à la liste résultat
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
    if os.path.exists("static/temp"):
        shutil.rmtree("static/temp")
    os.popen("mkdir static/temp")


def dessiner(coloree_salles):
    remove_images()
    liste_salles = []
    for (salle, couleur) in coloree_salles:
        liste_salles.append(salle)
    liste_id_salles = from_nom_to_id(liste_salles)

    image0 = Dessin("static/etage0_res.png")
    image1 = Dessin("static/etage1_res.png")
    image_1 = Dessin("static/etage-1_res.png")

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
