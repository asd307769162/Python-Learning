# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:04:55 2018

@author: busby
"""

from flask import Flask
from flask import render_template

class Myobj(object):
    def __init__(self, name):
        self.name = name
        
    def getname(self):
        return self.name

app = Flask(__name__)

@app.route('/')
def index():
    mydict = {'key1':'123', 'key':'hello'}
    mylist = (123, 234, 345, 789)
    myintvar = 1
    myobj = Myobj('Hyman')
    return render_template('param.html', mydict = mydict, mylist = mylist, myintvar = myintvar, myobj = myobj)

if __name__ == '__main__':
    app.run()