# -*- coding: utf-8 -*-
'''
Created on 15.08.2019

@author: yu03
'''
import numpy as np
import matplotlib.pyplot as plt

x = 0.01
y = x
L = 1
Vx = np.linspace(0, 0.01, 1000)
Vy = Vx

r_real = np.sqrt( x**2 + y**2 + L**2 - ((2*x*Vx+2*y*Vy+L*(1-Vx**2-Vy**2))/(1+Vx**2+Vy**2))**2 )
print(r_real)

r = np.sqrt(x**2+y**2+L**2 - (2*x*Vx+2*y*Vy+L)**2)
print(r)

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(r_real, 'b')
plt.plot(r, 'r')
plt.grid(which='both', axis='both')
plt.subplot(2,1,2)
plt.plot(r - r_real, 'k')
plt.grid(which='both', axis='both')
plt.show()