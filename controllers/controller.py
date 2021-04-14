from flask import render_template
from app import app
from modules.calculator import *

@app.route("/add/<num_1>/<num_2>")
def add_page():
    num_1 = int(num_1)
    num_2 = int(num_2)
    total = add(num_1,num_2)
    return render_template("add.html")