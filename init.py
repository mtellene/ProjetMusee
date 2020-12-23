import sqlite3, json

# supprime l'ancienne base de données et en re-créer une autre vide
def init_db():
    conn = sqlite3.connect('db/database.db')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS oeuvres")
    cur.execute("CREATE TABLE IF NOT EXISTS oeuvres(id_oeuvre INT, identifiant TEXT," +
        "nom TEXT, artiste TEXT, type TEXT, salle TEXT)")

    conn.commit()
    cur.close()
    conn.close()


def recuperer_les_oeuvres():
    liste_oeuvres = []
    filename = 'db/oeuvres.json'
    with open(filename, 'r') as f:
        data = f.read()
        dico = json.loads(data)
        for i in dico.values():
            for j in i:
                id, type, artiste, titre, salle = j.values()
                tuple = (id, type, artiste, titre, salle)
                liste_oeuvres.append(tuple)
    f.close()
    return liste_oeuvres

def remplir_table_oeuvre():
    liste_oeuvres = recuperer_les_oeuvres()

    conn = sqlite3.connect('db/database.db')
    cur = conn.cursor()
    for i in range (len(liste_oeuvres)):
        id, type, artiste, titre, salle = liste_oeuvres[i]
        values = (i, id, titre, artiste, type, salle)
        cur.execute("INSERT INTO oeuvres(id_oeuvre, identifiant, nom, artiste, "
            +"type, salle) VALUES (?, ?, ?, ?, ?, ?)", values)
        conn.commit()
    print("Table 'oeuvres' remplie !")
    cur.close()
    conn.close()
