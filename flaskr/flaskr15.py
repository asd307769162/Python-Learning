# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:01:06 2018

@author: busby
"""

from flask import Flask
from flask import g


app = Flask(__name__)

@app.before_request  
def bf_request():  
    g.string = 'before_request'  
        
@app.before_first_request  
def bf_first_request():  
    g.string = 'before_first_request'  
 
@app.after_request  
def af_request(param):  
    return param  

@app.teardown_request  
def td_request(param):  
    return param  
    
@app.route('/test')
def test():
    return g.string



if __name__ == "__main__":
    app.run()