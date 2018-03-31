# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 18:35:02 2018

@author: busby
"""

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)
app.config['SECRET_KEY']='secret_key'
manager=Manager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:19980501.@localhost/flask'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db=SQLAlchemy(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)


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
      role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))  
      age=db.Column(db.Integer)  

if __name__=='__main__':  
    manager.run()  
