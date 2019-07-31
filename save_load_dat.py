# -*- coding: utf-8 -*-
'''
Created on 31.07.2019

@author: yu03
'''
import numpy as np

file_name = 'test.npy'

a = np.zeros(10)
print(a)
f = open(file_name,'wb')
np.save(f, a)