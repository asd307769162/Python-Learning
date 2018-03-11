# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:43:03 2018

@author: busby
"""

import numpy as np
import matplotlib.pyplot as plt

x = [0, 1]
y = [0, 1]


plt.figure()
plt.plot(x, y)
plt.xlabel("time(s)")
plt.ylabel("value(m)")
plt.title("A simple plot")


plt.savefig("A simple plot.jpg", format='jpg', dpi=300)  
plt.show()