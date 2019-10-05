# -*- coding: utf-8 -*-
'''
Created on Oct 5, 2019

@author: yl
'''

import numpy as np
from sympy import *

f, d = symbols('f d')

# f=3
# d =1
m_lens = np.array([[1,0],[-1/f,1]])
m_d = np.array([[1,d],[0,1]])
# m = np.dot(m_lens, m_d)
# print(m) 

m_lens = np.mat(m_lens)
m_d = np.mat(m_d)
m = m_lens * m_d
print(m)
