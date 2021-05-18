# ! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    app.py
    traite les requêtes HTTP
"""
__author__ = "Maxime Tellene"
__copyright__ = "Univ Lyon1, 2020"
__license__ = "Public Domain"
__version__ = "3.0"

from flask import Flask, render_template, request, flash, redirect, url_for

from init import initialisation
from fonctions import separation_par_types, charger_resultat, avoir_nom_salles_oeuvres, coloration, dessiner_plan

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # sert pour return redirect(url_for('itineraire'))

# se lance au début du programme
initialisation()


@app.route('/')
def index():
    """
    charge la page index.html, accueil du site
    """
    return render_template("index.html")


@app.route('/plan')
def plan():
    """
    charge la page plan.html, page où il y a les plans du musée
    """
    return render_template("plan.html")


@app.route('/itineraire')
def itineraire():
    """
    charge la page itineraire.html, page où on doit faire notre sélection d'oeuvres
    appel de la separation_par_types() pour le visuel de la page
    """
    ecrits, peintures, sculptures, artefacts = separation_par_types()
    return render_template("itineraire.html", peintures=peintures, ecrits=ecrits, sculptures=sculptures,
                           artefacts=artefacts)


# todo
@app.route('/resultat', methods=['POST'])
def resultat():
    """
    charge la page resultat.html, page où il est affiché le plus court chemin pour voir toutes les oeuvres choisies
        -> récupérer les oeuvres selectionnées (check) (pensez à vérifier que des oeuvres ont été selectionné)
        -> récupérer les noms des salles des oeuvres sélectionnées
        -> appel fonction du plus court chemin
        -> coloration des oeuvres et des salles (pour le visuel)
        -> gérer le cas si aucune oeuvre sélectionnée
    """
    liste_oeuvres = request.form.getlist('check')
    if len(liste_oeuvres) > 0:
        liste_salles = avoir_nom_salles_oeuvres(liste_oeuvres)
        resultat = charger_resultat(liste_oeuvres)
        coloree_salles, coloree_oeuvres = coloration(resultat, liste_oeuvres)
        image0_n, image1_n, image_1_n, image0_f, image1_f, image_1_f = dessiner_plan(coloree_salles)
        print(image0_n, image0_f)
        return render_template("resultat.html", coloree_oeuvres=coloree_oeuvres, liste_salles=liste_salles,
                               coloree_salles=coloree_salles, image0_n=image0_n, image1_n=image1_n, image_1_n=image_1_n,
                               image0_f=image0_f, image1_f=image1_f, image_1_f=image_1_f)
    else:
        flash("Erreur ! Vous n'avez saisi aucunes oeuvres !")
        return redirect(url_for('itineraire'))
