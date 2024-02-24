from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models import dojo,ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template("dojo.html", dojos=Dojo.get_all_dojos())
    

@app.route('/create', methods=['POST'])
def create():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/show/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    Dojo.get_one_dojo_with_ninjas(data)
    return render_template("show_dojo.html" , dojo=Dojo.get_one_dojo_with_ninjas(data))