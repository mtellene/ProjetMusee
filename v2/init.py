import sqlite3, json

mon_graph = {}
liste_des_salles = [
                "Entrée", "Antiquites Grecques", "Antiquites Asiatiques", "Antiquites Egyptiennes", "Objets d'art", "Art du Moyen-Age",
                "Objets du Moyen-Age", "Objets de la Renaissance", "Litterature de la Renaissance", "Peintures de la Renaissance", "Sculptures",
                "Litterature du 18-19e siecle", "Objets du 18-19e siecle", "Peintures du 18-19e siecle", "Litterature du 20e siecle",
                "Peintures du 20e siecle", "Sortie"
                ]

couleurs_salles = [
                "#000000", "#92a8d1", "#ff0000", "#8c562f", "#ac6895", "#a33222", "#dd431e", "#fffb00", "#00ff00", "#ff00ff", "#00ffff",
                "#606060", "#f8a090", "#004c00", "#bbc17e", "#c8b0d0", "#000000"
                ]

# supprime l'ancienne bdd et en re-créer une autre vide
def init_db():
    conn = sqlite3.connect('db/database.db')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS oeuvres")
    cur.execute("CREATE TABLE IF NOT EXISTS oeuvres(id_oeuvre INT, nom TEXT, artiste TEXT, type TEXT, " +
        "img TEXT, salle TEXT)")

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

# creer une representation du graphe sous forme de dictionnaire
def creer_dict():
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
        mon_graph[str(cptL)] = liste
        cptL = cptL + 1
        ligne = f.readline()

def initialisation():
    init_db()
    remplir_table_oeuvre()
    creer_dict()
