# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 20:58:29 2018

@author: busby
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

if __name__ == '__main__':
    app.run()