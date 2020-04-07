# -*- coding: utf-8 -*-
'''
Created on 07.04.2020

@author: yu03
'''

import numpy as np
import matplotlib.pyplot as plt

Vrx,Vry=2e-3,2e-3
Vmx,Vmy=0,0

Vmy_set = np.linspace(-1e-3,1e-3,num=10)
Vmx = np.linspace(-1e-3,1e-3,num=10)
for Vmy in Vmy_set:
    theta = Vmx/(1+Vmx**2+Vmy**2)-Vrx/(1+Vrx**2+Vry**2)
    error = theta-Vmx+Vrx
    plt.plot(error)

plt.show()