from flask import Flask, render_template

from init import init_db, remplir_table_oeuvre

app = Flask(__name__)

@app.route('/')
def index():
    init_db()
    remplir_table_oeuvre()
    return render_template("index.html")

@app.route('/plan')
def hello():
    return render_template("plan.html")
