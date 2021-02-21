# -*- coding: utf-8 -*-
'''
Created on Feb 20, 2021

@author: yl
'''
from sympy import *

x = symbols('x')

a = integrate(1/(1+x*x) ,x)
print(a)
