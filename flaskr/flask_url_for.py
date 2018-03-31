# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:47:20 2018

@author: busby
"""
from flask import Flask, url_for
app = Flask(__name__)
@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass


# 构造url
with app.test_request_context():
    print (url_for('index'))
    print (url_for('login'))
    print (url_for('login', next = '/'))
    print (url_for('profile', username = 'Busby'))