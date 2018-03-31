# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 20:18:38 2018

@author: busby
"""

from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/flask'  #设置MySQL
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True  #设置自动提交commit
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    
    def __repr__(self):
        return('<Role %s>' %self.name)
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    
    def __repr__(self):
        return('<User %s>' %self.name)

if __name__ == '__main__':
    app.run()