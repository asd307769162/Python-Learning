# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:22:04 2018

@author: busby
"""

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User_Agent')
    return 'user_agent is %s' %user_agent

if __name__ == '__main__':
    app.run()