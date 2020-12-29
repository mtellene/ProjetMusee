from flask import Flask, render_template, request, flash, redirect, url_for

from init import initialisation
from fonctions import separation_par_types, charger_resultat, avoir_nom_salles_oeuvres

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# fonction(s) qui se lance(ent) dès le début du programme
initialisation()

# accueil du site
@app.route('/')
def index():
    return render_template("index.html")

# onglet plan
@app.route('/plan')
def plan():
    return render_template("plan.html")

# onglet itineraire
@app.route('/itineraire')
def itineraire():
    ecrits, peintures, sculptures, artefacts = separation_par_types()   # permet de separer les oeuvres en categories
    return render_template("itineraire.html", peintures=peintures, ecrits=ecrits, sculptures=sculptures, artefacts=artefacts)

# page quand on a choisit les oeuvres a voir
@app.route('/resultat', methods=['POST'])
def resultat():
    liste_oeuvres = request.form.getlist('check')
    if len(liste_oeuvres) > 0:  # si au moins une oeuvre a ete selectionnee
        liste_salles = avoir_nom_salles_oeuvres(liste_oeuvres)
        resultat = charger_resultat(liste_oeuvres)  # charge le plus court chemin
        return render_template("resultat.html", liste_oeuvres=liste_oeuvres, resultat=resultat, liste_salles=liste_salles)
    else:   # si aucunes oeuvres selectionnees
        flash("Erreur ! Vous n'avez saisi aucunes oeuvres !")
        return redirect(url_for('itineraire'))
