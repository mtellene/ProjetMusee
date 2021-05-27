# ! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    init.py
    initialise la base de données et le dictionnaire
"""
__author__ = "Maxime Tellene"
__copyright__ = "Univ Lyon1, 2020"
__license__ = "Public Domain"
__version__ = "3.0"

import sqlite3

mon_graphe = {}
liste_des_salles = [
    "Entrée", "Antiquites Grecques", "Antiquites Asiatiques", "Antiquites Egyptiennes", "Objets d'art",
    "Art du Moyen-Age", "Objets du Moyen-Age", "Objets de la Renaissance", "Litterature de la Renaissance",
    "Peintures de la Renaissance", "Sculptures", "Litterature du 18-19e siecle", "Objets du 18-19e siecle",
    "Peintures du 18-19e siecle", "Litterature du 20e siecle", "Peintures du 20e siecle", "Sortie"
]

couleurs_salles = [
    "#000000", "#0000ff", "#ff0000", "#ff00ff", "#00ff00", "#ffff00", "#800000", "#808000", "#800080", "#008080",
    "#ffa500",
    "#808080", "#f08080", "#008000", "#d2691e", "#9acd32", "#000000"
]


def init_db():
    """
    Input: /
    Output: /
    fonction qui supprime l'ancienne base de donnée et en crée une vide
    l'appel de cette fonction peut être optionnel
    """
    conn = sqlite3.connect('db/database.db')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS oeuvres")
    cur.execute("CREATE TABLE IF NOT EXISTS oeuvres(id_oeuvre INT, nom TEXT, artiste TEXT, type TEXT, " +
                "img TEXT, salle TEXT)")

    conn.commit()
    cur.close()
    conn.close()


def recuperer_les_oeuvres():
    """
    Input: /
    Output: un dictionnaire avec toutes les oeuvres
    """
    filename = 'db/oeuvres.json'
    with open(filename) as f:
        dico = eval(f.read().replace('\n', ''))
    values = list(dico.values())[0]
    return values


def remplir_table_oeuvre():
    """
    Input: /
    Output: /
    fonction qui permet de remplir la table oeuvres de la base de donnée
    """
    liste_oeuvres = recuperer_les_oeuvres()

    conn = sqlite3.connect('db/database.db')
    cur = conn.cursor()
    for i in range(len(liste_oeuvres)):
        type = liste_oeuvres[i]['Type']
        artiste = liste_oeuvres[i]['Artiste']
        titre = liste_oeuvres[i]['Titre']
        salle = liste_oeuvres[i]['Salle']
        img = liste_oeuvres[i]['Representation']
        values = (i, titre, artiste, type, salle, img)
        cur.execute("INSERT INTO oeuvres(id_oeuvre, nom, artiste, type, salle, img) VALUES (?, ?, ?, ?, ?, ?)", values)
        conn.commit()
    print("Table 'oeuvres' remplie !")
    cur.close()
    conn.close()


def creation_db():
    """
    Input : /
    Output : /
    initialise une base de données vide et la remplit
    """
    init_db()
    remplir_table_oeuvre()


# todo pour eleve
def creer_dict():
    """
    Input: /
    Output: /
    fonction qui représente le graphe sous forme de dictionnaire de la forme [cle] : [valeurs]
    où cle est le sommet et valeurs correspond au(x) noeud(s) successeur(s)
    déroulement:
        -> lire et récupérer les lignes d'un fichier (matrice)
        -> définir un compteur de ligne et un compteur de colonne
        -> quand on a un '1' ajouter le compteur de colonne dans une liste (attention vous avez des chiffres)
        -> à la fin d'un ligne ajouter dans le dictionnaire [compteur ligne] : [liste]
    """
    cptL = 0
    f = open('db/matrice.txt', 'r')
    ligne = f.readline()
    while ligne != '':
        ligne = ligne.replace(' ', '')
        liste = []
        cptC = 0
        for c in ligne:
            if c == '1':
                liste.append(str(cptC))
            cptC = cptC + 1
        mon_graphe[str(cptL)] = liste
        cptL = cptL + 1
        ligne = f.readline()


def initialisation():
    creation_db()
    creer_dict()
