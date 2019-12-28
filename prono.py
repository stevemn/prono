from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
bootstrap = Bootstrap(app)

class UrlForm(FlaskForm):
    url = StringField('Parse URL', validators=[URL()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/parse')
def parse():
    form = UrlForm()
    return render_template('url_input.html', form=form)
