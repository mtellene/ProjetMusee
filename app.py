from flask import Flask, render_template, request

from init import init_db, remplir_table_oeuvre, remplir_table_salle
from fonctions import separation_par_types, avoir_salles

app = Flask(__name__)

init_db()
remplir_table_oeuvre()
remplir_table_salle()

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
    liste_salles = avoir_salles(liste_oeuvres)
    return render_template("resultat.html", liste_oeuvres=liste_oeuvres, liste_salles=liste_salles)
