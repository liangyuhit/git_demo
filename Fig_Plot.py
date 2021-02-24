# -*- coding: utf-8 -*-
'''
Created on Feb 24, 2021

@author: yl
'''

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimSun']
plt.rcParams['axes.unicode_minus']=False

# V_set = np.linspace(-10, 10, num=15) # in mm
# Resl_set = np.array([100,20,5,5,5,5,5,5,5,5,5,5,5,20,100]) # in pm
# print(len(Resl_set))
# plt.semilogy(V_set, Resl_set,'o-')
# plt.xlim([-15,15])
# plt.ylim([-10,110])
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.grid(which='major', axis='both')
# plt.grid(linestyle='--',which='minor',axis='y')
# plt.show()

X_set = np.linspace(1, 50, num=50) # in mm
Y_set = [0.2, 0.2, 0.12, 0.12, 0.12, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.0231, 0.0231, 0.0231, 0.0231, 0.0231, 0.0231, 0.0231, 0.0231, 0.0231, 0.0231, 0.0231, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013, 0.013] # in pm
print(len(Y_set))
plt.plot(X_set, Y_set,'r')
# plt.xlim([-15,15])
# plt.ylim([-10,110])
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.grid(which='major', axis='both')
# plt.grid(linestyle='--',which='minor',axis='y')
plt.show()

