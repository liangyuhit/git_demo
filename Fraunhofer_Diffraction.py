# -*- coding: utf-8 -*-
'''
Created on Jul 15, 2019

@author: yl
'''

import numpy as np
from scipy.special import jv
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

Lamda = 633e-9
Diameter = Lamda * 100
D = 0.1 + Lamda/1

k = 2 * np.pi / Lamda
a = np.pi * Diameter / Lamda
#Theta = np.arctan(dx/D)

x = np.linspace(0, 0.01, 1001)
dx = np.sqrt(np.abs(x - x[501])**2 + 0.005**2)
Theta = np.arctan(dx/D)
# jx = jv(1,x)
I_distribution = 1 / k**2 / D**2 * a**4 * (jv(1, a*np.sin(Theta)) / a / np.sin(Theta))**2
# I_distribution *= signal.gaussian(len(x), std=len(x)/10)


plt.figure(1)
plt.plot(x, I_distribution)
plt.show()








# plt.figure('Bessel J')
# plt.plot(x, jx)
# plt.show()