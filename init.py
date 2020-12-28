import sqlite3, json

# supprime l'ancienne base de données et en re-créer une autre vide
def init_db():
    conn = sqlite3.connect('db/database.db')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS oeuvres")
    cur.execute("DROP TABLE IF EXISTS salles")

    cur.execute("CREATE TABLE IF NOT EXISTS oeuvres(id_oeuvre INT, nom TEXT, artiste TEXT, type TEXT, " +
        "img TEXT, salle TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS salles(id_salle INT, nom TEXT)")

    conn.commit()
    cur.close()
    conn.close()


# retourne une liste de listes où les sous-listes sont les oeuvres du musée
def recuperer_les_oeuvres():
    liste_oeuvres = []
    filename = 'db/oeuvres.json'
    with open(filename, 'r') as f:
        data = f.read()
        dico = json.loads(data)
        for i in dico.values():
            for j in i:
                type, artiste, titre, salle, img = j.values()
                tuple = (type, artiste, titre, salle, img)
                liste_oeuvres.append(tuple)
    f.close()
    return liste_oeuvres

# remplit la table "oeuvres" de la base de données
def remplir_table_oeuvre():
    liste_oeuvres = recuperer_les_oeuvres()

    conn = sqlite3.connect('db/database.db')
    cur = conn.cursor()
    for i in range (len(liste_oeuvres)):
        type, artiste, titre, salle, img = liste_oeuvres[i]
        values = (i, titre, artiste, type, salle, img)
        cur.execute("INSERT INTO oeuvres(id_oeuvre, nom, artiste, type, salle, img) VALUES (?, ?, ?, ?, ?, ?)", values)
        conn.commit()
    print("Table 'oeuvres' remplie !")
    cur.close()
    conn.close()

# retourne la liste des salles du musée
def recuperer_les_salles():
    liste_salles = []
    filename = 'db/salles.json'
    with open(filename, 'r') as f:
        data = f.read()
        dico = json.loads(data)
        for i in dico.values():
            for j in i:
                liste_salles.append(j.get('Nom').replace('_', ' '))
    f.close()
    return liste_salles

# remplit la table "salles" de la base de données
def remplir_table_salle():
    liste_salles = recuperer_les_salles()

    conn = sqlite3.connect('db/database.db')
    cur = conn.cursor()
    for i in range (len(liste_salles)):
        print(liste_salles[i])
        values = (i, liste_salles[i])
        cur.execute("INSERT INTO salles(id_salle, nom) VALUES (?, ?)", values)
        conn.commit()
    print("Table 'salles' remplie !")
    cur.close()
    conn.close()
