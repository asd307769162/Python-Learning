# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:16:37 2018

@author: busby
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:09:20 2018

@author: busby
"""

import numpy as np
import matplotlib.pyplot as plt


# 折线一（蓝色虚线）
x = [0,1,2,3,4,5,6]  
y = [0.3,0.4,2,5,3,4.5,4]  

plt.figure(1, figsize=(8, 4))
plt.plot(x, y, "b--", linewidth = 1)

# 折线二（红色实线）
x = [0, 1, 2, 3, 4, 5, 6]
y = [3.9, 3, 4, 3, 2, 1, 0]

plt.figure(1, figsize=(8, 4))
plt.plot(x, y, "red", linewidth = 1)

# 图表信息
plt.legend()
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("Two Line plots")


plt.savefig("Two Line plots.jpg", format='png', dpi=300)  
plt.show()