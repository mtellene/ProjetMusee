# ProjetMusee

Projet Musee est un projet de calcul d'itinéraire dans un musée. Il permet de calculer le plus court chemin en terme de nombre de salles traversées pour voir les oeuvres choisies par l'utilisateur.

Pour mettre en forme ce projet, un musée factice a été créé mais également un site web a été créé ainsi qu'une base de données avec toutes les oeuvres du musée.

#### Base de données  

Les lignes de la base de données sont construites de la façon suivante: 
id | nom de l'oeuvre | artiste | type | représentation (img) | salle

#### Fichiers Json

Pour remplir la table `oeuvres` de la base de donnée, le fichier `oeuvres.json` est utilisé. Ce fichier est constitué d'un tableau d'objets où chaque objet correspond à une oeuvre. Un objet se construit de la forme suivante:

- type 

- artiste

- titre

- salle

- representation

#### Découpage web

- `index.html` est la page d'acceuil du site

- `itineraire.html` est la page où l'utilisateur choisit les oeuvres qu'il veut voir et valide son (ou ses) choix

- `plan.html` est la page où l'on peut voir le plan du musée

#### Fonctions de `init.py`

- `init_db()` est une fonction qui supprime le contenu de la base de données (s'il y en avait un) et crée ensuite la (ou les) nouvelle(s) table(s)

- `recuperer_les_oeuvres()` est une fonction qui récupère les champs d'une oeuvre dans le fichier `oeuvres.json` et les ajoute à une liste. Cette liste est ensuite retournée.

- `remplir_table_oeuvre()` est une fonction qui récupère la liste retournée par la fonction précédente et remplit la table `oeuvres` de la base de données avec les informations correspondantes.

#### Fonctions de `app.py`

`app.py` permet de faire le lien entre les différentes pages HTML

- `index()` permet d'aller à la page `index.html`

- `plan` permet d'aller à la page `plan.html`

- `itineraire` permet d'aller à la page `itineraire.html`












