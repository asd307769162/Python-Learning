# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:18:11 2018

@author: busby
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/if')
def if_():
    return render_template('if.html', user = 'Busby')


@app.route('/')
def index():
    comments = ['nihao', '123', 'test']
    return render_template('for.html', comments = comments)
    
    
if __name__ == '__main__':
    app.run()