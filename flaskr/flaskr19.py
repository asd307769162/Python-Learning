# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 17:59:14 2018

@author: busby
"""



from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:19980501.@localhost/flask'  #设置MySQL
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True  #设置自动提交commit
db = SQLAlchemy(app)

class Role(db.Model):  
    __tablename__='roles'  
    id = db.Column(db.Integer,primary_key=True)  
    name = db.Column(db.String(64),unique=True)  
    users = db.relationship('User',backref='role')
        
    def __repr__(self):  
        return '<Role %s>'%self.name  

class User(db.Model):  
    __tablename__='users'  
    id=db.Column(db.Integer,primary_key=True)  
    name=db.Column(db.String(64),unique=True)  
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    def __repr__(self):  
        return '<User %s>'%self.name  

