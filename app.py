from flask import Flask, render_template

from init import init_db, remplir_table_oeuvre
from fonctions import separation_par_types

app = Flask(__name__)

init_db()
remplir_table_oeuvre()

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
