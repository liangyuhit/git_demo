# -*- coding: utf-8 -*-
'''
Created on 08.08.2019

@author: yu03
'''

import numpy as np

a = np.arange(24)
print(a)
# b = a.reshape(5,2,order='F')
# print(b)
c = np.reshape(a, (len(a)//3,-1))
print(c)
print(len(c))
d = np.mean(c,axis=1)
print(d)
print(len(d))