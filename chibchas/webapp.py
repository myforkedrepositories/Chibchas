from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import pathlib

# App config.
DEBUG = True
app = Flask(__name__,template_folder=str(pathlib.Path(__file__).parent.absolute()) + '/templates/')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class WebForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])

    def reset(self):
            blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
            self.process(blankData)
                
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = WebForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        name=request.form['name']
        password=request.form['password']
        email=request.form['apikey']
        print( name, " ", email, " ", password)

    if form.validate():
    # Save the comment here.
        flash('Thanks for registration ' + name)
    else:
        flash('Error: All the form fields are required. ')

    return render_template('login.html', form=form)

def run_server():#to do ip and port
    app.run()