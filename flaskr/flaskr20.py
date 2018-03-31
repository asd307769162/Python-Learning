# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:40:24 2018

@author: busby
"""

from flaskr19 import db #导入数据模型
db.create_all() #创建表
db.drop_all() #删除表

# 插入新数据
from flaskr import Role, User
admin_role = Role(name = 'admin', id = 1)
user_admin = User(name = 'admin', role_id = 1)
db.session.add(admin_role)
db.session.add(user_admin)
db.session.commit() # 确认提交数据
db.session.commit()
db.session.rollback() #回滚数据，放弃提交

# 修改行
admin_role.name = 'Adminstrator'
db.session.add(admin_role)
db.session.commit()

# 删除行
db.session.delete(admin_role)
db.session.commit()

# 查询行
User.query.all
User.query.filter_by(name = 'admin').all()

