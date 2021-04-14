from flask import render_template
from app import app
from modules.calculator import *

@app.route("/add/<num_1>/<num_2>")
def add_page(num_1, num_2):
    num_1 = int(num_1)
    num_2 = int(num_2)
    total = add(num_1,num_2)
    return render_template("add.html", num_1 = num_1, num_2 = num_2, total = total)

@app.route("/subtract/<num_1>/<num_2>")
def subtract_page(num_1, num_2):
    num_1 = int(num_1)
    num_2 = int(num_2)
    total = subtract(num_1,num_2)
    return render_template("subtract.html", num_1 = num_1, num_2 = num_2, total = total)

@app.route("/multiply/<num_1>/<num_2>")
def multiply_page(num_1, num_2):
    num_1 = int(num_1)
    num_2 = int(num_2)
    total = multiply(num_1,num_2)
    return render_template("multiply.html", num_1 = num_1, num_2 = num_2, total = total)

@app.route("/divide/<num_1>/<num_2>")
def divide_page(num_1, num_2):
    num_1 = int(num_1)
    num_2 = int(num_2)
    total = divide(num_1,num_2)
    return render_template("divide.html", num_1 = num_1, num_2 = num_2, total = total)