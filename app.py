from flask import Flask, render_template, request

from init import init_db, remplir_table_oeuvre, remplir_table_salle, creer_dict
from fonctions import separation_par_types, avoir_id_salles, plus_court_chemin

app = Flask(__name__)

init_db()
remplir_table_oeuvre()
remplir_table_salle()
creer_dict()

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
    liste_id_salles = avoir_id_salles(liste_oeuvres)
    resultat = plus_court_chemin(liste_id_salles)
    return render_template("resultat.html", liste_oeuvres=liste_oeuvres, resultat=resultat)
