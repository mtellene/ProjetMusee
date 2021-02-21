## README de la version v2

### Structure dossiers
* ```db``` contient la base de données, la matrice d'adjacence et le ficher oeuvre.json qui contient toutes les oeuvres (pour la création de la bd)
* ```static``` contient les fichiers ```*.png``` et ```*.css``` 
* ```templates``` contient les fichiers ```*.html```

### Structure code
#### init.py
* ```mon_graphe```: dictionnaire qui représente le graphe du musée, est de la forme {salle (str) : successeur(s) de salle (liste de str)}
* ```liste_des_salles```: liste qui contient toutes les salles du musée (str)
* ```couleurs_salles```: liste qui contient des couleurs au format hexadécimal (str)


* ```init_db()```: supprime l'ancienne base de données et en crée une vide
* ```recuperer_les_oeuvres()```: parse le fichier ```oevres.json``` afin de récupérer une liste avec toutes les oeuvres sous formes de tuple
* ```remplir_table_oeuvre()```: appelle la fonction précédente pour remplir la base de données
* ```creation_db()```: appelle ```init_db()``` et ```remplir_table_oeuvre()``` pour initialiser une base de données vide et la remplir
* ```creer_dict()```: remplit un dictionnaire représentant le graphe du musée en lisant la matrice d'adjacence ```todo pour les élèves```
* ```initialisation()```: fonction qui appelle ```creation_db()``` (cet appel peut être optionnel) et ```creer_dict()``` pour remplir le dictionnaire ```mon_graphe```

#### fonctions.py
* ```separation_par_types()```: créer 4 listes (une pour chaque type d'oeuvres), pour l'affichage dans ```itineraire.html```
* ```avoir_nom_salles_oeuvres(liste_oeuvres)```: prend en entrée une liste d'oeuvres et retourne une liste avec les salles associées à chaque oeuvres
* ```from_nom_salles_to_id(liste_oeuvres)```: prend en entrée une liste d'oeuvres et retourne une liste avec les id des salles correspondantes, cette fonction appelle ```avoir_nom_salles_oeuvres(liste_oeuvres)``` pour récupérer les salles de chaque oeuvres  


* ```lister_tous_les_chemins(graph, depart, path=[])```: prend en entrée le graphe (dictionnaire), un noeud de départ et une liste contenant un chemin, et retourne la liste de tous les chemins possibles
* ```garder_chemins_entree_sortie(liste_chemins)```: prend en entrée une liste contenant tous les chemins et retourne une liste ne contenant que les chemins qui vont de l'entrée jusqu'à la sortie
* ```garder_chemin_oeuvres(liste_chemins_ES, id_salle)```: prend en entrée une liste contenant tous les chemins entré-sortie du graphe et l'id d'une salle et retourne une liste ne contenant que les chemins contenant cet id
* ```garder_plus_court_chemin(liste_chemins)```: prend en entrée une liste contenant tous les chemins que l'utilisateur peut prendre afin de voir toutes les oeuvres choisies et retourne LE chemin le plus court 


* ```plus_court_chemin(liste_id_salles)```: fonction qui à partir d'une liste contenant les id des salles à visiter retourne le chemin le plus court pour voir toutes ces salles


* ```from_id_to_nom(liste_id_salles)```: prend en entrée une liste d'id de salles et retourne une liste contenant les noms des salles correspondants
* ```charger_resultat(liste_oeuvres)```: prend en argument une liste avec les oeuvres selectionnées par l'utilisateur et retourne la liste des salles à visiter
* ```coloration(chemin, liste_oeuvres)```: prend en argument une liste contenant le chemin à visiter et la liste des oeuvres sélectionnées et retourne deux listes : une liste contenant des tuples de la forme (salle,couleur de la salle) et une autre liste  contenant également des tuples de la forme (oeuvre, couleur de l'oeuvre). Une salle a la même couleur qui les oeuvres qui sont exposées dans celle-ci

#### app.py
Récupère les requêtes HTTP
* ```app.secret_key = ...```: est utilisé pour ```redirect(url_for('...'))```


* ```initialisation()```: fonction dans init.py, se lance dès le lancement du site 
* ```index()```: page d'acceuil du site 
* ```plan()```: page où il y a les plans du musée
* ```itineraire()```: page où l'utilisateur choisi les oeuvres qu'il veut voir
* ```resultat()```: page qui affiche le résultat de la selection de l'utilisateur

### Todo
* Régler le problème des images:
    * nombre des œuvres des arts visuels utilisées est limité à 20 œuvres par travail pédagogique :white_check_mark:
    * définition limitée à 400 x 400 pixels :x:
    * une résolution limitée à 72 DPI (point par pouce) :x:
* Faire le trajet pour la page résultat
### Utiles 

- site pour les droits d'auteur/exceptions pédagogiques:
https://www.reseau-canope.fr/savoirscdi/societe-de-linformation/cadre-reglementaire/le-coin-du-juriste/le-point-sur-lexception-pedagogique-au-29-septembre-2016.html
  
