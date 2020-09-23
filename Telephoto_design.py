# -*- coding: utf-8 -*-
'''
Created on 02.09.2020

@author: yu03
'''


f1 = 0.125
f2 = -0.05
f = 0.25
d = f1 + f2 - f1*f2/f
# d=0.09
Ld = (f1*f2 + d*(f1-d)) / (f1 + f2 -d)
c = Ld / f
print(d, Ld, c)