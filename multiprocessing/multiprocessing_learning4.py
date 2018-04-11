# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 08:51:22 2018

@author: busby
"""

import mmultiprocessing as mp

value = mp.Value('d', 1)
array = mp.Array('i',[1,2,3]) #只能为一位数组