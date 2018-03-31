# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:18:11 2018

@author: busby
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/common/')
def common_test():
    return render_template('common_test.html')
    
    
if __name__ == '__main__':
    app.run()