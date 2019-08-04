# -*- coding: utf-8 -*-
'''
Created on Aug 4, 2019

@author: yl
'''
import numpy as np
import matplotlib.pyplot as plt

j = complex(0, 1)
c = 3e8 # 光速 [m/s]
Lamda = 633e-9 # 光波长 [m]
Fc = c / Lamda # 光频率 [Hz]
k = 2 * np.pi / Lamda

P = 1 #功率
w0 = 1000e-6
Z_R = np.pi * w0**2 / Lamda

Z_pos = 0.1
w_z = w0 * np.sqrt(1 + Z_pos**2/Z_R**2)
R_z = Z_pos * (1 + Z_R**2/Z_pos**2)
Gouy_Z = np.arctan(Z_pos/Z_R)

X = np.linspace(-0.0025, 0.0025, num=301)
Y = X
x, y = np.meshgrid(X, Y)
r = np.sqrt(x**2 + y**2)
A = np.sqrt(2*P/np.pi/(w_z**2)) * np.exp(-r**2/w_z**2)
Phi = k*r**2/2/R_z - Gouy_Z + k*Z_pos
# E = A * np.exp(j * (2*np.pi*Fc*t-Phi))
plt.figure(1)
c = plt.gca().pcolor(X, Y, A, cmap='gray')
plt.xlabel('dx [mm]')
plt.ylabel('dy [mm]')
plt.colorbar(c, ax=plt.gca())

plt.show()
