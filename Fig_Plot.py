# -*- coding: utf-8 -*-
'''
Created on Feb 24, 2021

@author: yl
'''

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimSun']
plt.rcParams['axes.unicode_minus']=False

V_set = np.linspace(-10, 10, num=15) # in mm
Resl_set = np.array([100,20,5,5,5,5,5,5,5,5,5,5,5,20,100]) # in pm
# noise = np.array([np.random.normal(1, 0.8, 21)])
# Resl_set = Resl_set + noise
# Resl_set = Resl_set[0]
print(len(Resl_set))
plt.semilogy(V_set, Resl_set,'o-')
plt.xlim([-15,15])
plt.ylim([-10,110])
# plt.ylabel('动态分辨力 (pm)')
# plt.xlabel('速度变化范围 (mm/s)')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.grid(which='major', axis='both')
plt.grid(linestyle='--',which='minor',axis='y')
plt.show()

