import sqlite3

from init import recuperer_les_oeuvres, mon_graph, liste_des_salles, couleurs_salles

# separe la liste d'oeuvres par type (ecrits, peintures, sculptures, artefacts)
# cette fonction sert pour l'affichage dans itineraire
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

# retourne une liste avec les identifants des salles où sont les oeuvres de liste_oeuvres
def from_nom_salles_to_id(liste_oeuvres):
    liste_id_salles = []
    conn = sqlite3.connect('db/database.db')
    for oeuvre in liste_oeuvres:
        cur = conn.cursor()
        cur.execute("""SELECT salle FROM oeuvres WHERE nom=?""", (oeuvre,))
        records = cur.fetchall()
        if records[0][0] in liste_des_salles:
            id = liste_des_salles.index(records[0][0])
            if id not in liste_id_salles:
                liste_id_salles.append(id)
        cur.close()
    conn.close()
    return liste_id_salles

# retourne une liste avec le nom des salles des oeuvres de la liste passées en argument
def avoir_nom_salles_oeuvres(liste_oeuvres):
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

# retourne une liste qui contient tous les chemins possibles du graph
def lister_tous_les_chemins(graph, depart, path=[]):
    path = path + [depart]  # on ajoute le noeud de depart dans la liste path
    if not depart in graph: # si le noeud de depart n'est pas dans le graphe
        return [path]   # alors on return la liste
    paths = [path]  # sinon, on ajoute la liste path a la liste qui contiendra tous les chemins
    for noeud in graph[depart]: # on parcourt les successeurs du noeud depart
        if noeud not in path:   # si le noeud n'est pas dans le chemin
            newpaths = lister_tous_les_chemins(graph, noeud, path)  # on lance la fonction récursivement en prenant comme depart noeud
            for newpath in newpaths:    # on parcourt la liste retournée par l'appel récursif
                paths.append(newpath)   # on ajoute les éléments de newpaths dans la liste paths
    return paths    # on retourne la liste paths (qui contient tous les chemins)

# retourne une liste qui ne contient seulement les chemins qui vont de l'entree jusqu'a la sortie du graphe
def garder_chemins_entree_sortie(liste_chemins):
    chemins = []
    for chem in liste_chemins:
        if chem[-1] == list(mon_graph.keys())[-1]:  # list(mon_graph.keys())[-1] = recup de la derniere key du dict mon_graph
            chemins.append(chem)
    return chemins

# retourne une liste qui ne contient seulement les chemins qui passent par toutes les salles demandees
def garder_chemin_oeuvres(liste_chemins, salle):
    chemin = []
    for i in range(len(liste_chemins)):
        if salle in liste_chemins[i]:
            chemin.append(liste_chemins[i])
    return chemin

# retourne le chemin le plus court parmis les chemins de la liste retournee par la fonction precedente
def garder_plus_court_chemin(liste_chemins):
    min = liste_chemins[0]
    for i in range(len(liste_chemins)):
        if len(min) > len(liste_chemins[i]):
            min = liste_chemins[i]
    return min

# retourne le chemin le plus court (en terme de nombre de salles traversees) pour voir toutes les oeuvres voulues
def plus_court_chemin(liste_id_salles):
    chemin = lister_tous_les_chemins(mon_graph, list(mon_graph.keys())[0])
    chemin = garder_chemins_entree_sortie(chemin)
    for salle in liste_id_salles:
        chemin = garder_chemin_oeuvres(chemin, str(salle))
    chemin = garder_plus_court_chemin(chemin)
    return chemin

# change la liste d'id des salles en liste de noms des salles correspondantes
def from_id_to_nom(liste_id_salles):
    liste_salles = []
    for id_salle in liste_id_salles:
        salle = liste_des_salles[int(id_salle)]
        if salle not in liste_salles:
            liste_salles.append(salle)
    return liste_salles

# fonction qui prend en argument une liste d oeuvre et retourne une liste de salle
# cette liste de salle est le plus court chemin (en terme de nombre de salle traversees) pour voir toutes les oeuvres demandees
def charger_resultat(liste_oeuvres):
    liste_id_salles = from_nom_salles_to_id(liste_oeuvres)
    id_plus_court_chemin = plus_court_chemin(liste_id_salles)
    resultat = from_id_to_nom(id_plus_court_chemin)
    return resultat

# fonction qui sert pour la coloration du résultat
def coloration(chemin, liste_oeuvres):
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
