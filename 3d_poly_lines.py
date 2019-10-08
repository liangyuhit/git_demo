# -*- coding: utf-8 -*-
'''
Created on 28.08.2019

@author: yu03
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0, 10, 2000)
line_num = 10
z = np.zeros([line_num, 2000])

for i in range(line_num):
    z[i, :] = np.sin(2 * np.pi * t * (i + 1) * 0.2)

x = [np.linspace(0, 9, line_num)] * 2000
y = [np.linspace(0, 1999, 2000)] * line_num
x = np.array(x).T
y = np.array(y)

fig = plt.figure(figsize=(6, 2.5))

ax = fig.gca(projection='3d')
plt.gca().patch.set_facecolor('white')
for i in range(line_num):
    ax.plot(x[i, :], y[i, :], z[i, :])
# ax.view_init(20,60)
# fig.set_size_inches(6, 2.5)
# fig.savefig('fig6.png',dpi=1200)
plt.show()
