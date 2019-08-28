# -*- coding: utf-8 -*-
'''
Created on 08.08.2019

@author: yu03
'''

import numpy as np

a = np.arange(10)
print(a)

b = a.reshape(5,2,order='F')
print(b)

c = a.reshape(2, 5)
print(c)