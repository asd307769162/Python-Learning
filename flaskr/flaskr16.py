# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:09:35 2018

@author: busby
"""
from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

class NameForm(FlaskForm):
    name = StringField('your name', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods= ['GET', 'POST'])
def form():
    form = NameForm()
    return render_template('form.html', form = form)


if __name__ == '__main__':
    debug=True
    app.run()