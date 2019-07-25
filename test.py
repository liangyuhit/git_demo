# -*- coding: utf-8 -*-
'''
Created on 13.05.2019

@author: yu03
'''

import numpy as np
from numpy.polynomial.hermite import hermval
import matplotlib.pyplot as plt
import django
import bokeh
import scipy


a = '2019-5-6 20:03:16'
b = '2019-5-6 20:05:02 from Github'
c = '2019-5-6 20:11:21 from PTB'
d = '2019-05-06 22:08:50 from Home'
e = '2019-05-06 22:14:33 from Github'
f = '2019-05-06 22:16:19 from Home'
g = '2019-05-07 22:26:23 from Home'
h = '2019-05-07 22:27:10 from Github'
i = '2019-5-8 14:15:11 from PTB'
j = '2019-5-8 14:18:49 from Github'
k = '2019-5-13 14:41:42 from PTB'
h = '2019-07-05 @home'
i = '2019-07-24 22:48:57 from pi'
j = '2019-07-24 22:51:26 from Github'
k = '2019-7-25 13:45:05 from PTB'

a = hermval(2, [0,0,1])

print(a)
