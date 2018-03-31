# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:09:35 2018

@author: busby
"""
from flask import Flask, session, make_response, redirect, abort, request, render_template, url_for, flash
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
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('name has benn changed')
            return redirect(url_for('form'))
        session['name'] = form.name.data
        return render_template('form_session.html', form = form)
    return render_template('form_session.html', form = form)


if __name__ == '__main__':
    debug=True
    app.run()