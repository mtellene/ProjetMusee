import sqlite3

from init import recuperer_les_oeuvres

def separation_par_types():
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

def avoir_salles(liste_oeuvres):
    liste_salles = []
    conn = sqlite3.connect('db/database.db')
    for oeuvre in liste_oeuvres:
        cur = conn.cursor()
        cur.execute("""SELECT salle FROM oeuvres WHERE nom=?""", (oeuvre,))
        records = cur.fetchall()
        for r in records:
            salle = r[0].replace('_', ' ')
            if salle not in liste_salles:
                liste_salles.append(salle)
        cur.close()
    conn.close()
    return liste_salles
