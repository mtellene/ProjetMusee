## README de la version v3

### Avant-propos

Ce logiciel est un logiciel a des fins pédagogiques. Une partie sera donc à faire par des élèves. Par conséquent les fonctions avec <em> TODO </em> seront à faire par les élèves. 

### Le projet 
Les oeuvres sont stockés dans une base de données (```database.db```). Cette base de données est rempli à partir d'un fichier json.
* ```db``` contient la base de données, la matrice d'adjacence et le ficher oeuvres.json qui contient toutes les oeuvres.
* ```static``` contient les fichiers ```*.png```, ```*.js``` et ```*.css```. 
  Il contient : 
    - deux dossiers ```temp_n/``` et ```temp_f/``` qui contiennent les plans avec le chemin (voir section ```fonctions.py```).
    - deux dossiers ```representations_temp/``` et ```representations/``` qui contiennent les réprésentations des oeuvres (voir section ```init.py```).
* ```templates``` contient les fichiers ```*.html``` qui vont permettre à l'utilisateur d'utiliser le site.

### Structure code
#### init.py
* ```mon_graphe```: dictionnaire qui représente le graphe du musée, est de la forme {salle (str) : successeur(s) de salle (liste de str)}
* ```liste_des_salles```: liste qui contient toutes les salles du musée (str)
* ```couleurs_salles```: liste qui contient des couleurs au format hexadécimal (str) 


* ```init_db()```: supprime l'ancienne base de données et en crée une vide
* ```recuperer_les_oeuvres()```: parse le fichier ```oevres.json``` afin de récupérer un dictionnaire avec toutes les oeuvres
* ```remplir_table_oeuvre()```: appelle la fonction précédente, récupère le résultat et remplit la base de données
* ```creation_db()```: appelle ```init_db()``` et ```remplir_table_oeuvre()``` pour initialiser une base de données vide et la remplir
* ```creer_dict()```: remplit un dictionnaire représentant le graphe du musée en lisant la matrice d'adjacence (<em>TODO</em>)
* ```redimensionnement(filename, output_file)``` : redimensionne l'image <em>filename</em> et sauvegarde l'image en tant que <em>output_file</em>.
* ```recuperer_representations()``` : télécharge toutes les représentations des oeuvres pour les redimensionner.  
* ```initialisation()```: fonction qui appelle ```creation_db()``` (cet appel peut être optionnel) et appelle ```creer_dict()``` pour remplir le dictionnaire ```mon_graphe``` enfin appelle ```recuperer_representations()``` pour télécharger les représentations des oeuvres puis les redimensionne pour les afficher.

#### fonctions.py
* ```separation_par_types()```: créer 4 listes (une pour chaque type d'oeuvres), pour l'affichage dans ```itineraire.html```
* ```avoir_nom_salles_oeuvres(liste_oeuvres)```: prend en entrée une liste d'oeuvres et retourne une liste avec les salles associées à chaque oeuvres
* ```from_nom_salles_to_id(liste_oeuvres)```: prend en entrée une liste d'oeuvres et retourne une liste avec les id des salles correspondantes, cette fonction appelle ```avoir_nom_salles_oeuvres(liste_oeuvres)``` pour récupérer les salles de chaque oeuvres (<em>TODO</em>)  


* ```lister_tous_les_chemins(graph, depart, path=[])```: prend en entrée le graphe (dictionnaire), un noeud de départ et une liste contenant un chemin, et retourne la liste de tous les chemins possibles (<em>TODO</em>)
* ```garder_chemins_entree_sortie(liste_chemins)```: prend en entrée la liste contenant tous les chemins et retourne la liste ne contenant que les chemins qui vont de l'entrée jusqu'à la sortie (<em>TODO</em>)
* ```garder_chemin_oeuvres(liste_chemins_ES, id_salle)```: prend en entrée la liste contenant tous les chemins entré-sortie du graphe et l'id d'une salle et retourne une liste ne contenant que les chemins contenant cet id (<em>TODO</em>)
* ```garder_plus_court_chemin(liste_chemins)```: prend en entrée une liste contenant tous les chemins que l'utilisateur peut prendre afin de voir toutes les oeuvres choisies et retourne LE chemin le plus court en terme de nombre de salle traversée (<em>TODO</em>)
* ```plus_court_chemin(liste_id_salles)```: fonction qui à partir d'une liste contenant les id des salles à visiter retourne le chemin le plus court pour voir toutes ces salles (<em>TODO</em>)


* ```from_id_to_nom(liste_id_salles)```: prend en entrée une liste d'ids de salles et retourne une liste contenant les noms des salles correspondants (<em>TODO</em>)
* ```from_nom_to_id(liste_nom_salles)```: prend en entrée une liste de noms de salles et retourne une liste contenant les ids des salles correspondants (<em>TODO</em>)
* ```charger_resultat(liste_oeuvres)```: prend en argument une liste avec les oeuvres selectionnées par l'utilisateur et retourne la liste des salles à visiter (<em>TODO</em>)
* ```coloration(chemin, liste_oeuvres)```: prend en argument une liste contenant le chemin à prendre et la liste des oeuvres sélectionnées et retourne deux listes : une liste contenant des tuples de la forme (salle, couleur de la salle) et une autre liste  contenant également des tuples de la forme (oeuvre, couleur de l'oeuvre). Une salle a la même couleur qui les oeuvres qui sont exposées dans celle-ci (<em>TODO</em>)
* ```dessiner(coloree_salles)```: supprime les anciens plans dessinés et en crée d'autres. Les plans sont les plans vierges et la fonction dessine le chemin à prendre


#### app.py
Récupère les requêtes HTTP
* ```app.secret_key = ...```: est utilisé pour ```redirect(url_for('...'))```


* ```initialisation()```: fonction dans init.py, se lance dès le lancement du site 
* ```index()```: page d'acceuil du site 
* ```plan()```: page où il y a les plans du musée
* ```itineraire()```: page où l'utilisateur choisi les oeuvres qu'il veut voir
* ```resultat()```: page qui affiche le résultat de la selection de l'utilisateur

#### Dessin_b.py et Dessin_h.py

Classes DessinB et DessinH, le constructeur crée une image sur lequel on peut dessiner. On ajoute également au nom du fichier la date à laquelle le dessin a été édité afin d'avoir un nom unique. Les différentes méthodes sont des petits bouts de dessins pour créer le chemin à afficher dans ```resultat.html```
L'une permet le dessin pour le chemin base et l'autre permet le dessin pour le chemin handicap.

### static

* ```affichage_representation.js```: script qui donne un aperçu des oeuvres
* ```is_fautueil.js```: script qui change les images en fonction de la valeur du slider. 
