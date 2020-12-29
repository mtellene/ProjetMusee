from flask import Flask, render_template, request, flash, redirect, url_for

from init import initialisation
from fonctions import separation_par_types, avoir_id_salles, plus_court_chemin, transformation

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

initialisation()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/plan')
def plan():
    return render_template("plan.html")

@app.route('/itineraire')
def itineraire():
    ecrits, peintures, sculptures, artefacts = separation_par_types()
    return render_template("itineraire.html", peintures=peintures, ecrits=ecrits, sculptures=sculptures, artefacts=artefacts)

@app.route('/resultat', methods=['POST'])
def resultat():
    liste_oeuvres = request.form.getlist('check')
    if len(liste_oeuvres) > 0:
        liste_id_salles = avoir_id_salles(liste_oeuvres)
        id_plus_court_chemin = plus_court_chemin(liste_id_salles)
        resultat = transformation(id_plus_court_chemin)
        return render_template("resultat.html", liste_oeuvres=liste_oeuvres, resultat=resultat)
    else:
        flash("Erreur ! Vous n'avez saisi aucunes oeuvres !")
        return redirect(url_for('itineraire'))
