from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

from flask_app.models import ninja,dojo


    
@app.route('/create/ninja', methods=['POST','GET'])
def new_ninja():
    if request.method =='GET':
        return render_template("new_ninja.html", dojos=dojo.Dojo.get_all_dojos())
    if request.method == 'POST':
        Ninja.save(request.form)
    print(request.form)
    return redirect('/')


# @app.route('/edit/user/<int:ninja_id>')
# def edit_user(ninja_id):
#         return render_template('update.html', one_ninja = Ninja.get_one(ninja_id))

# @app.route('/update/user', methods=['POST'])
# def update_user():
#     Ninja.update(request.form)
#     print(request.form)
#     return redirect('/')




# @app.route('/delete/<int:ninja_id>')
# def delete(ninja_id):
#     Ninja.delete(ninja_id)
#     return redirect('/')


