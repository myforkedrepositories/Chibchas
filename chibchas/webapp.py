from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, validators
from flask_bootstrap import Bootstrap
import pathlib

# App config.
DEBUG = True
app = Flask(__name__, template_folder=str(
    pathlib.Path(__file__).parent.absolute()) + '/templates/')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

Bootstrap(app)


class WebForm(Form):
    name = TextField('Usuario:', validators=[validators.required()])
    password = TextField('Contraseña:', validators=[
                         validators.required(), validators.Length(min=3, max=35)])
    apikey = TextField('Apikey:', validators=[
                       validators.required(), validators.Length(min=3, max=35)])


@app.route("/", methods=['GET', 'POST'])
def login():
    form = WebForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        apikey = request.form['apikey']
        print(name, " ", apikey, " ", password)

    if form.validate():
        # Save the comment here.
        flash('Thanks for registration ' + name)
    else:
        flash('Error: All the form fields are required. ')

    return render_template('login.html', form=form)


def run_server():  # to do ip and port
    app.run()
