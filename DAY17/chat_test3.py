# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:09:20 2018

@author: busby
"""

import numpy as np
import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6]  
y = [0.3,0.4,2,5,3,4.5,4]  

plt.figure(figsize=(8, 4))
plt.plot(x, y, "b--", linewidth = 1)
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("Line plot")

plt.savefig("Line plot.jpg", format='jpg', dpi=300)  
plt.show()