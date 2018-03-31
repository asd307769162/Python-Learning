# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:28:54 2018

@author: busby
"""

from flask import Flask
from flask_script import Manager  

app = Flask(__name__)

manager = Manager(app)

if __name__ == '__main__':
    manager.run()