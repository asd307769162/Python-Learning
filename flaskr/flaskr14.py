# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 22:03:35 2018

@author: busby
"""

from flask_moment import Moment
from flask import Flask
from flask import render_template

app = Flask(__name__)
Moment(app)


@app.route('/')
def local_time():
    return render_template('localtime.html')


if __name__ == '__main__':
    app.run()