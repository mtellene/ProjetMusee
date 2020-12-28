import sqlite3

from init import recuperer_les_oeuvres

mon_graph = {
    '0': ['1', '3'],
    '1': ['2'],
    '2': ['3', '5', '11'],
    '3': ['4'],
    '4': ['5', '11'],
    '5': ['6', '11'],
    '6': ['7', '8', '9'],
    '7': ['8', '10'],
    '8': ['9'],
    '9': ['10'],
    '10': ['11'],
    '11': ['12'],
    '12': ['13'],
    '13': ['14'],
    '14': []
}

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

def avoir_id_salles(liste_salles):
    liste_id_salles = []
    conn = sqlite3.connect('db/database.db')
    for salle in liste_salles:
        cur = conn.cursor()
        cur.execute("""SELECT id_salle FROM salles WHERE nom=?""", (salle,))
        records = cur.fetchall()
        for r in records:
            if r[0] not in liste_id_salles:
                liste_id_salles.append(r[0])
        cur.close()
    conn.close()
    return liste_id_salles

def tous_les_chemins(graph, depart, path=[]):
    path = path + [depart]
    if not depart in graph:
        return [path]
    paths = [path]
    for noeud in graph[depart]:
        if noeud not in path:
            newpaths = tous_les_chemins(graph, noeud, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def garder_chemins_e_s(liste_chemins):
    chemins = []
    for chem in liste_chemins:
        if chem[-1] == '14':
            chemins.append(chem)
    return chemins

def garder_chemin_oeuvres(liste_chemins, salle):
    chemin = []
    for i in range(len(liste_chemins)):
        if salle in liste_chemins[i]:
            chemin.append(liste_chemins[i])
    return chemin

def garder_plus_court_chemin(liste_chemins):
    min = liste_chemins[0]
    for i in range(len(liste_chemins)):
        if len(min) > len(liste_chemins[i]):
            min = liste_chemins[i]
    return min

def plus_court_chemin(liste_id_salles):
    chemin = tous_les_chemins(mon_graph, '0')
    chemin = garder_chemins_e_s(chemin)
    for salle in liste_id_salles:
        chemin = garder_chemin_oeuvres(chemin, str(salle))
    chemin = garder_plus_court_chemin(chemin)
    return chemin
