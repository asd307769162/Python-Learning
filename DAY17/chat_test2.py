# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:02:29 2018

@author: busby
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)  #将0到10进行1000等分
y = np.sin(x)

plt.figure(figsize = (8, 4))

plt.plot(x, y, label = "$sin(x)$", color="red", linewidth = 2)

plt.xlabel("Time(s)")

plt.ylabel("Volt")

plt.title("PyPlot First Example")

plt.ylim(-1.2, 1.2)

plt.legend()

plt.savefig("PyPlot First Example.jpg", format='jpg', dpi=300)  
plt.show()