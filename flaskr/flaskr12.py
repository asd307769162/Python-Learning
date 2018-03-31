# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:34:38 2018

@author: busby
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

if __name__ == '__main__':
    app.run()