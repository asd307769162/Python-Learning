# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:46:17 2018

@author: busby
"""

from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/flask'  #设置MySQL
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


app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'

class NameForm(FlaskForm):
    name = StringField('管理员设置', validators=[Required()])
    submit = SubmitField('提交')
    
    
@app.route('/',methods=['GET','POST'])
def database():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user is None:
            user=User(name=form.name.data)
            db.session.add(user)
            db.session.commit()
        session['name']=form.name.data
        form.name.data=''
        return redirect(url_for('database'))
    return render_template('database.html',form=form,name=session.get('name'))

'''
第5行，先从数据库中查询是否存在用户填写的名称的用户。

第6行，进行判断，如果不存在该用户，那么创建一个新User，并添加到db.session中去。然后通过全局变量session将用户名缓存到本地。

第11行，进行重定向，这样刷新页面时就不会重新POST表单。

第12行，返回index.html，将表单对象以及利用session缓存的name传给html。
'''

if __name__ == '__main__':
    app.run()