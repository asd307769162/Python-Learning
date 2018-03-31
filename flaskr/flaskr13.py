# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:34:38 2018

@author: busby
"""

from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/user/<name>')
def test(name):
    return render_template('test.html', name = name)

if __name__ == '__main__':
    app.run()