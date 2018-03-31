# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:09:40 2018

@author: busby
"""

from flaskr19 import Role, User, db
r = Role(id = 1, name = 'admin')
u = User(id = 10, name = 'Busby', role_id = 1)
r.users.append(u)
print(u.role)
print(u.name)
db.session.add(u) #增加u用户
db.session.commit() #确认增加u用户
