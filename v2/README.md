## README de la version v2

### Structure dossiers
* ```db``` contient la base de données, la matrice d'adjacence et le ficher oeuvre.json qui contient toutes les oeuvres (pour la création de la bd)
* ```static``` contient les fichiers ```*.png``` et ```*.css``` 
* ```templates``` contient les fichiers ```*.html```

### Structure code
#### init.py
* ```mon_graph```: dictionnaire qui représente le graphe du musée, est de la forme {salle (str) : successeur(s) de salle (liste de str)}
* ```liste_des_salles```: liste qui contient toutes les salles du musée (str)
* ```couleurs_salles```: liste qui contient des couleurs au format hexadécimal (str)


* ```init_db()```: supprime l'ancienne base de données et en crée une vide
* ```recuperer_les_oeuvres()```: parse le fichier ```oevres.json``` afin de récupérer une liste avec toutes les oeuvres sous formes de tuple
* ```remplir_table_oeuvre()```: appelle la fonction précédente pour remplir la base de données
* ```creation_db()```: appelle ```init_db()``` et ```remplir_table_oeuvre()``` pour initialiser une base de données vide et la remplir
* ```creer_dict()```: remplit un dictionnaire représentant le graphe du musée en lisant la matrice d'adjacence ```todo pour les élèves```

#### app.py
Récupère les requêtes HTTP

* ```initialisation()``` 
*
*
*
*
### Todo
* Régler le problème des images:
    * nombre des œuvres des arts visuels utilisées est limité à 20 œuvres par travail pédagogique :white_check_mark:
    * définition limitée à 400 x 400 pixels :x:
    * une résolution limitée à 72 DPI (point par pouce) :x:
* Faire le trajet pour la page résultat
### Utiles 

- site pour les droits d'auteur/exceptions pédagogiques:
https://www.reseau-canope.fr/savoirscdi/societe-de-linformation/cadre-reglementaire/le-coin-du-juriste/le-point-sur-lexception-pedagogique-au-29-septembre-2016.html
  
