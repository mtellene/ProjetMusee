from flask import Flask, render_template

from init import init_db, remplir_table_oeuvre, recuperer_les_oeuvres

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
    oeuvres_liste = recuperer_les_oeuvres()
    return render_template("itineraire.html", oeuvres_liste = oeuvres_liste)
